from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.rotation = 90
from random import randint

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return(r, g, b)
 
pos = range(0,8)

def my_Function():
    for x in pos:
        for y in pos:
            sense.clear()
            sense.set_pixel(y, x, random_color())
            sleep(0.1)
    my_Function()
my_Function()
