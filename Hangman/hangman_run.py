import pygame as pg
from pygame.locals import *
import math

pg.init()

SCREEN_SIZE = (600,400)
STAGE_DELAY = 10
STROKE_DELAY = 5
STAGE = 0

STROKE_SIZE = 2
CHALK_COLOR = "whitesmoke"
BOARD_COLOR = (39,76,67)
DONE_DRAWING = False
SQRT_2 = math.sqrt(2)
X_OFFSET = 400
Y_OFFSET = 250

def drawStroke(x,y,color):
    pg.draw.circle(screen, color, (x,y), STROKE_SIZE)
    pg.time.delay(STROKE_DELAY)
    pg.display.update()

def chooseDrawStage(i, isErase):
    if isErase:
        color = BOARD_COLOR
    else:
        color = CHALK_COLOR
    drawStage(i, color)

def drawStage(stage, color):
    pg.time.delay(STAGE_DELAY)
    match stage:
        case 1: # pole
            for i in range(200):
                x = X_OFFSET
                y = Y_OFFSET - i
                drawStroke(x,y,color)
        case 2: # truss
            for i in range(57):
                x = X_OFFSET + i / SQRT_2
                y = Y_OFFSET + 90 - i / SQRT_2
                drawStroke(x,y,color)
        case 3: # beam
            for i in range(100):
                x = X_OFFSET + i
                y = Y_OFFSET + 50
                drawStroke(x,y,color)
        case 4: # rope
            for i in range(40):
                x = X_OFFSET + 125
                y = Y_OFFSET + 50 + i
                drawStroke(x,y,color)
        case 5: # head
            pg.time.delay(50)
            for i in range(-90,271):
                theta = i / 180 * math.pi
                x = X_OFFSET + 125 + 25 * math.cos(theta)
                y = Y_OFFSET - 135 + 25 * math.sin(theta)
                drawStroke(x,y,color)
        case 6: # trunk
            for i in range(60):
                x = X_OFFSET + 125
                y = Y_OFFSET - 110 + i
                drawStroke(x,y,color)
        case 7: # left arm
            for i in range(50):
                x = X_OFFSET + 125 - i / SQRT_2
                y = Y_OFFSET - 110 + i / SQRT_2
                drawStroke(x,y,color)
        case 8: # right arm
            for i in range(50):
                x = X_OFFSET + 125 + i / SQRT_2
                y = Y_OFFSET - 110 + i / SQRT_2
                drawStroke(x,y,color)
        case 9: # left leg
            for i in range(50):
                x = X_OFFSET + 125 - i / SQRT_2
                y = Y_OFFSET - 110 + i / SQRT_2
                drawStroke(x,y,color)
        case 10: # right leg
            for i in range(50):
                x = X_OFFSET + 125 + i / SQRT_2
                y = Y_OFFSET - 110 + i / SQRT_2
                drawStroke(x,y,color)

screen = pg.display.set_mode(SCREEN_SIZE)
screen.fill(BOARD_COLOR)


while True:
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    if not DONE_DRAWING:
        for i in range(1,11):
            chooseDrawStage(i, False)
        #DONE_DRAWING = True
        
        # for i in range(10,0,-1):
        #     chooseDrawStage(i, True)
        DONE_DRAWING = True
    else:
        pass