import pygame

BLUE = (0, 102, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 153, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
# from NewStartScreen import *
# from PauseScreen import *
# from CreditScreen import * 

import pygame, sys
pygame.init()

black = (0, 0, 0)
yellow = (255, 255, 0) #List of different colors
red = (255, 0, 0)
green = (0, 255, 40)

background = pygame.Surface((800, 600))
    
def render_text(word, x, y, font, color): #Function to render text. includes specific phrase, coordinates and color.
    my_font = pygame.font.SysFont('arial',60)
    label = my_font.render(word, 1, (color))
    background.blit(label, (x, y))
    label.set_colorkey(black)

def render_smaller_text(word, x, y, font, color): #Function to render smaller text.
    my_small_font = pygame.font.SysFont('arial', 36)
    new_label = my_small_font.render(word, 1, (color))
    new_label.set_colorkey(black)
    background.blit(new_label, (x, y))
    
def render_title_text(word, x, y, font, color): #Renders title text
    my_title_font = pygame.font.SysFont('arial', 80)
    title_label = my_title_font.render(word, 1, (color))
    background.blit(title_label, (x, y))
    title_label.set_colorkey(black)

background.fill(black) #Sets the background black to create a place to render text onto
# if rendertextvariable == True: #Referring back to that statement from earlier to print the text.
render_title_text("Sample Title", 210, 20, "arial", red)
render_text("Start Game", 260, 160, "arial", red)
render_smaller_text("Instructions", 200, 320, "arial", red)
render_smaller_text("Credits", 480, 320, "arial", red)