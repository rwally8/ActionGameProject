import pygame
import GraphicsLib as GLib
from Game_Boarder import Background, Points
from Wizard import Wizard1
from Enemy import Enemy
from Util import *

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

class Fireball:
    def __init__(self, x ,y, img):
        self.x = x
        self.y = y
        self.img = GLib.Fireball

    def update (self):
        self.x + 2 

class Enms:
    def __init__ (self):
        self.lives=[]
        self.enemies=[]
        self.wpn=[]
        self.xpos=[]
        self.ypos=[]
        self.resil=1
    def spawndcd(difficulty):
        EnLst=["grunt"]                             #Current list of all enemies except bosses
        WpnLst=["Firebolt","Fireblast","Aimfire"]   #Current list of all weapons except boss weapons, they are single forward shot, scatter shot, and targeted shot respectively, they do not require new art, but each one will have slightly different behavior programming.
        whm=random.randint(0,0)                     #Change this if we add more enemies
        wpn=random.randint(0,2)                     #Change this if we add more enemy weapons
        seed=random.randint(1,5)                    #Determines the number of enemies spawned, which is then further modulated by the difficulty.
        Etype=EnLst[whm]
        Ewpn=WpnLst[wpn]
        num=seed+(difficulty//1)                    #For this to work difficulty must always be an integer
        xval=800                                    #enum is the number of enemies
        ymod=(500/(num+1))                          #ymod is the value which you must multiply by each ship's number to get it's position.     Change this if y changes from 500.
        return(Etype, Ewpn, num, xval, ymod, difficulty)
    def spwnd (self, mtype, mweapon, xstrt, ystrt, diff):
        self.resil=self.resil+(diff//5)
        if (diff//5)>=1:
            diff=0
        self.lives.append(resil)
        self.enemies.append(mtype)
        self.wpn.append(mweapon)
        self.xpos.append(xstrt)
        self.ypos.append(ystrt)
        self.enemies.append(mtype)
    def check (self, pblltlst):
        bulltnum=0
        for blt in pblltlst:
            enemynum=0
            for enmy in enmylst:
                if pygame.Rect.colliderect(pbltlst[bulltnum], self.enemies[enemynum])!=False:
                    self.lives[enemynum]-=1
                    if self.lives[enemynum]<=0:
                        self.lives.remove(self.lives[enemynum])
                        self.enemies.remove(self.lives[enemynum])
                        self.wpn.remove(self.lives[enemynum])
                        self.xpos.remove(self.lives[enemynum])
                        self.ypos.remove(self.lives[enemynum])
                        self.resil.remove(self.lives[enemynum])
                        enemynum-=1
                    pbltlst.remove(pbltlst[bulltnum])      #removes player shots which hit the enemy, post damage.
                    bulltnum-=1
                enemynum+=1
            bulltnum+=1
    def emovement (self, ennum, movedi):
        strtx=0
        strty=0
        if (self.xpos[ennum]>=100):
            strtx=strtx-1
        if ((self.ypos[ennum]>0)&(movedi=="UP")):
            strty=strty-1
        elif ((self.ypos[ennum]<=0)&(movedi=="UP")):
            movedi="DOWN"
        elif ((self.ypos[ennum]<500)&(movedi=="DOWN")):
            strty=strty+1
        elif ((self.ypos[ennum]>=500)&(movedi=="DOWN")):
            movedi="UP"
        self.ypos[ennum]+=strty
        self.xpos[ennum]+=strtx
    def fire (self, ennum, plrx, plry):
        ammox=self.xpos[ennum]
        ammoy=self.ypos[ennum]
        if self.wpn[ennum]== "Firebolt":
            velox=1
            veloy=0
            numb=1
        elif self.wpn[ennum]== "Fireblast":
            velox=[1,1,1,1,1]
            veloy=[ 1,.5,0,-.5,-1]
            numb=5
        elif self.wpn[ennum]== "Aimfire":
            velox=(plrx-self.xpos[ennun])
            veloy=(plry-self.ypos[ennun])
            numb=1
        return(velox, veloy)



class Game:
    def __init__(self):
        # initialize the timer to zero. This is like a little clock
        self.timer = self.stateTimer = 0
        self.hero = Wizard1(100,300)
        self.background = GLib.background_start
        self.scoreBoard = Points()
        E = []
        # TODO: add any variables you think will be needed as a property of Game
        # ...
        # ..
        # .
        # TODO: add any objects that you would like to be drawn on the screen
        # Make sure that all of those objects has x, y and img defined as their property
        self.objectsOnScreen = []
    


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
                self.objectsOnScreen = [self.hero, self.scoreBoard]
                self.scoreBoard.update(100)
            # TODO: what the game would do in this state
            # update the position of hero based on its velocity
            self.hero.update()
            # use showAnimationOn functon immported from Util module,
            # it taks three argument, the object to have animation, the animation, and the frameNumber
            # this example switch to the next frame every 5 ticks
            #showAnimationOn(self.ball, [GLib.ballSpriteBLUE, GLib.ballSpriteOrange, GLib.someLoadedImage], self.timer / 2)
            # bounceIn(self.hero, 0, 0, 500, 500)
            wrapAroundIn(self.hero, 0, 0, 500, 500)
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
                if type(obj) is list:
                    stack.append(obj)
                else:
                    screen.blit(obj.img, (obj.x, obj.y))

