from PIL import Image
# this is the python file for controlling the servo motors to make a hand movement

def updown():
    # servo motor controls to move the hand up and down and say rock paper scissor shoot
def rock(num):
    # play the rock with servo motors
    n = Image.open('images/grey-images/hand{}.jpg').format(num)
    n.save('images/ML-data/scissors/hand{}.png').format(num)
def paper(num):
    # play the paper with servo motors
    n = Image.open('images/grey-images/hand{}.jpg').format(num)
    n.save('images/ML-data/rock/hand{}.png').format(num)
def scissors(num):
    # play the scissors with servo motors
    n = Image.open('images/grey-images/hand{}.jpg').format(num)
    n.save('images/ML-data/paper/hand{}.png').format(num)
