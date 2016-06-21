import pygame

def director(move, xvel, yvel):                         #edit this function based on how large things become, it is currently expecting a 800 by 500 screen, and a 10 by 10 charactor
    if move.type == pygame.KEYDOWN:
        if ((move.key == pygame.K_UP)):
            yvel=yvel-1
        elif ((move.key == pygame.K_DOWN)):
            yvel=yvel+1
        elif ((move.key == pygame.K_RIGHT)):
            xvel=xvel+1
        elif ((move.key == pygame.K_LEFT)):
            xvel=xvel-1
    if move.type == pygame.KEYUP:
        if ((move.key == pygame.K_UP)):
            yvel=yvel+1
        elif ((move.key == pygame.K_DOWN)):
            yvel=yvel-1
        elif ((move.key == pygame.K_RIGHT)):
            xvel=xvel-1
        elif ((move.key == pygame.K_LEFT)):
            xvel=xvel+1
    return (xvel, yvel)    
