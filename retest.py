import pygame, os, sys
from pygame.locals import *
from Arcade import arcade
from colours import *

def Game(arcade):

    arcade.setCaption(__file__)

    wall_x, wall_y = 50, 50
    wall = arcade.makeSurface(800, 60)
    wall.fill(black,(0,0,800,60))

    background = pygame.Surface((800,800))
    background.fill(grey,(0,0,800,800))
    arcade.initBackground(background)

    alive = True
    
    while alive:
        arcade.getEvents()

        pressed = arcade.getKey()
        if pressed[K_a] or pressed[K_LEFT]:
            if wall_x > 0:
                wall_x -= 5
        if pressed[K_d] or pressed[K_RIGHT]:
            if wall_x < 500:
                wall_x += 5
        if pressed[K_ESCAPE]:
            pygame.quit()
            sys.exit()

        arcade.drawBackground(background)
        arcade.draw((wall, wall_x, wall_y))

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    Game(arcade())
