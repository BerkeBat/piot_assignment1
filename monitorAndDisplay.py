from sense_hat import SenseHat
from time import sleep
import json
sense = SenseHat()

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
c = (0, 0, 0)

cfg =  'config.json'
with open('config.json') as json_file:
    cfg_dict = json.load(json_file)

c_max = cfg_dict['cold_max']
cm_min = cfg_dict['comfortable_min']
cm_max = cfg_dict['comfortable_max']
h_min = cfg_dict['hot_min']

while True:
    t = sense.get_temperature()
    if t < c_max:
        c = b
    elif t > cm_min and t < cm_max:
        c = g
    elif t > h_min:
        c = r
    sense.clear(c)
    sleep(10)


