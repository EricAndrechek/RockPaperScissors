from picamera import PiCamera
from time import sleep, time
import numpy as np
from PIL import Image, ImageFilter
import PIL.ImageOps


def main(num):
    camera.capture('hand' + num + '.jpg')
    camera.stop_preview()
    start = time()
    n = Image.open('hand' + num + '.jpg')
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
    end = time()
    time = str(end - start)
    print('processing time: ' + time + ' seconds')
