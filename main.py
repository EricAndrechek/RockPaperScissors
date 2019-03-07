from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import glob
import os
import imaging
import pyml
import play


list_of_files = glob.glob('images/raw-images/*')
latest_file = max(list_of_files, key=os.path.getctime)
latest_file_number = latest_file[22:][:-4] + 1


def distance():
    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distancemm = round(pulse_duration * 17150, 2)
    distancecm = distancemm / 10
    if distancecm < 15:
        print('object detected {} centimeters away').format(distancecm)
        hand()
    else:
        distance()


def hand():
    global latest_file_number
    camera.capture('images/raw-images/hand{}.jpg').format(latest_file_number)
    imaging.greyscale(latest_file_number)
    if pyml.check(latest_file_number) is True:
        print('hand found')
        start()
    else:
        print('no hand found')
        sleep(5)
        distance()
    latest_file_number += 1


def start():
    global latest_file_number
    num = latest_file_number
    play.updown()
    camera.capture('images/raw-images/hand{}.jpg').format(num)
    imaging.greyscale(num)
    played = pyml.evaluate(num)
    if played[0] == 'r':
        play.paper(num)
    elif played[0] == 'p':
        play.scissors(num)
    elif played[0] == 's':
        play.rock(num)
    else:
        print(played)
    print('I was {}% sure they played {}').format(played[1], played[0])
    latest_file_number += 1
    sleep(5)
    distance()


camera = PiCamera()
camera.start_preview()
distance()
