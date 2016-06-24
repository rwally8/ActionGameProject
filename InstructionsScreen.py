import pygame, sys
pygame.init()
screen=pygame.display.set_mode((800, 500))

somerendervariable = True

black = (0, 0, 0)
red = (255, 0, 0)

screen.fill(black)

def render_control_text(word, x, y, font, color):
    my_control_font = pygame.font.SysFont('arial', 40)
    control_label = my_control_font.render(word, 1, (color))
    screen.blit(control_label, (x, y))

def render_other_text(word, x, y, font, color):
    my_other_text = pygame.font.SysFont('arial', 20, bold=False, italic=True)
    other_label = my_other_text.render(word, 1, (color))
    screen.blit(other_label, (x, y))

if somerendervariable == True:
    render_control_text("Controls:", 340, 80, "arial", red)
    render_control_text("Space bar - Shoot", 270, 160, "arial", red)
    render_control_text("Arrow keys - Movement", 232, 220, "arial", red)
    render_control_text("ESC - Pause / resume game", 200, 280, "arial", red)
    render_other_text("Press ESC to go back.", 0, 0, "arial", red)

pygame.display.flip()
