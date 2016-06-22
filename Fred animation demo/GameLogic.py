import pygame
import GraphicsLib as GLib
from Util import *

# a great example of an object that can move on the screen
class Hero:
    def __init__(self):
        # ------------------------
        # [REQUIRED PART] for any class that will be drawn on the screen
        # Grab the surface that Graphics people worked very hard on
        self.img = GLib.heroSprite
        # Set the initial coordinate of this object
        self.x = 0
        self.y = 0
        # ------------------------
        # TODO: add more properties to Hero based on your game
        self.vx = 0
        self.vy = 0

    # an example of updating position of the object
    def update(self):
        # TODO: what else hero is going to do in each frame
        self.x += self.vx
        self.y += self.vy

# the minimum class for an object that can be displaced on the screen
class Ball:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img


class Game:
    def __init__(self):
        # initialize the timer to zero. This is like a little clock
        self.timer = 0
        self.hero = Hero()
        self.ball = Ball(250, 250, GLib.ballSpriteBLUE)
        # TODO: add any variables you think will be needed as a property of Game
        # ...
        # ..
        # .
        # TODO: add any objects that you would like to be drawn on the screen
        # Make sure that all of those objects has x, y and img defined as their property
        self.objectsOnScreen = [self.ball , self.hero]
    


    # Try to update all the elements
    # if you want to add another to the screen:                 self.objectsOnScreen.add(x)
    # if you want to remove a object from the screen:           self.objectsOnScreen.remove(x)
    # if you want to switch to another the state                return 10                      --> this switches to state 10
    # if you want to bring a object to the front                
        # just remove it first and then added it back
        # the last added object is going to be on the top
    def updateInState(self, state):
        # increment the timer
        self.timer += 1
        # check what state the game is at
        if state == "Normal":
            # TODO: what the game would do in this state
            # update the position of hero based on its velocity
            self.hero.update()
            # use showAnimationOn functon immported from Util module,
            # it taks three argument, the object to have animation, the animation, and the frameNumber
            # this example switch to the next frame every 5 ticks
            showAnimationOn(self.ball, [GLib.ballSpriteBLUE, GLib.ballSpriteOrange, GLib.someLoadedImage], self.timer / 2)
            # bounceIn(self.hero, 0, 0, 500, 500)
            wrapAroundIn(self.hero, 0, 0, 500, 500)
        elif state == "Pause":
            # Switch to another state by return the state number
            if self.timer - self.savedTime > 20:
                return "Normal"
        # TODO: add more state to the game
        else:
            print("Undefined game state " + str(state))
            exit()
        # return the same state if you decided not to switch a state
        return state

    





    # A method that does all the drawing for you.
    def draw(self, screen):
        # The first line clear the screen
        # TODO: if you want a differnt background, 
            # you can replace the next line                     screen.blit(GLib.Background, (0, 0))
        screen.fill(GLib.BLACK)
        for obj in self.objectsOnScreen:
            screen.blit(obj.img, (obj.x, obj.y))