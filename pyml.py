from PIL import Image
import random

# this is the python file that will handle the machine learning


def check(num):  # checks if there is a hand present in the image or not
    # img = Image.open('images/grey-images/hand' + num + '.png')
    # run img through tensorflow to check if there is a hand in the picture
    # return True if there is a hand return False if there is not
    # for testing purposes it will return True
    return True


def evaluate(num):  # evaluates the position a players hand is in (ie rock, paper, scissors, or none)
    # img = Image.open('images/grey-images/hand' + num + '.png')
    # run img through tensorflow to check what position the hand is in
    # return 'r' if it's a rock, 'p' if it's paper, 's' if it is scissors, otherwise print the message, for example if
    # the threshold wasn't met, return 'unsure: 34% rock' or 'unable to process image: IOError'
    # ALL RETURN STATEMENTS THAT ARE NOT AN ERROR SHOULD BE A LIST IE: if they threw rock and the ML model was 63% sure
    # of it, return ['r', '63']
    # for testing purposes it will return rock with 63% confidence
    rand = random.randint(1,3)
    if rand == 1:
        return ['r', '63']
    elif rand == 2:
        return ['p', '63']
    else:
        return ['s', '63']
    
