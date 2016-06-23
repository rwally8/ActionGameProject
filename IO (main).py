import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# <<ADVANCED>> If you want KEYDOWN event to fire continuously, when a key is held down
# ============ give it two argument, both of them are interval of KEYDOWN event
#pygame.key.set_repeat(50, 50)

#-------------------------
# initialize the game
#-------------------------
## GameLogic should contain all the classes like Hero, Ball, Ship etc.
from GameLogic import *

# acquire a game object
game = Game()

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#BEIGINING STATES
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#The game will probably begin at a state called "start_menu," or something along those lines. The game begins when the player clicks the start button, which changes the state to the "Normal," or
#gameplay state
state = "start_menu"
#I have put the starting state as "start_menu" as a place holder. Change this based on what the state for the start menu is called. 
#----------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------
# Our Main Loop
#-------------------------
while True:
    #-------------------------
    # Our event hanlding loop
    #-------------------------
    ## You are not supposed to call any graphics method like blit or flip here,
    ## All you need to do is update some state of game.
    eventList = pygame.event.get()
    # grab all events pygame recieved
    for event in eventList:
        if event.type == pygame.QUIT:
            # if someone tries to close the Windows
            exit()
        if event.type == pygame.KEYDOWN:
            # "hero" is used here as the default class name, change the "game.hero" based on whatever the class for the players model is named
            if event.key == pygame.K_UP:
                game.hero.vy -= 2
            elif event.key == pygame.K_DOWN:
                game.hero.vy += 2
            elif event.key == pygame.K_LEFT:
                game.hero.vx -= 2
            elif event.key == pygame.K_RIGHT:
                game.hero.vx += 2
            elif event.key == pygame.K_ESCAPE:
                if state == "Normal":
                    # you can add an arbitrary attributes of game in this way
                    game.savedTime = game.timer
                    state = "Pause"
                else:
                    state = "Normal"
            elif event.key == pygame.K_SPACE:
                game.bullet.vx -=3
                #gives projectile a velocity when space is pressed.
                #change name "bullet" based on whatever the projectiles class is named.
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #FOR THE START MENU
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
            elif event.key == pygame.K_p:
                if state == "start_menu":
                    state = "Normal"
                    #By pressing "p" on the start menu, you will enter the "Normal" state and begin playing the game.
            elif event.key == pygame.K_ESCAPE:
                if state == "Normal"
                    state = "start_menu"
                    #This would give the player the option to quit back to the start menu by pressing the key "escape." This is something that we can remove if we do not want to give the option
                    #to return to the main menu during the game. 
            elif event.key == pygame.K_i:
                if state == "start_menu":
                    state = "Instruction"
                    #By pressing the "i" key on the main menu you will enter the "Instruction" state and will be brought to the instructions page.
            elif event.key == pygame.K_ESCAPE:
                if state == "Instruction":
                    state = "start_menu"
                    #This gives the player the option to return to the start screen after entering the instructions state by pressing the key "escape"
            elif event.key == pygame.K_o:
                if state == "start_menu":
                    state = "Credits"
                    #By pressing the "o" key on the start menu, you will enter the "Credits" state, and will be brought to the credits page.
            elif event.key == pygame.K_ESCAPE:
                if state == "Credits":
                    state = "start_menu"
                    #By pressing the "escape" key, you will be taken back to the start menu if your state is "Credits."
            #Using the mouse to select the option you want would be optimal, but this method of simply pressing keys to enter the desired state is much easier to 
            #implement. If we want to we can look to replace these settings with mouse control. This method also requires some aspects to be added to the start menu, such as 
            #parenthesis around the different options that signal which key to press
            # Example: "Play (p)" or "Instructions(i)" and etc. 
            #it would also require aspects of the same nature to be added to the other menus, signalling to the player how to get back to the start menu.
            # Example: "Return to Title Screen (esc)"
            #An alternative to using the escape function to return to the title screen would be to add an else statement to the comands for entering the different states,
            #much like the one implemented in the pause section. However, the escape key returning you to the title screen seems more logical.
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #FOR EXTRA FEATURES IF TIME PERMITS
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #If time permits, multiple different fire modes could be set to different states, and a key could be used to set the state to the desired fire mode.
            #Fire mode implementation could look something like this
            elif event.key == pygame.K_z:
                state = "Normal"
            elif event.key == pygame.K_x:
                state = "Fire2"
            elif event.key == pygame.K_c:
                state = "Fire3"
            #This method may run into problems, mainly concerning the base fire mode. If the pause menu also deals with the state of normal, then after pausing you would be reset into fire mode 1, 
            #even if you were in another fire mode before pausing. Also, because the first fire mode is going off the normal, or default, state of the game, all other fire modes would have to 
            #contain the things that the normal state needs to run the game. 
            #One potential solution may be different fire keys, each of which shoots a different projectile, but this does not seem ideal. 
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #CONTROLS THAT ALLOW THE PLAYER TO STOP
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------         
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                game.hero.vy == 0
            elif event.key == pygame.K_DOWN:
                game.hero.vy == 0
            elif event.key == pygame.K_LEFT:
                game.hero.vx == 0
            elif event.key == pygame.K_RIGHT:
                game.hero.vx == 0
        #These controls allow the player to stop moving in a direction by releasing a key, which is optimal for doging and aiming. It also makes it easier to change directions
        #If, for some reason, we do not want the player to be able to stop, remove these controls.
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------- 


    #-------------------------
    # The main game logic block
    #-------------------------
    ## all the exciting interactive of objects happen here
    ## game.updateInState() will return the next state
    state = game.updateInState(state)

    #-------------------------
    # The graphics block
    #-------------------------
    game.draw(screen)

    #-------------------------
    # display this frame and 
    #-------------------------
    pygame.display.flip()
    # ask pygame to display everythong on the GUI
    pygame.time.wait(100)
    # delay the time, so can see the Windows, controls the frame rate