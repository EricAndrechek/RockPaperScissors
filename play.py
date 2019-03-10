import RPi.GPIO as GPIO
from time import sleep
from servo import tfe, sfe, tfi, sfi
# tfe brings first two finger from 0 to 180
# sfe brings second two fingers from 0 to 180
# tfi brings first two fingers from 180 to 0
# sfi brings second two fingers from 180 to 0


def updown():
    # servo motor controls to move the hand up and down and say rock paper scissor shoot
    pass
    
    
def rock():
    # play the rock with servo motors
    tfi()
    sfi()

    
def paper():
    # play the paper with servo motors
    tfe()
    sfe()

    
def scissors():
    # play the scissors with servo motors
    tfe()

