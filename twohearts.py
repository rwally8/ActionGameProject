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

x = 10
y = 10
vx = 0
vy = 0

while True:
    eventLs = pygame.event.get()
    for event in eventLs:
        if event.type == pygame.QUIT:
            exit()

    screen.fill(black)

    x += vx
    y += vy
    screen.blit(heart, (x, y))
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
