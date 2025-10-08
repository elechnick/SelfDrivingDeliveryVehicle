import Mock.GPIO as GPIO
import time

class ObstacleAvoidance:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def get_distance(self):
        # Ensure trigger is low
        GPIO.output(self.trigger_pin, False)
        time.sleep(0.0002)

        # Send 10us pulse
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)

        start_time = time.time()
        stop_time = time.time()

        # Wait for echo to start
        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()

        # Wait for echo to end
        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()

        # Time difference * speed of sound / 2
        time_elapsed = stop_time - start_time
        distance = (time_elapsed * 34300) / 2  # cm
        return distance

    def detect_obstacle(self, threshold=20):
        distance = self.get_distance()
        print(f"Measured distance: {distance:.2f} cm")

        if distance <= threshold:
            print("Obstacle detected!")
            return True
        return False

    def avoid_obstacle(self, navigator):
        print("Avoiding obstacle...")
        navigator.stop()
        time.sleep(0.5)
        navigator.turn("left")
        time.sleep(1)
        navigator.go_straight()
        time.sleep(1)
        navigator.stop()
