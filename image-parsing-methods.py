from __future__ import print_function
import numpy as np
from PIL import Image, ImageFilter
import PIL.ImageOps
import time
import colorama
from colorama import Fore, Style


colorama.init(autoreset=True)


def print2(msg, elapsed_time):
    elapsed_time_string = str(elapsed_time)
    if elapsed_time < 0.1:
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + msg + ": " + Fore.GREEN + elapsed_time_string + " seconds\n")
    elif elapsed_time < 0.15:
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + msg + ": " + Fore.YELLOW + elapsed_time_string + " seconds\n")
    else:
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + msg + ": " + Fore.RED + elapsed_time_string + " seconds\n")


def specific_color():
    # removes green from color, turns to greyscale
    # very impractical, have to define one color
    start = time.time()
    im = Image.open('example-files/step1.jpg')
    im = im.convert('RGB')
    data = np.array(im)
    rgb = data[:, :, :3]
    color = [0, 254, 4]   # This is the color I want to remove
    white = [255, 255, 255]
    mask = np.all(rgb == color, axis=-1)
    # the following line turns all that match to the color green
    data[mask] = white
    # the following line turns all that don't match into black
    # black = [0, 0, 0, 255]
    # data[np.logical_not(mask)] = black
    Image.fromarray(data).convert('L').save('example-files/step2.png')
    end = time.time()
    print2("remove green first", end - start)


def greyscale_color_back():
    # converts to greyscale, converts to color, removes specific shade of grey, converts to greyscale
    color = [149, 149, 149]   # This is the color I want to remove
    white = [255, 255, 255]
    start = time.time()
    im2 = Image.open('example-files/step1.jpg').convert('L')
    im = im2.convert('RGB')
    data = np.array(im)
    rgb = data[:, :, :3]
    mask = np.all(rgb == color, axis=-1)
    # the following line turns all that match to the color green
    data[mask] = white
    Image.fromarray(data).convert('L').save('example-files/step3.png')
    end = time.time()
    print2("greyscale first", end - start)


def individual_pixels():
    # removes all pixels within specific color range
    # most effective, but slowest by far
    start = time.time()
    n = Image.open('example-files/step1.jpg')
    n = n.convert('RGB')
    s = n.size
    m = n.load()
    for x in xrange(s[0]):
        for y in xrange(s[1]):
            r, g, b = m[x, y]
            if g > 200 and r < 150 and b < 150:
                m[x, y] = 255, 255, 255
            elif g > 125 and r < 75 and b < 75:
                m[x, y] = 255, 255, 255
            elif g > 100 and r < 10 and b < 50:
                m[x, y] = 255, 255, 255
            elif g > 100 and r < 50 and b < 10:
                m[x, y] = 255, 255, 255
    n.convert('L').save('example-files/step4.png')
    end = time.time()
    print2("removes pixel by pixel", end - start)


def edges():
    # find the edges
    # simple, effective, fast, need to see how well with ML
    start = time.time()
    Image.open('example-files/step1.jpg').filter(ImageFilter.FIND_EDGES).convert('L').save('example-files/step5.png')
    end = time.time()
    print2("find edges", end - start)


def all_grey():
    # converts to greyscale, removes specific shade of grey
    # potential to be the best option, just can't get it to work
    start = time.time()
    im = Image.open('example-files/step1.jpg').convert('L')
    data = np.array(im)
    mask = np.all(data == [149], axis=-1)
    data[mask] = [255]
    new_im = Image.fromarray(data)
    new_im.save('example-files/step6.png')
    end = time.time()
    print2("greyscale only", end - start)


def slow_perfection():
    # slowest by a long shot, but combines perfect removal in the pixel by pixel method, with the edge finding in the
    # edge method to get you a clear and bold and definite edge finder
    start = time.time()
    n = Image.open('example-files/step1.jpg')
    n = n.convert('RGB')
    s = n.size
    m = n.load()
    for x in xrange(s[0]):
        for y in xrange(s[1]):
            r, g, b = m[x, y]
            if g > 200 and r < 150 and b < 150:
                m[x, y] = 255, 255, 255
            elif g > 125 and r < 75 and b < 75:
                m[x, y] = 255, 255, 255
            elif g > 100 and r < 10 and b < 50:
                m[x, y] = 255, 255, 255
            elif g > 100 and r < 50 and b < 10:
                m[x, y] = 255, 255, 255
    n.filter(ImageFilter.FIND_EDGES).convert('L').save('example-files/step7.png')
    end = time.time()
    print2("edge perfection", end - start)


print(Style.DIM + "beginning image filtering...\n")
edges()
all_grey()
greyscale_color_back()
individual_pixels()
slow_perfection()
specific_color()
print(Style.DIM + "image filtering complete")
