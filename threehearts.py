import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
heart=pygame.Surface((300,100))
red = (255, 0, 0)
black = (0, 0, 0)
pygame.draw.circle(heart, red, (10, 10), 10)
pygame.draw.circle(heart, red, (30, 10), 10)
pygame.draw.polygon(heart, red, ((0, 10), (40, 10), (20, 30)))
pygame.draw.circle(heart, red, (60, 10), 10)
pygame.draw.circle(heart, red, (80, 10), 10)
pygame.draw.polygon(heart, red, ((50, 10), (90, 10), (70, 30)))
pygame.draw.circle(heart, red, (110, 10), 10)
pygame.draw.circle(heart, red, (130, 10), 10)
pygame.draw.polygon(heart, red, ((100, 10), (140, 10), (120, 30)))

xcoordinate = 10
ycoordinate = 10
velox = 0
veloy = 0

while True:
    eventLs = pygame.event.get()
    for event in eventLs:
        if event.type == pygame.QUIT:
            exit()

    screen.fill(black)

    xcoordinate += velox
    ycoordinate += veloy
    screen.blit(heart, (xcoordinate, ycoordinate))
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
