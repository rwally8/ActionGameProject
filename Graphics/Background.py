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
         self.image = pygame.image.load("ActionGameProject/Graphics/space.png")
         self.image = self.image.convert()
         self.image = pygame.transform.scale(self.image, (800, 500))


              
              
              
              


     
       


