import pygame, sys
pygame.init()
screen = pygame.display.set_mode((800,500))

newrendervariable = True #Same concept as title screen.

black = (0, 0, 0)
red = (255, 0, 0)

screen.fill(black)

def render_creator_text(word, x, y, font, color): #Renders font the Creators text
    my_creator_font = pygame.font.SysFont('arial', 40, bold=True)
    creator_label = my_creator_font.render(word, 1, (color))
    screen.blit(creator_label, (x, y))

def render_name_text(word, x, y, font, color): #Renders our names
    my_name_font = pygame.font.SysFont('arial', 40)
    name_label = my_name_font.render(word, 1, (color))
    screen.blit(name_label, (x, y))

def render_catapult_text(word, x, y, font, color): #Renders Catapult text at bottom
    my_catapult_font = pygame.font.SysFont('arial', 20, bold=False, italic=True)
    catapult_label = my_catapult_font.render(word, 1, (color))
    screen.blit(catapult_label, (x, y))

if newrendervariable == True:
    render_creator_text("Creators", 320, 20, "arial", red)
    render_name_text("Andrew Blonsky", 275, 90, "arial", red)
    render_name_text("Austin Rothschild", 265, 140, "arial", red)
    render_name_text("Ryan Walulik", 295, 190, "arial", red)
    render_name_text("Charles Villar", 290, 240, "arial", red)
    render_catapult_text("Created at Operation Catapult 2016", 260, 440, "arial", red)
    render_catapult_text("Press ESC to go back.", 0, 0, "arial", red)
    

pygame.display.flip()
