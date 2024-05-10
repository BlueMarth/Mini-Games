import pygame as pg
from pygame.locals import *
import math

SIZE = (960, 600)
screen = pg.display.set_mode(SIZE)

clock = pg.time.Clock()
fps = 60

""" define physical constants """
# fluid_density, speed, drag_coeff, cross_area, angle_radian
GRAVITY = 0.6 # veritcal acceleration due to gravity


""" define static parameters (don't change with time) """
CHASSIS_MASS = 100 # units
CHASSIS_SIZE = (20, 6) # pixels
WHEEL_MASS = 10
WHEEL_RADIUS = 3
DIM_A = 
GROUND_CLEARANCE = 15

ROAD_LEVEL = 500 # y = 100
F_WEIGHT = CAR_MASS * GRAVITY # weight acts veritically down





""" define dynamic parameters (change with time) """
pos_x, pos_y = 0, 0
vel_x, vel_y = 0, 0
acc_x, acc_y = 0, 0

""" set up initial conditions """
pos_x = SIZE[0]//2 - 350
pos_y = ROAD_LEVEL - CAR_SIZE[1]

""" simulation settings """


""" User Interaction """

def getInputs():
    for event in pg.event.get():
        if (event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            exit()

    

""" Game Logic """

def initiate_Car():
    pass

def drive_Car():
    pass

""" Physics Engine """
def updateForces():
    pass

def integrator():
    pass


""" Render """
def renderGraphics(x, y):
    screen.fill('black')
    pg.draw.line(screen, 'red', [0, ROAD_LEVEL], [SIZE[0], ROAD_LEVEL], 1)
    
    # car
    pg.draw.rect(screen, "green", [x, y, CAR_SIZE[0], CAR_SIZE[1]])
    # wheels
    pg.draw.circle(screen, "yellow", (x + ))
    
    pg.display.update()

while True:
    
    getInputs()
    renderGraphics()
    
    clock.tick(fps)
    pg.display.set_caption("fps: " + str(clock.get_fps()))