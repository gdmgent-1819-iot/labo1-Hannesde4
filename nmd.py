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
    
while 1:
    sense.show_letter("N", random_color())
    sleep(1)
    sense.show_letter("M", random_color())
    sleep(1)
    sense.show_letter("D", random_color())
    sleep(1)
    sense.clear()
    sleep(2)
