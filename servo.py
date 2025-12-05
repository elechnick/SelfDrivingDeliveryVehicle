import Mock.GPIO as GPIO
import time

class CameraServo:
    def __init__(self, pin=12):
        self.pin = pin # pin 10
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(0)

    def set_angle(self, angle):
        duty = 2 + (angle / 18)
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(0.25)

    def center(self):         # camera looking forward
        self.set_angle(90)

    def right_90(self):       # rotate camera 90 degrees right
        self.set_angle(0)

    def left_90(self):        # rotate camera 90 degrees left
        self.set_angle(180)
