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
        self.img = pygame.image.load("ActionGameProject/Graphics/wizard.png")
        self.currentImage=0
        self.img = self.img.convert()
        self.img.set_colorkey(WHITE)
        #change the size of the wizard
        self.img = pygame.transform.scale(self.img, (60, 60))
    def update(self):
        # TODO: what else hero is going to do in each frame
        self.x += self.vx
        self.y += self.vy



