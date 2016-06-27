import pygame, sys
pygame.init()
screen=pygame.display.set_mode((800,500))
herofireball=pygame.Surface((100,100))
brightblue=(0, 128, 255)
blue=(0, 0, 255)
black=(0, 0, 0)
pygame.draw.circle(herofireball, brightblue, (20, 20), 6)
pygame.draw.polygon(herofireball, brightblue, ((20, 14), (8, 17), (20, 20)))
pygame.draw.polygon(herofireball, brightblue, ((20, 17), (4, 20), (20, 23)))
pygame.draw.polygon(herofireball, brightblue, ((20, 20), (8, 23), (20, 26)))
pygame.draw.circle(herofireball, blue, (20, 20), 3)

screen.fill(black)

x = 10
y = 10

screen.blit(herofireball, (x, y))
pygame.display.flip()
pygame.time.wait(500)
