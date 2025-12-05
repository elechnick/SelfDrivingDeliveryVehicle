import traceback
from model import Model_Run

class AIModel:
    def __init__(self, threshold=0.7):
        self.model = Model_Run()
        self.threshold = threshold

    def predict(self, frame):
        try:
            label, conf = self.model.classify_frame(frame)
            if conf >= self.threshold:
                return label, conf
            return None, None
        except Exception:
            traceback.print_exc()
            return None, None
