import tkinter as tk
from PIL import Image, ImageTk

from camera_feed import CameraFeed
from ai_model import AIModel
from car_controller import CarController

class RobotGUI:
    def __init__(self, stream_url, icon_path):
        self.root = tk.Tk()
        self.root.title("Live Camera Feed")
        self.root.iconphoto(True, tk.PhotoImage(file=icon_path))

        self.camera = CameraFeed(stream_url)
        self.ai_model = AIModel()
        self.robot = CarController()

        self.label = tk.Label(self.root)
        self.label.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Start UI loop
        self.update_gui()
        self.root.mainloop()

    def update_gui(self):
        frame = self.camera.frame
        if frame is not None:
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)

            # AI detection
            label, conf = self.ai_model.predict(frame)
            if label:
                print(f"[AI] {label} ({conf:.2f})")
                self.robot.handle_label(label)

        self.root.after(30, self.update_gui)

    def on_close(self):
        print("[CLEANUP] Stopping robot and camera")
        self.camera.stop()
        self.robot.stop()
        self.root.destroy()
