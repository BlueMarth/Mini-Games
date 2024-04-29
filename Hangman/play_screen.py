import pygame as pg
from pygame.locals import *
import math
import random

pg.init()

SCREEN_SIZE = (600,400)
STAGE_DELAY = 1

CHALK_COLOR = "antiquewhite3"
BOARD_COLOR = (39,76,67)
DONE_DRAWING = False
SQRT_2 = math.sqrt(2)
X_OFFSET = 400
Y_OFFSET = 250

def drawStroke(x,y,color):
    stroke_size = random.randrange(2, 5) # introduce imperfection to the drawing lines
    stroke_delay = random.randrange(2, 9)
    error = (random.random()-0.5)*2
    x += error
    y += error
    pg.draw.circle(screen, color, (x,y), stroke_size) # draw tiny circles one at a time
    pg.time.delay(stroke_delay)
    pg.display.update()

def chooseDrawStage(i, isErase):
    if isErase:
        color = BOARD_COLOR # eraser mode
    else:
        color = CHALK_COLOR # chalk mode
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
                y = Y_OFFSET - 160 - i / SQRT_2
                drawStroke(x,y,color)
        case 3: # beam
            for i in range(100):
                x = X_OFFSET + i
                y = Y_OFFSET - 200
                drawStroke(x,y,color)
        case 4: # rope
            for i in range(40):
                x = X_OFFSET + 100
                y = Y_OFFSET - 200 + i
                drawStroke(x,y,color)
        case 5: # head
            pg.time.delay(50)
            for i in range(-90,271, 2):
                theta = i / 180 * math.pi
                x = X_OFFSET + 100 + 25 * math.cos(theta)
                y = Y_OFFSET - 135 + 25 * math.sin(theta)
                drawStroke(x,y,color)
        case 6: # trunk
            for i in range(60):
                x = X_OFFSET + 100
                y = Y_OFFSET - 110 + i
                drawStroke(x,y,color)
        case 7: # left arm
            for i in range(50):
                x = X_OFFSET + 100 - i / SQRT_2
                y = Y_OFFSET - 110 + i / SQRT_2
                drawStroke(x,y,color)
        case 8: # right arm
            for i in range(50):
                x = X_OFFSET + 100 + i / SQRT_2
                y = Y_OFFSET - 110 + i / SQRT_2
                drawStroke(x,y,color)
        case 9: # left leg
            for i in range(50):
                x = X_OFFSET + 100 - i / SQRT_2
                y = Y_OFFSET - 50 + i / SQRT_2
                drawStroke(x,y,color)
        case 10: # right leg
            for i in range(50):
                x = X_OFFSET + 100 + i / SQRT_2
                y = Y_OFFSET - 50 + i / SQRT_2
                drawStroke(x,y,color)

screen = pg.display.set_mode(SCREEN_SIZE)
screen.fill(BOARD_COLOR)

stage = 0

while True:
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        
        if stage < 0:
            stage = 0
        else:
            if event.type == KEYDOWN:
                if event.key == pg.K_UP:
                    stage += 1
                    chooseDrawStage(stage, False)
                elif event.key == pg.K_DOWN:
                    chooseDrawStage(stage, True)
                    stage -= 1