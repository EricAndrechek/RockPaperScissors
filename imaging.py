from PIL import Image


def greyscale(num):
    n = Image.open('images/raw-images/hand{}.jpg').format(num)
    n = n.convert('RGBA')
    m = n.load()
    s = n.size
    for x in xrange(s[0]):
        for y in xrange(s[1]):
            r, g, b, a = m[x, y]
            if g > 200 and r < 100 and b < 100:
                m[x, y] = 255, 255, 255, 0
    n.convert('LA')
    n.save('images/grey-images/hand{}.png').format(num)
