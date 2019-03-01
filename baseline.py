from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.rotation = 90
from random import randint

def random_color():
    r = randint(128,255)
    g = randint(128,255)
    b = randint(128,255)
    return(r, g, b)

def random_background_color():
    r = randint(0,128)
    g = randint(0,128)
    b = randint(0,128)
    return(r, g, b)
    
while 1:
    sense.show_message("Hello! We are New Media Development :)",0.1, text_colour=random_color(), back_colour=random_background_color())
    sense.clear()
