import pygame
import GraphicsLib as GLib
from Game_Boarder import Background, Points
from Wizard import Wizard1
from Enemy import Enemy
from Util import *
import random

class Object:
    def __init__(self, x ,y, img):
        self.x = x
        self.y = y
        self.img = img

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
        wrapAroundIn(self, 0, 0, 500, 500)

class Fireball:
    def __init__(self, x ,y):
        self.x = x
        self.y = y + 30 
        self.img = GLib.Fireball

    def update (self):
        self.x += 10

class Bullet:
    def __init__(self,ammox,ammoy,velox,veloy):
        self.img = GLib.enemyfireball
        self.x =ammox
        self.y =ammoy
        self.vx = velox
        self.vy = veloy

    def uppos(self):
        self.x +=self.vx
        self.y +=self.vy
        
class Enemynw:
    def __init__(self,life,entype,weapon,exposition,whyposition):
        self.lives=life
        self.entyp=entype
        self.wepn=weapon
        self.x =exposition
        self.y =whyposition
        self.vx = -10
        self.vy = 10
        self.img = GLib.enemyImage
        self.bltlst=[]

    def fire (self,plrx, plry):
        ammox=self.x 
        ammoy=self.y 
        if self.wepn== "Firebolt":
            velox=[10]
            veloy=[0]
            numb=1
        elif self.wepn== "Fireblast":
            velox=[10,10,10,10,10]
            veloy=[ 10,5,0,-5,-10]
            numb=5
        elif self.wepn== "Aimfire":
            velox=[-(plrx-self.x)/20]
            veloy=[-(plry-self.y)/20]
            numb=1
        for i in range(numb):
            nwbullet=Bullet(ammox,ammoy,velox[i],veloy[i])
            self.bltlst.append(nwbullet)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        bounceIn(self, 0, 0, 800, 600)
        for i in range (len(self.bltlst)):
            self.bltlst[i].x-=self.bltlst[i].vx
            self.bltlst[i].y-=self.bltlst[i].vy

class Game:
    def __init__(self):
        # initialize the timer to zero. This is like a little clock
        self.timer = self.stateTimer = 0
        self.hero = Wizard1(100,300)
        self.background = GLib.background_start
        self.scoreBoard = Points()
        self.resil = 0
        self.enemyLs = []
        self.fireballLs = []
        self.enemiesBullets = []
        # TODO: add any variables you think will be needed as a property of Game
        # ...
        # ..
        # .
        # TODO: add any objects that you would like to be drawn on the screen
        # Make sure that all of those objects has x, y and img defined as their property
        self.objectsOnScreen = []
    
    def fire (self):
        x = self.hero.x
        y = self.hero.y
        self.fireballLs.append(Fireball(x, y))

    def spawndcd(self, difficulty):
        EnLst=["grunt"]                             #Current list of all enemies except bosses
        WpnLst=["Firebolt","Fireblast","Aimfire"]   #Current list of all weapons except boss weapons, they are single forward shot, scatter shot, and targeted shot respectively, they do not require new art, but each one will have slightly different behavior programming.
        whm=random.randint(0,0)                     #Change this if we add more enemies
        wpn=random.randint(0,2)                     #Change this if we add more enemy weapons
        seed=random.randint(1,5)                    #Determines the number of enemies spawned, which is then further modulated by the difficulty.
        Etype=EnLst[whm]
        Ewpn=WpnLst[wpn]
        num=seed+(difficulty//1)
        xval=700                                    #enum is the number of enemies
        ymod=(600/(num+1))                          #ymod is the value which you must multiply by each ship's number to get it's position.     Change this if y changes from 500.
        self.resil=self.resil+(difficulty//5)
        if (difficulty//5)>=1:
            difficulty=0
        for i in range (num):
            yval=(i+1)*ymod
            Newen=Enemynw(self.resil, Etype, Ewpn,xval,yval)
            Newen.fire(self.hero.x,self.hero.y)
            self.enemyLs.append(Newen)
            self.enemiesBullets.extend(Newen.bltlst)
            #print (self.enemiesBullets)


    # Try to update all the elements
    # if you want to add another to the screen:                 self.objectsOnScreen.add(x)
    # if you want to remove a object from the screen:           self.objectsOnScreen.remove(x)
    # if you want to switch to another the state                return 10                      --> this switches to state 10
    # if you want to bring a object to the front                
        # just remove it first and then added it back
        # the last added object is going to be on the top
    def updateInState(self, state):
        # increment the timer
        # check what state the game is at
        if state == "Start Menu":
            self.background = GLib.background_start
        elif state == "Pause":
            if self.stateTimer == 0:
                self.background = GLib.Pause
                self.objectsOnScreen = []
        elif state == "Instructions":
           if self.stateTimer == 0:
                self.background = GLib.Instructions
                self.objectsOnScreen = []
        elif state == "Credits":
            if self.stateTimer == 0:
                self.background = GLib.Credits
                self.objectsOnScreen = []
        elif state == "Game":
            self.timer += 1
            if self.stateTimer == 0:
                self.background = GLib.background_game
                self.objectsOnScreen = [self.hero, self.scoreBoard, self.fireballLs, self.enemyLs, self.enemiesBullets]
                self.scoreBoard.update(100)
            # TODO: what the game would do in this state
            # update the position of hero based on its velocity
            self.hero.update()
            for f in self.fireballLs:
                f.update()
            for e in self.enemyLs:
                e.update()
            for e in self.enemyLs:
                for f in self.fireballLs:
                    if hasCollideCirc(e, f, 10):
                        self.fireballLs.remove(f)
                        self.enemyLs.remove(e)
            if self.timer % 50 == 0:
                self.spawndcd(5)
                for e in self.enemyLs:
                    e.fire(self.hero.x,self.hero.y)
            # use showAnimationOn functon immported from Util module,
            # it taks three argument, the object to have animation, the animation, and the frameNumber
            # this example switch to the next frame every 5 ticks
            #showAnimationOn(self.ball, [GLib.ballSpriteBLUE, GLib.ballSpriteOrange, GLib.someLoadedImage], self.timer / 2)
            # bounceIn(self.hero, 0, 0, 500, 500)
        else:
            raise Exception("Invalide state: " + str(state))
        return state

    
    def draw(game, screen):
        # set the background of the game
        if type(game.background) is tuple:
            screen.fill(game.background)
        else:
            screen.blit(game.background, (0, 0))

        # the magic that draw all the objects stored in objectsOnScreen onto the screen
        stack = [game.objectsOnScreen]
        while len(stack) > 0:
            objectsLs = stack.pop()
            for obj in objectsLs:
                #print(type(obj))
                if type(obj) is list:
                    stack.append(obj)
                else:
                    screen.blit(obj.img, (obj.x, obj.y))