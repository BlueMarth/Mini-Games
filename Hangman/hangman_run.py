import pygame as pg
from pygame.locals import *
import math

pg.init()

SCREEN_SIZE = (600,400)


CHALK_SIZE = 4
CHALK_COLOR = "whitesmoke"
BOARD_COLOR = (39,76,67)
DONE_DRAWING = False

def drawStage(stage):
    match stage:
        case 1:
            pg.time.delay(500)
            for i in range(200):
                x = 425
                y = 250 - i
                pg.draw.circle(screen, CHALK_COLOR, (x, y), CHALK_SIZE)
                pg.time.delay(5)
                pg.display.update()
        case 2:
            pg.time.delay(500)
            for i in range(57):
                x = 425 + i / math.sqrt(2)
                y = 90 - i / math.sqrt(2)
                pg.draw.circle(screen, CHALK_COLOR, (x, y), CHALK_SIZE)
                pg.time.delay(5)
                pg.display.update()
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            pass

screen = pg.display.set_mode(SCREEN_SIZE)
screen.fill(BOARD_COLOR)


while True:
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    if not DONE_DRAWING:
        drawStage(1)
        drawStage(2)
        DONE_DRAWING = True
    else:
        pass