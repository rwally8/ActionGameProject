import pygame, sys
pygame.init()
screen=pygame.display.set_mode((800,500))

renderdeathtext = True #Sets up the if statement to render text

black = (0, 0, 0)
red = (255, 0, 0)

screen.fill(black)

def render_death_text(word, x, y, font, color):
    my_death_font = pygame.font.SysFont('arial', 80, bold=True)
    death_label = my_death_font.render(word, 1, (color))
    screen.blit(death_label, (x, y))

def render_restart_text(word, x, y, font, color):
    my_restart_font = pygame.font.SysFont('arial', 30)
    restart_label = my_restart_font.render(word, 1, (color))
    screen.blit(restart_label, (x, y))

if renderdeathtext == True:
    render_death_text("GAME   OVER", 180, 100, "arial", red)
    render_restart_text("Would you like to play again?", 240, 300, "arial", red)

pygame.display.flip()
