# Handles obstacle detection and avoidance

import Mock.GPIO as GPIO
import time

class ObstacleAvoidance:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)

    def get_distance(self):
        # Measures distance using an ultrasonic sensor.
        # Returns distance in centimeters.
        # Send 10us pulse to trigger
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)

        # Wait for echo start
        start_time = time.time()
        stop_time = time.time()

        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()

        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()

        # Calculate distance in cm
        time_elapsed = stop_time - start_time
        distance = (time_elapsed * 34300) / 2  # Speed of sound = 34300 cm/s

        return distance

    def detect_obstacle(self, threshold=10):
       #  detects if there is an obstacle within threshold distance (cm).
       #  returns true if obstacle detected, False otherwise.

        distance = self.get_distance()
        return distance < threshold

    def avoid_obstacle(self, navigator):
       # basic avoidance maneuver: stops, turns, and moves forward.
       # `navigator` is an instance of BasicNavigation.

        navigator.stop()
        time.sleep(0.5)
        navigator.turn("left")  # Turn left to avoid
        time.sleep(1)  # Adjust duration for proper turning
        navigator.go_straight()
        time.sleep(1)  # Move forward to bypass obstacle
        navigator.stop()
