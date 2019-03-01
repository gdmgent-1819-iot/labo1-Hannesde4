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

def pos():
    return(randint(0,7))

while 1:
    color = random_color()
    for x in range(0, 32):
        sense.set_pixel(pos(), pos(), color)
    sleep(5)
    sense.clear()
