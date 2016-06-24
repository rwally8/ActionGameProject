import pygame, sys
from Background import *
pygame.init()


rendertextvariable = True

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 40)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((800, 600))
space = pygame.Surface((800, 100))

class Points:
    def __init__(self, x, y, font, size, color):
        self.x=x
        self.y=y
        self.size=size
        self.font=pygame.font.SysFont('monospace', 50)
        self.image = pygame.image.load("ActionGameProject/Graphics/space.png")


x=0
y=0
image = pygame.image.load("ActionGameProject/Graphics/space.png")
screen.blit(image, (x, y))



space = pygame.image.load("ActionGameProject/Graphics/space.png")    
font = pygame.font.SysFont('Sans', 50)
text = font.render('Points:', True, WHITE)
screen.blit(text, (500, 50))


surf = pygame.Surface((800, 7))
surf.fill(WHITE)
screen.blit(surf, (0, 110))

pygame.display.flip()

def eventLoop():
    while True:
        eventList=pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                exit()
eventLoop()
