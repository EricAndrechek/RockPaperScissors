import RPi.GPIO as GPIO
from time import sleep

# this is first two fingers extended
def tfe():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    pwm3=GPIO.PWM(3, 50)
    pwm3.start(0)
    sleep(0.5)
    pwm3.ChangeDutyCycle(12)
    sleep(0.5)
    pwm3.stop()
    GPIO.cleanup()

# this is the second two fingers extended
def sfe():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    pwm11=GPIO.PWM(11, 50)
    pwm11.start(0)
    sleep(0.5)
    pwm11.ChangeDutyCycle(2)
    sleep(0.5)
    pwm11.stop()
    GPIO.cleanup()

# this is first two fingers brought in
def tfi():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    pwm3=GPIO.PWM(3, 50)
    pwm3.start(0)
    sleep(0.5)
    pwm3.ChangeDutyCycle(2)
    sleep(0.5)
    pwm3.stop()
    GPIO.cleanup()

# this is the second two fingers brought in
def sfi():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    pwm11=GPIO.PWM(11, 50)
    pwm11.start(0)
    sleep(0.5)
    pwm11.ChangeDutyCycle(12.5)
    sleep(0.5)
    pwm11.stop()
    GPIO.cleanup()


