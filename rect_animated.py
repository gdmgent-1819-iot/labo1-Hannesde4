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

def repeat():
    sleep(0.5)


while True:
    C = random_color()
    O = (0,0,0)
    s1 = [
        C, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]

    s2 = [
        C, C, O, O, O, O, O, O,
        C, C, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]

    s3 = [
        C, C, C, O, O, O, O, O,
        C, O, C, O, O, O, O, O,
        C, C, C, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]

    s4 = [
        C, C, C, C, O, O, O, O,
        C, O, O, C, O, O, O, O,
        C, O, O, C, O, O, O, O,
        C, C, C, C, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]


    s5= [
        C, C, C, C, C, O, O, O,
        C, O, O, O, C, O, O, O,
        C, O, O, O, C, O, O, O,
        C, O, O, O, C, O, O, O,
        C, C, C, C, C, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]

    s6= [
        C, C, C, C, C, C, O, O,
        C, O, O, O, O, C, O, O,
        C, O, O, O, O, C, O, O,
        C, O, O, O, O, C, O, O,
        C, O, O, O, O, C, O, O,
        C, C, C, C, C, C, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]

    s7= [
        C, C, C, C, C, C, C, O,
        C, O, O, O, O, O, C, O,
        C, O, O, O, O, O, C, O,
        C, O, O, O, O, O, C, O,
        C, O, O, O, O, O, C, O,
        C, O, O, O, O, O, C, O,
        C, C, C, C, C, C, C, O,
        O, O, O, O, O, O, O, O,
        ]

    s8= [
        C, C, C, C, C, C, C, C,
        C, O, O, O, O, O, O, C,
        C, O, O, O, O, O, O, C,
        C, O, O, O, O, O, O, C,
        C, O, O, O, O, O, O, C,
        C, O, O, O, O, O, O, C,
        C, O, O, O, O, O, O, C,
        C, C, C, C, C, C, C, C,
        ]
    sense.set_pixels(s1)
    repeat()
    sense.set_pixels(s2)
    repeat()
    sense.set_pixels(s3)
    repeat()
    sense.set_pixels(s4)
    repeat()
    sense.set_pixels(s5)
    repeat()
    sense.set_pixels(s6)
    repeat()
    sense.set_pixels(s7)
    repeat()
    sense.set_pixels(s8)
    repeat()
    sense.set_pixels(s7)
    repeat()
    sense.set_pixels(s6)
    repeat()
    sense.set_pixels(s5)
    repeat()
    sense.set_pixels(s4)
    repeat()
    sense.set_pixels(s3)
    repeat()
    sense.set_pixels(s2)
    repeat()
    sense.set_pixels(s1)
    repeat()
    sense.clear()
    repeat()
