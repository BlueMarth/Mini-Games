import pygame as pg
from pygame.locals import *
import math

pg.init()

SCREEN_SIZE = (600,400)
STAGE_DELAY = 2
STROKE_DELAY = 1

CHALK_SIZE = 4
CHALK_COLOR = "whitesmoke"
BOARD_COLOR = (39,76,67)
DONE_DRAWING = False
SQRT_2 = math.sqrt(2)

def chalkStroke(x,y):
    pg.draw.circle(screen, CHALK_COLOR, (x,y), CHALK_SIZE)
    pg.time.delay(STROKE_DELAY)
    pg.display.update()

def drawStage(stage):
    pg.time.delay(STAGE_DELAY)
    match stage:
        case 1: # vertical pole
            for i in range(200):
                x = 425
                y = 250 - i
                chalkStroke(x,y)
        case 2: # truss
            for i in range(57):
                x = 425 + i / SQRT_2
                y = 90 - i / SQRT_2
                chalkStroke(x,y)
        case 3: # horizontal beam
            for i in range(100):
                x = 425 + i
                y = 50
                chalkStroke(x,y)
        case 4: # rope
            for i in range(40):
                x = 525
                y = 50 + i
                chalkStroke(x,y)
        case 5: # head
            pg.time.delay(50)
            for i in range(90,-271,-1):
                theta = i / 180 * math.pi
                x = 25 * math.cos(theta) + 525
                y = 115 - 25 * math.sin(theta)
                chalkStroke(x,y)
        case 6: # trunk
            for i in range(75):
                x = 525
                y = 115 + i
                chalkStroke(x,y)
        case 7: # left arm
            for i in range(71):
                x = 525 - i / SQRT_2
                y = 120 + i / SQRT_2
                chalkStroke(x,y)
        case 8: # right arm
            for i in range(71):
                x = 525 + i / SQRT_2
                y = 120 + i / SQRT_2
                chalkStroke(x,y)
        case 9: # left leg
            for i in range(71):
                x = 525 - i / SQRT_2
                y = 190 + i / SQRT_2
                chalkStroke(x,y)
        case 10: # right leg
            for i in range(71):
                x = 525 + i / SQRT_2
                y = 190 + i / SQRT_2
                chalkStroke(x,y)

screen = pg.display.set_mode(SCREEN_SIZE)
screen.fill(BOARD_COLOR)


while True:
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    if not DONE_DRAWING:
        for i in range(1,11):
            drawStage(i)
        DONE_DRAWING = True
    else:
        pass