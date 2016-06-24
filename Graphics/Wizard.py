import pygame
import random

BLACK = (0, 0 , 0)
WHITE = (255, 255, 255)


#class for wizard
class Wizard1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0
        # import image
        self.image = pygame.image.load("ActionGameProject/Graphics/wizard.png")
        self.currentImage=0
        self.image = self.image.convert()
        self.image.set_colorkey(WHITE)
        #change the size of the wizard
        self.image = pygame.transform.scale(self.image, (60, 60))



