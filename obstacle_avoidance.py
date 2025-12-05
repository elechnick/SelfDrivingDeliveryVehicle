import Mock.GPIO as GPIO
import time

class ObstacleAvoidance:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)
        GPIO.output(trigger_pin, False)

    def get_distance(self):
        readings = []

        for _ in range(5):  # take # quick readings

            GPIO.output(self.trigger_pin, True)
            time.sleep(0.00001)
            GPIO.output(self.trigger_pin, False)

            # wait for echo start
            start = time.time()
            while GPIO.input(self.echo_pin) == 0:
                start = time.time()

            # wait for echo end
            stop = time.time()
            while GPIO.input(self.echo_pin) == 1:
                stop = time.time()

            elapsed = stop - start
            d = (elapsed * 34300) / 2  # cm

            # keep only valid readings
            if 1 < d < 300:
                readings.append(d)

            time.sleep(0.003)

        if not readings:
            return 999

        # median (middle value)
        readings.sort()
        median = readings[len(readings) // 2]

        return median

    def detect_obstacle(self, threshold=6):
        distance = self.get_distance()

        return distance < threshold

    def avoid_obstacle(self, navigator):
        navigator.stop()
        time.sleep(0.1)

        navigator.reverse()
        time.sleep(0.15)

        navigator.turn("left")
        time.sleep(0.4)

        navigator.stop()
        time.sleep(0.15)
