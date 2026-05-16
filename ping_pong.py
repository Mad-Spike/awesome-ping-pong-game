import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from pygame import *
from random import randint

#set up basic game window thingymabob
display.set_caption("greatest pingpong game known to man kind")
window = display.set_mode((700, 599))
clock = time.Clock() 
FPS = 60

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    #Fill window background color (Dark Blue vibe color)
    window.fill((20, 30, 50))

    #Update frame rendering structure
    display.update()
    clock.tick(FPS)