import time
from camera_feed import CameraFeed
from ai_model import AIModel
from car_controller import CarController

def main():
    STREAM_URL = "http://192.168.4.1:81/stream"

    print("[SYSTEM] Starting car...")
    camera = CameraFeed(STREAM_URL)
    ai = AIModel(threshold=0.70)
    car = CarController()

    print("[SYSTEM] Car is now ACTIVE.")
    print("[SYSTEM] Driving...")

    try:
        while True:
            frame = camera.frame
            if frame is None:
                time.sleep(0.05)
                continue

            label, conf = ai.predict(frame)
            ai_took_control = False

            if label:
                ai_took_control = car.handle_label(label)

            if not ai_took_control:
                obstacle = car.obstacle_step()

                if not obstacle:
                    car.normal_drive()

            time.sleep(0.03)

    except KeyboardInterrupt:
        print("\n[SHUTDOWN] Stopping car...")
        car.stop()
        camera.stop()

if __name__ == "__main__":
    main()
