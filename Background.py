import pygame



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
         self.img = pygame.transform.scale(self.img, (800, 500))


              
              
              
              


     
       


