from time import sleep, time
import RPi.GPIO as GPIO

for i in range(100):

    GPIO.setmode(GPIO.BCM)

    TRIG = 23
    ECHO = 24

    print('measuring now')

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    print('sensor settling')
    sleep(.1)

    GPIO.output(TRIG, True)
    sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start_time = time()
    while GPIO.input(ECHO) == 1:
        pulse_end_time = time()


    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print(distance)
    GPIO.cleanup()
