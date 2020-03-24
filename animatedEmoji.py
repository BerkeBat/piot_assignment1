from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

y = (255, 255, 0)
b = (0, 0, 0)
g = (0, 255, 0)
w = (255, 255, 255)
bl = (0, 0, 255)
br = (170, 80, 50)
sense.clear()

smiley_pixels= [
    y, y, y, y, y, y, y, y,
    y, y, y, y, y, y, y, y,
    y, w, w, y, y, w, w, y,
    y, w, b, y, y, b, w, y,
    y, y, y, y, y, y, y, y,
    y, b, y, y, y, y, b, y,
    y, y, b, b, b, b, y, y,
    y, y, y, y, y, y, y, y
]
sad_pixels= [
    y, y, y, y, y, y, y, y,
    y, y, y, y, y, y, y, y,
    y, w, w, y, y, w, w, y,
    y, w, b, y, y, b, w, y,
    y, bl, y, y, y, y, y, y,
    y, y, b, b, b, b, y, y,
    y, b, y, y, y, y, b, y,
    y, y, y, y, y, y, y, y
]
tree_pixels= [
    b, b, b, b, b, b, b, b,
    b, b, g, g, g, g, b, b,
    b, g, g, g, g, g, g, b,
    b, g, g, g, g, g, g, b,
    b, b, g, g, g, g, b, b,
    b, b, b, br, br, b, b, b,
    b, b, b, br, br, b, b, b,
    b, b, b, br, br, b, b, b,
]

sense.set_pixels(smiley_pixels)
sleep(3)
sense.set_pixels(sad_pixels)
sleep(3)
sense.set_pixels(tree_pixels)
sleep(3)
sense.clear() 

