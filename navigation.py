import Mock.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class BasicNavigation:
    def go_straight(self):
        # Move both motors forward
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(8, GPIO.LOW)

    def turn(self, direction):
        if direction == "left":
            GPIO.output(3, GPIO.LOW)
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(8, GPIO.LOW)
        elif direction == "right":
            GPIO.output(3, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(7, GPIO.LOW)
            GPIO.output(8, GPIO.HIGH)

    def stop(self):
        # Stop all motors
        for pin in [3, 6, 7, 8]:
            GPIO.output(pin, GPIO.LOW)
