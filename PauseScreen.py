import pygame, sys
pygame.init()
screen=pygame.display.set_mode((800,500))

differentrendervariable = True

black = (0, 0, 0)
red = (255, 0, 0)
gray = (77, 82, 72)

screen.fill(black)

def render_paused_text(word, x, y, font, color):
    my_paused_font = pygame.font.SysFont('arial', 80, bold=True)
    paused_label = my_paused_font.render(word, 1, (color))
    screen.blit(paused_label, (x, y))

def render_resume_text(word, x, y, font, color):
    my_resume_font = pygame.font.SysFont('arial', 30)
    resume_label = my_resume_font.render(word, 1, (color))
    screen.blit(resume_label, (x, y))

if differentrendervariable == True:
    render_paused_text("Paused!", 260, 100, "arial", red) #Renders text with specific phrase, coordinates, font, size
    render_resume_text("Press [Insert Key] to continue!", 220, 280, "arial", red)

pygame.display.flip()
