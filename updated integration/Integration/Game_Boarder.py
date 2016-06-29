import pygame, sys
BLUE = (0, 102, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 153, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Background:
     def __init__(self, x, y):
         self.x=x
         self.y=y
         self.img = pygame.image.load("ActionGameProject/Graphics/space.png")
         self.img = self.img.convert()
         self.img = pygame.transform.scale(self.img, (800, 600))


class Points:
    def __init__(self):
        self.x=500
        self.y=50
        self.font=pygame.font.SysFont('monospace', 50)

    def update(self, scoreNum):
        self.img = self.font.render('Points:'+str(scoreNum), True, WHITE)



if __name__ == "__main__":

    
    pygame.init()
    
    rendertextvariable = True

    screen = pygame.display.set_mode((800, 600))
    space = pygame.Surface((800, 100))

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
    pygame.time.wait(1000)

