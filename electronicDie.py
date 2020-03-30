from sense_hat import SenseHat
from time import sleep
import random
import dieFaces

sense = SenseHat()

def numToFace(dieNum):
    face = []
    if dieNum == 1:
        face = dieFaces.one
    if dieNum == 2:
        face = dieFaces.two
    if dieNum == 3:
        face = dieFaces.three
    if dieNum == 4:
        face = dieFaces.four
    if dieNum == 5:
        face = dieFaces.five
    if dieNum == 6:
        face = dieFaces.six
    return face


def rollDie():
    dieNum = 0
    while dieNum == 0:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 2 or y > 2 or z > 2:
            dieNum = random.randint(1, 6)
            sense.set_pixels(numToFace(dieNum))
            sleep(2)
            return dieNum
        else:
            sense.clear()