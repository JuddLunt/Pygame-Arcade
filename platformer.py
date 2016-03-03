import pygame, os
from pygame.locals import *
from Arcade import arcade
from colours import *

def game(arcade):

    
    background = pygame.Surface((800,800))
    background.fill(grey,(0,0,800,800))
    arcade.initBackground(background)
    while True:
        arcade.getEvents()
        
        arcade.drawBackground(background)

    
if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    pygame.display.set_caption(os.path.basename(__file__).split('.')[0])
    game(arcade())

