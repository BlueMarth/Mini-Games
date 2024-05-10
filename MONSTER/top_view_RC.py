import pygame as pg
from pygame.locals import *
import math
pg.init()

SIZE = (300, 300)
screen = pg.display.set_mode(SIZE)

clock = pg.time.Clock()
fps = 60

# define Car class
class Car(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super(Car, self).__init__()

        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = 0
        self.speed = 5

        self.surface = pg.Surface((width, height))
        self.surface.set_colorkey((127,127,127))
        self.rect = self.screen.get_rect(center=(x + width//2, y - height //2))

    def update(self):
        center = self.rect.center
        self.angle = self.angle + self.speed
        image = pg.transform.rotate(self.surface, self.angle)
        self.rect = image.get_rect()
        self.rect.center = center

        pg.draw.rect(self.screen, self.color, pg.Rect(self.x, self.y, self.width, self.height))
        screen.blit(image, self.rect)

    def turnRight(self):
        self.angle += self.speed
        
    def turnLeft(self):
        self.angle -= self.speed

car = Car(50, 50, 20, 5, 'red')

while True:
    
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            pg.quit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                car.turnRight()
            elif event.key == pg.K_LEFT:
                car.turnLeft()

    car.update()
    
    clock.tick(fps)
    pg.display.set_caption("fps: " + str(clock.get_fps()))