import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)




class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.image = pygame.image.load("ActionGameProject/Graphics/enemy1.png")
        self.currentImage=0
        self.image = self.image.convert()
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (60,60))
        self.image = pygame.transform.flip(self.image, True, False)
pygame.display.flip()

