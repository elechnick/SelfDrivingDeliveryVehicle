import cv2
import time
import threading

class CameraFeed:
    def __init__(self, url, frame_delay=0.2):
        self.url = url
        self.frame_delay = frame_delay
        self.cap = cv2.VideoCapture(url)
        self.frame = None
        self.running = True
        if not self.cap.isOpened():
            raise RuntimeError(f"Cannot open camera stream: {url}")
        threading.Thread(target=self._update, daemon=True).start()

    def _update(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                self.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            time.sleep(self.frame_delay)

    def stop(self):
        self.running = False
        self.cap.release()
