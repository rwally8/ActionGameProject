import pygame, sys
pygame.init()
screen=pygame.display.set_mode((800,500))
enemyfireball=pygame.Surface((100,100))
red=(255, 0, 0)
orange=(255, 128, 0)
black=(0, 0, 0)
pygame.draw.circle(enemyfireball, orange, (20, 20), 6)
pygame.draw.polygon(enemyfireball, orange, ((20, 14), (32, 17), (20, 20)))
pygame.draw.polygon(enemyfireball, orange, ((20, 17), (36, 20), (20, 23)))
pygame.draw.polygon(enemyfireball, orange, ((20, 20), (32, 23), (20, 26)))
pygame.draw.circle(enemyfireball, red, (20, 20), 3)

screen.fill(black)

x = 10
y = 10

screen.blit(enemyfireball, (x, y))
pygame.display.flip()
pygame.time.wait(500)
