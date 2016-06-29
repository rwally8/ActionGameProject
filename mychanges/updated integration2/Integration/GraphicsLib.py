import pygame

BLUE = (0, 102, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 153, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

import pygame, sys
pygame.init()

black = (0, 0, 0)
yellow = (255, 255, 0) #List of different colors
red = (255, 0, 0)
green = (0, 255, 40)

background_start = pygame.image.load("ActionGameProject/Graphics/start_back.png")
background_start = pygame.transform.scale(background_start, (800, 600))
background_start = background_start.convert()

fireball = pygame.mixer.Sound("ActionGameProject/fireball.wav")
def render_text(word, x, y, font, color): #Function to render text. includes specific phrase, coordinates and color.
    my_font = pygame.font.SysFont('comicsansms',60)
    label = my_font.render(word, 1, (color))
    background_start.blit(label, (x, y))
    label.set_colorkey(black)

def render_smaller_text(word, x, y, font, color): #Function to render smaller text.
    my_small_font = pygame.font.SysFont('comicsansms', 36)
    new_label = my_small_font.render(word, 1, (color))
    new_label.set_colorkey(black)
    background_start.blit(new_label, (x, y))
    
def render_title_text(word, x, y, font, color): #Renders title text
    my_title_font = pygame.font.SysFont('comicsansms', 80)
    title_label = my_title_font.render(word, 1, (color))
    background_start.blit(title_label, (x, y))
    title_label.set_colorkey(black)


render_title_text("Wizard Rush", 160, 20, "arial", red)
render_text("Start Game", 240, 160, "arial", red)
render_smaller_text("Instructions", 180, 320, "arial", red)
render_smaller_text("Credits", 480, 320, "arial", red)


background_game = pygame.image.load("ActionGameProject/Graphics/stone_brick.png")
background_game = background_game.convert()
background_game = pygame.transform.scale(background_game, (800, 600))


Credits = pygame.image.load("ActionGameProject/Graphics/start_back.png")
Credits = pygame.transform.scale(Credits, (800, 600))
Credits = Credits.convert()
Credits.set_colorkey()
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


Pause = pygame.image.load("ActionGameProject/Graphics/start_back.png")
Pause = pygame.transform.scale(Pause, (800, 600))
Pause = Pause.convert()
Pause.set_colorkey()
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



Instructions = pygame.image.load("ActionGameProject/Graphics/start_back.png")
Instructions = pygame.transform.scale(Instructions, (800, 600))
Instructions = Instructions.convert()
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
render_control_text("Arrow keys and WASD- Movement", 180, 220, "arial", red)
render_control_text("ESC - Pause / resume game", 200, 280, "arial", red)
render_other_text("Press ESC to go back.", 0, 0, "arial", red)


Fireball = pygame.Surface((30,30))
pygame.draw.circle(Fireball, BLUE, (20, 20), 6)
pygame.draw.polygon(Fireball, BLUE, ((20, 14), (8, 17), (20, 20)))
pygame.draw.polygon(Fireball, BLUE, ((20, 17), (4, 20), (20, 23)))
pygame.draw.polygon(Fireball, BLUE, ((20, 20), (8, 23), (20, 26)))
pygame.draw.circle(Fireball, BLUE, (20, 20), 3)
Fireball.set_colorkey(BLACK)


enemyfireball = pygame.Surface((40,40))
pygame.draw.circle(enemyfireball, RED, (20, 20), 6)
pygame.draw.polygon(enemyfireball, RED, ((20, 14), (32, 17), (20, 20)))
pygame.draw.polygon(enemyfireball, RED, ((20, 17), (36, 20), (20, 23)))
pygame.draw.polygon(enemyfireball, RED, ((20, 20), (32, 23), (20, 26)))
pygame.draw.circle(enemyfireball, RED, (20, 20), 3)
enemyfireball.set_colorkey(BLACK)

enemyImage = pygame.image.load("ActionGameProject/Graphics/enemy1.png")
enemyImage = enemyImage.convert()
enemyImage.set_colorkey(WHITE)
enemyImage = pygame.transform.scale(enemyImage, (50,60))
enemyImage = pygame.transform.flip(enemyImage, True, False)