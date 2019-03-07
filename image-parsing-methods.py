import numpy as np
from PIL import Image

# removes green from color, turns to greyscale
im = Image.open('example-files/step1.jpg')
im = im.convert('RGBA')
data = np.array(im)
rgb = data[:, :, :3]
color = [0, 254, 4]   # This is the color I want to remove
black = [0, 0, 0, 255, 255]
white = [255, 255, 255, 0]
mask = np.all(rgb == color, axis=-1)
# the following line turns all that match to the color green
data[mask] = white
# the following line turns all that don't match into black
# data[np.logical_not(mask)] = black
new_im = Image.fromarray(data)
new_im.save('example-files/step2.png')

img = Image.open('example-files/step2.png').convert('LA')
img.save('example-files/step3.png')

# converts to greyscale, converts to color, removes specific shade of grey, converts to greyscale

img2 = Image.open('example-files/step1.jpg').convert('L')
img2.save('example-files/step4.png')

im2 = Image.open('example-files/step4.png')
im2 = im2.convert('RGB')
im2.save('example-files/step5.png')

im = Image.open('example-files/step5.png')
im = im.convert('RGBA')
data = np.array(im)
rgb = data[:, :, :3]
color = [149, 149, 149]   # This is the color I want to remove
black = [0, 0, 0, 255, 255]
white = [255, 255, 255, 0]
mask = np.all(rgb == color, axis=-1)
# the following line turns all that match to the color green
data[mask] = white
new_im = Image.fromarray(data)
new_im = new_im.convert('LA')
new_im.save('example-files/step6.png')

# removes all pixels within specific color range
n = Image.open('example-files/step1.jpg')
n = n.convert('RGBA')
m = n.load()
s = n.size
for x in xrange(s[0]):
    for y in xrange(s[1]):
        r, g, b, a = m[x, y]
        if g > 200 and r < 100 and b < 100:
            m[x, y] = 255, 255, 255, 0

n.save('example-files/step7.png')
img = Image.open('example-files/step7.png').convert('LA')
img.save('example-files/step8.png')