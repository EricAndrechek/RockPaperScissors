from picamera import PiCamera
from PIL import Image
from time import sleep, time
import RPi.GPIO as GPIO
import glob
import os
import pyml
from play import rock, paper, scissors, updown
import random


list_of_files = glob.glob('images/raw-images/*')
latest_file = max(list_of_files, key=os.path.getctime)
latest_file_number = int(latest_file[22:][:-4]) + 1


def grey(num):
    global cam
    cam.capture('images/raw-images/hand' + num + '.jpg')
    cam.stop_preview()
    sleep(1)
    # start_time = time()
    n = Image.open('images/raw-images/hand' + num + '.jpg')
    n = n.convert('RGBA')
    s = n.size
    m = n.load()
    for x in range(s[0]):
        for y in range(s[1]):
            r, g, b, a = m[x, y]
            if g > 200 and r < 150 and b < 150:
                m[x, y] = 255, 255, 255, 0
            elif g > 125 and r < 75 and b < 75:
                m[x, y] = 255, 255, 255, 0
            elif g > 100 and r < 10 and b < 60:
                m[x, y] = 255, 255, 255, 0
            elif g > 100 and r < 60 and b < 10:
                m[x, y] = 255, 255, 255, 0
            elif g > (r + b):
                m[x, y] = 255, 255, 255, 0
            elif g > 255 and b < 175 and r < 175:
                m[x, y] = 255, 255, 255, 0
    n.convert('LA').save('hand' + num + '.png')
    # end = time()
    # time = str(end - start_time)
    # print('processing time: ' + time + ' seconds')

def distance():
    print('setting up...')
    sleep(4)
    print('ready')
    i = 0
    while i < 6001:
        GPIO.setmode(GPIO.BCM)
        TRIG = 23
        ECHO = 24
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        GPIO.output(TRIG, False)
        sleep(.1)
        GPIO.output(TRIG, True)
        sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO) == 0:
            pulse_start_time = time()
        while GPIO.input(ECHO) == 1:
            pulse_end_time = time()
        GPIO.cleanup()
        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        if distance < 50:
            print('object detected ' + str(distance) + ' centimeters away on run number: ' + str(i) + '')
            i = 60001
            sleep(2)
            cam.start_preview()
            hand()
        else:
            i += 1


def hand():
    global latest_file_number
    grey(str(latest_file_number))
    if pyml.check(str(latest_file_number)) is True:
        print('hand found')
        start()
    else:
        print('no hand found')
        sleep(2)
        distance()
    latest_file_number += 1


def start():
    global latest_file_number
    num = str(latest_file_number)
    cam.start_preview()
    updown()
    sleep(3)
    grey(num)
    played = pyml.evaluate(num)
    if played[0] == 'r':
        paper()
        print('I was ' + played[1] + '% sure they played ' + played[0] + '')
        # n = Image.open('images/grey-images/hand' + num + '.jpg')
        # n.save('images/ML-data/rock/hand' + num + '.png')
    elif played[0] == 'p':
        scissors()
        print('I was ' + played[1] + '% sure they played ' + played[0] + '')
        # n = Image.open('images/grey-images/hand' + num + '.jpg')
        # n.save('images/ML-data/paper/hand' + num + '.png')
    elif played[0] == 's':
        rock()
        print('I was ' + played[1] + '% sure they played ' + played[0] + '')
        # n = Image.open('images/grey-images/hand' + num + '.jpg')
        # n.save('images/ML-data/scissors/hand' + num + '.png')
    else:
        rand = random.randint(1,3)
        if rand == 1:
            rock()
        elif rand == 2:
            paper()
        else:
            scissors()
        print(played)
    latest_file_number += 1
    sleep(3)
    rock()
    distance()

print(latest_file_number)
cam = PiCamera()
cam.rotation = 180
cam.exposure_mode = 'sports'
cam.resolution = (300,200)
distance()
