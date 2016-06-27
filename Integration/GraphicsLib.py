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

background_start = pygame.Surface((800, 600))
    
def render_text(word, x, y, font, color): #Function to render text. includes specific phrase, coordinates and color.
    my_font = pygame.font.SysFont('arial',60)
    label = my_font.render(word, 1, (color))
    background_start.blit(label, (x, y))
    label.set_colorkey(black)

def render_smaller_text(word, x, y, font, color): #Function to render smaller text.
    my_small_font = pygame.font.SysFont('arial', 36)
    new_label = my_small_font.render(word, 1, (color))
    new_label.set_colorkey(black)
    background_start.blit(new_label, (x, y))
    
def render_title_text(word, x, y, font, color): #Renders title text
    my_title_font = pygame.font.SysFont('arial', 80)
    title_label = my_title_font.render(word, 1, (color))
    background_start.blit(title_label, (x, y))
    title_label.set_colorkey(black)

background_start.fill(black) #Sets the background_start black to create a place to render text onto
# if rendertextvariable == True: #Referring back to that statement from earlier to print the text.
<<<<<<< HEAD
#
render_title_text("Wizard Rush", 210, 20, "arial", red)
render_text("Start Game", 260, 160, "arial", red)
render_smaller_text("Instructions", 200, 320, "arial", red)
#=======
render_title_text("Wizard Rush", 170, 20, "arial", red)
render_text("Start Game", 240, 160, "arial", red)
render_smaller_text("Instructions", 180, 320, "arial", red)
#>>>>>>> Stashed changes
=======
render_title_text("Wizard Rush", 210, 20, "arial", red)
render_text("Start Game", 260, 160, "arial", red)
render_smaller_text("Instructions", 200, 320, "arial", red)
>>>>>>> parent of 7793fee... misc
render_smaller_text("Credits", 480, 320, "arial", red)


background_game = pygame.image.load("ActionGameProject/Graphics/space.png")
background_game = background_game.convert()
background_game = pygame.transform.scale(background_game, (800, 600))


Credits = pygame.Surface ((800,600))
def render_creator_text(word, x, y, font, color): #Renders font the Creators text
    my_creator_font = pygame.font.SysFont('arial', 40, bold=True)
    creator_label = my_creator_font.render(word, 1, (color))
    Credits.blit(creator_label, (x, y))

def render_name_text(word, x, y, font, color): #Renders our names
    my_name_font = pygame.font.SysFont('arial', 40)
    name_label = my_name_font.render(word, 1, (color))
    Credits.blit(name_label, (x, y))

def render_catapult_text(word, x, y, font, color): #Renders Catapult text at bottom
    my_catapult_font = pygame.font.SysFont('arial', 20, bold=False, italic=True)
    catapult_label = my_catapult_font.render(word, 1, (color))
    Credits.blit(catapult_label, (x, y))

render_creator_text("Creators", 320, 20, "arial", red)
render_name_text("Andrew Blonsky", 275, 90, "arial", red)
render_name_text("Austin Rothschild", 265, 140, "arial", red)
render_name_text("Ryan Walulik", 295, 190, "arial", red)
render_name_text("Charles Villar", 290, 240, "arial", red)
render_catapult_text("Created at Operation Catapult 2016", 260, 440, "arial", red)


Pause = pygame.Surface((800,600))
def render_paused_text(word, x, y, font, color):
    my_paused_font = pygame.font.SysFont('arial', 80, bold=True)
    paused_label = my_paused_font.render(word, 1, (color))
    Pause.blit(paused_label, (x, y))

def render_resume_text(word, x, y, font, color):
    my_resume_font = pygame.font.SysFont('arial', 30)
    resume_label = my_resume_font.render(word, 1, (color))
    Pause.blit(resume_label, (x, y))

render_paused_text("Paused!", 260, 100, "arial", red) #Renders text with specific phrase, coordinates, font, size
render_resume_text("Press Escape to continue!", 220, 280, "arial", red)



Instructions = pygame.Surface((800,600))
def render_control_text(word, x, y, font, color):
    my_control_font = pygame.font.SysFont('arial', 40)
    control_label = my_control_font.render(word, 1, (color))
    Instructions.blit(control_label, (x, y))

def render_other_text(word, x, y, font, color):
    my_other_text = pygame.font.SysFont('arial', 20, bold=False, italic=True)
    other_label = my_other_text.render(word, 1, (color))
    Instructions.blit(other_label, (x, y))

#if somerendervariable == True:
render_control_text("Controls:", 340, 80, "arial", red)
render_control_text("Space bar - Shoot", 270, 160, "arial", red)
render_control_text("Arrow keys - Movement", 232, 220, "arial", red)
render_control_text("ESC - Pause / resume game", 200, 280, "arial", red)
render_other_text("Press ESC to go back.", 0, 0, "arial", red)


Fireball = pygame.Surface((20,20))
pygame.draw.circle(Fireball, brightblue, (20, 20), 6)
pygame.draw.polygon(Fireball, brightblue, ((20, 14), (8, 17), (20, 20)))
pygame.draw.polygon(Fireball, brightblue, ((20, 17), (4, 20), (20, 23)))
pygame.draw.polygon(Fireball, brightblue, ((20, 20), (8, 23), (20, 26)))
pygame.draw.circle(Fireball, blue, (20, 20), 3)
