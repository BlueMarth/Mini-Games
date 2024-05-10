import pygame as pg
from pygame.locals import *
import math

SIZE = (960, 600)
screen = pg.display.set_mode(SIZE)

clock = pg.time.Clock()
fps = 60

""" define physical constants """
# fluid_density, speed, drag_coeff, cross_area, angle_radian
GRAVITY = 0.5 # veritcal acceleration due to gravity
ROAD_LEVEL = 500 # y = 100

""" define static parameters (don't change with time) """
CHASSIS_MASS = 100 # units
CHASSIS_SIZE = (20, 6) # pixels
WHEEL_RADIUS = 3
DIM_A = 7
DIM_B = 3
WHEELBASE = 14

WEIGHT = CHASSIS_MASS * GRAVITY # weight acts veritically down





""" define dynamic parameters (change with time) """
# tilt angle in degrees
phi_deg = - math.atan2(DIM_B, DIM_A)
# tilt angle in radians
phi_rad = math.radians(phi_deg)
# initiate left wheel position
left_wheel_pos = [50, (ROAD_LEVEL - WHEEL_RADIUS) - 2 ]
# right wheel always on the same line that is parallel to the length of the chassis
right_wheel_pos = [left_wheel_pos + math.cos(phi_rad), left_wheel_pos[1] - math.sin(phi_rad)]
# centre of gravity of the car relative to the center of left wheel
cg = [left_wheel_pos[0] + DIM_A, left_wheel_pos[1] - DIM_B]
# just an approximation, only affects graphics not physics
chassis_center = cg


""" set up initial conditions """


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

""" Physics & math """
def updateForces():
    T_drive = 0
    F_drive = T_drive / WHEEL_RADIUS
    pass





""" Render """
def drawFrame(x, y):
    # draw background
    
    # draw terrain

    # draw car (chassis & wheels)
    
    
    pg.display.update()

while True:
    
    """ user inputs """

    """ update forces """

    """ compute movements """

    """ render graphics """
    drawFrame()
    
    clock.tick(fps)
    pg.display.set_caption("fps: " + str(clock.get_fps()))