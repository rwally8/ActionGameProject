import pygame
from pygame import mixer
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
start_sound = pygame.mixer.music.load("ActionGameProject/desertm.wav")
pygame.mixer.music.play(-1)
#-------------------------
# initialize the game
#-------------------------
## GameLogic should contain all the classes like Hero, Ball, Ship etc.
from GameLogic import *

# acquire a game object
game = Game()
pygame.key.set_repeat(1)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#BEIGINING STATES
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#The game will probably begin at a state called "start_menu," or something along those lines. The game begins when the player clicks the start button, which changes the state to the "Normal," or
#gameplay state
preState = state = "Start Menu"
#I have put the starting state as "start_menu" as a place holder. Change this based on what the state for the start menu is called. 
#----------------------------------------------------------------------------------------------------------------------------------------------------




while True:
    #-------------------------
    # Our event hanlding loop
    #-------------------------
    eventList = pygame.event.get()
    # grab all events pygame recieved
    for event in eventList:
        if event.type == pygame.QUIT:
            # if someone tries to close the Windows
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                game.hero.y -= 10
            elif event.key == pygame.K_s:
                game.hero.y +=10
            elif event.key == pygame.K_a:
                game.hero.x -= 10
            elif event.key == pygame.K_d:
                game.hero.x += 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.hero.y -= 10
            elif event.key == pygame.K_DOWN:
                game.hero.y += 10
            elif event.key == pygame.K_LEFT:
                game.hero.x -= 10
            elif event.key == pygame.K_RIGHT:
                game.hero.x += 10
            elif event.key == pygame.K_ESCAPE:
                if state == "Game":
                    state = "Pause"
                elif state == "Pause":
                    state = "Game"                
                elif state == "Credits":
                    state = "Start Menu"
                elif state == "Instructions":
                    state = "Start Menu"
                elif state == "Game Over":
                    state = "Start Menu"
            elif event.key == pygame.K_SPACE:
                game.fire()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "Start Menu":
                x, y = event.pos
                if ((x>=250)&(x<=510)&(y>=165)&(y<=220)):
                    game = Game()
                    state="Game"
                    pygame.mixer.music.stop()
                elif ((x>=180)&(x<=390)&(y>=325)&(y<=360)):
                    state="Instructions"
                elif ((x>=480)&(x<=575)&(y>=325)&(y<=360)):
                    state="Credits"


    # print(state)
    #-------------------------
    # The main game logic block
    #-------------------------
    # check if either updateInState(...) or user input altered state
    # initialized stateTimer to 0 to signal the begining of a new state
    if state != preState:
        game.stateTimer = 0
    preState = state
    ## all the exciting interactive of objects happen in updateGame()
    state = game.updateInState(state)
    # update both timer and stateTimer, if the state changed, clear the stateTimer
    game.timer += 1
    game.stateTimer += 1

    #-------------------------
    # The graphics block
    #-------------------------
    game.draw(screen)

    #-------------------------
    # display this frame and 
    #-------------------------
    pygame.display.flip()
    # ask pygame to display everythong on the GUI
    pygame.time.wait(25)
    # delay the time, so can see the Windows, controls the frame rate   