# Controls vehicle motors using Mock GPIO
import Mock.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Initialize GPIO pins safely
pins = [3, 6, 7, 8]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

class BasicNavigation:
    def __init__(self):
        print("Navigation system initialized.")

    def go_straight(self):
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(8, GPIO.HIGH)
        print("Moving forward...")

    def turn(self, direction):
        if direction == "left":
            GPIO.output(3, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(7, GPIO.LOW)
            GPIO.output(8, GPIO.HIGH)
            print("Turning left...")
        elif direction == "right":
            GPIO.output(3, GPIO.LOW)
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(8, GPIO.LOW)
            print("Turning right...")
        else:
            print("Invalid turn direction specified.")

    def stop(self):
        for pin in [3, 6, 7, 8]:
            GPIO.output(pin, GPIO.LOW)
        print("Motors stopped.")
