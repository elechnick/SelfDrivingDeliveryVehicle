# Controls vehicle motors

import Mock.GPIO as GPIO

# Initialize GPIO pins
pins = list(range(1, 14))
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

GPIO.setmode(GPIO.BCM)

class BasicNavigation:
    def __init__(self, distance=0, angle=0):
        self.distance = distance
        self.angle = angle

    def go_straight(self):
        # Activate motors to move forward
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(8, GPIO.HIGH)

    def turn(self, direction):
        if direction == "left":
            GPIO.output(3, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(7, GPIO.LOW)
            GPIO.output(8, GPIO.HIGH)
        elif direction == "right":
            GPIO.output(3, GPIO.LOW)
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(8, GPIO.LOW)

    def stop(self):
        for pin in range(1, 5):
            GPIO.output(pin, GPIO.LOW)
