# car_controller.py
import time
from navigation import BasicNavigation
from model import Model_Run
from servo import CameraServo

class CarController:
    def __init__(self):
        self.nav = BasicNavigation()
        self.model = Model_Run()
        self.servo = CameraServo(pin=12)

        self.rotated = False 
        self.TARGET = "banana"
        self.STOP_LABEL = "stop"
        self.THRESHOLD = 0.7

        self.servo.center()
        print("[INIT] CarController ready.")

    def process_frame(self, frame):
        """Runs model prediction and returns (label, conf)"""
        label, conf = self.model.classify_frame(frame)
        print(f"[AI] {label} ({conf:.2f})")
        return label, conf

    def handle_label(self, label):
        """Handles behaviour based on detected label."""
        print(f"[DEBUG] Handling label: {label}")

        if label == self.STOP_LABEL:
            print("[EVENT] STOP detected → Stopping motors")
            self.nav.stop()
            return

        if label == self.TARGET:
            if not self.rotated:
                print("[EVENT] Banana detected → rotating camera RIGHT")
                self.nav.stop()
                self.servo.right_90()
                time.sleep(1)  # give servo time to move
                self.rotated = True
                return
            else:
                print("[EVENT] Banana seen again → waiting 10s")
                self.nav.stop()
                time.sleep(10)
                print("[EVENT] Returning camera to CENTER")
                self.servo.center()
                time.sleep(1)
                self.rotated = False
                print("[EVENT] Resuming straight drive")
                self.nav.go_straight()
                return

        if not self.rotated:
            print("[ACTION] Driving straight")
            self.nav.go_straight()
        else:
            print("[ACTION] Rotated state → Staying stopped")
            self.nav.stop()
