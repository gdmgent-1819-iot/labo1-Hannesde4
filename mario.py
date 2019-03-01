from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.rotation = 90
    
X = (255,0,0)
O = (255,255,255)
B = (0,0,255)
R = (255,0,0)
G = (255,175,125)
F = (170,75,0)
P = (108,25,25)
E = (0,0,0)
D = (205,155,75)

mario = [
    O, O, R, R, R, R, O, O,
    O, O, R, R, R, O, R, O,
    O, O, G, B, G, B, O, O,
    O, O, G, G, F, F, O, O,
    G, R, B, R, R, B, R, G,
    O, O, B, B, B, B, O, O,
    O, O, B, B, B, B, O, O,
    O, O, F, O, O, F, O, O,
]

mario_jump = [
    O, O, R, R, R, O, R, O,
    O, O, G, B, G, B, O, O,
    O, O, G, G, F, F, O, O,
    G, R, B, R, R, B, R, G,
    O, O, B, B, B, B, O, O,
    O, O, B, B, B, B, O, O,
    O, O, F, O, O, F, O, O,
    O, O, O, O, O, O, O, O,
]

paddestoel = [
    O, O, R, R, R, R, O, O,
    O, R, R, O, O, R, R, O,
    O, O, R, O, O, R, O, O,
    O, O, D, E, D, E, O, O,
    O, O, D, D, P, D, O, O,
    O, D, B, D, D, B, D, O,
    O, O, B, O, O, B, O, O,
    O, O, F, O, O, F, O, O,
]


sense.set_pixels(mario)
while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                sense.set_pixels(mario_jump)

        sleep(0.5)
        sense.set_pixels(mario)
