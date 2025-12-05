import cv2
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Load model and labels once
model = load_model("keras_model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()


class Model_Run:
    def __init__(self):
        self.model = model
        self.class_names = class_names
        self.size = (224, 224)

    def classify_frame(self, frame):
        # Convert OpenCV BGR frame → RGB PIL Image
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Resize to 224x224
        image = ImageOps.fit(image, self.size, Image.Resampling.LANCZOS)

        # Convert to numpy array
        image_array = np.asarray(image)

        # Normalize
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        # Data shape (1, 224, 224, 3)
        data = np.expand_dims(normalized_image_array, axis=0)

        # Predict
        prediction = self.model.predict(data)
        index = np.argmax(prediction)
        label = self.class_names[index].strip()
        confidence = prediction[0][index]

        return label, confidence
