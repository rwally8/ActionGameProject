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
        self.vy = 10

    # an example of updating position of the object
    def update(self):
        # TODO: what else hero is going to do in each frame
        self.x += self.vx
        self.y += self.vy

class Enms:
    def __init__ (self):
        import random
        import pygame
        self.lives=[]
        self.enemies=[]
        self.exst=[]
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
        return(Etype, Ewpn, num, xval, ymod)
    def spwnd (self, mtype, mweapon, xstrt, ystrt, diff):
        self.resil=self.resil+(diff//5)
        if (diff//5)>=1:
            diff=0
        self.exst.append(True)
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
                if Pygame.Rect.contains(pbltlst[bulltnum], self.enemies[enemynum])!=False:
                    self.lives[enemynum]-=1
                    del pbltlst[bulltnum]      #removes player shots which hit the enemy, post damage.
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
        self.timer = 0
        self.hero = GLib.Wizard1(400,300)
        self.background = GLib.Background(0,0)
        # TODO: add any variables you think will be needed as a property of Game
        # ...
        # ..
        # .
        # TODO: add any objects that you would like to be drawn on the screen
        # Make sure that all of those objects has x, y and img defined as their property
        self.objectsOnScreen = [self.background, self.hero]
    


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
            #showAnimationOn(self.ball, [GLib.ballSpriteBLUE, GLib.ballSpriteOrange, GLib.someLoadedImage], self.timer / 2)
            # bounceIn(self.hero, 0, 0, 500, 500)
            wrapAroundIn(self.hero, 0, 0, 500, 500)
        return state

    
    # A method that does all the drawing for you.
    def draw(self, screen):
        # The first line clear the screen
        # TODO: if you want a differnt background, 
            # you can replace the next line                     screen.blit(GLib.Background, (0, 0))
        screen.fill(GLib.BLACK)
        for obj in self.objectsOnScreen:
            screen.blit(obj.img, (obj.x, obj.y))