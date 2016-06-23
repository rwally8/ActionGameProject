import pygame, sys
pygame.init()
screen=pygame.display.set_mode((800,500))

rendertextvariable = True

black = (0, 0, 0)
yellow = (255, 255, 0) #List of different colors
red = (255, 0, 0)
green = (0, 255, 40)

screen.fill(black) #Sets the screen black to create a place to render text onto

def render_text(word, x, y, font, size, color): #Function to render text. includes specific phrase, coordinates, font size and color
    my_font = pygame.font.SysFont('monospace',40)
    label = my_font.render(word, 1, (color))
    screen.blit(label, (x, y))

if rendertextvariable == True:
    render_text("Sample Title", 240, 20, "monospace", 60, red)
    render_text("Start Game", 40, 80, "monospace", 40, red)
    render_text("Instructions", 480, 80, "monospace", 40, red)
    render_text("Made by...", 200, 300, "monospace", 40, red)
        

pygame.display.flip()
