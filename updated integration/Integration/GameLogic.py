import pygame
import GraphicsLib as GLib
from Game_Boarder import Background, Points
from Enemy import Enemy
from Util import *
import random


class Object:
    def __init__(self, x ,y, img):
        self.x = x
        self.y = y
        self.img = img


class Health:
    def __init__(self):
        self.x = 50
        self.y = 25
        self.health = 3
        self.img = GLib.heart3
        self.lastHttenTime = 0

    def update(self):
        if self.health == 2:
            self.img = GLib.heart2
        elif self.health == 3:
            self.img = GLib.heart3
        elif self.health == 1:
            self.img = GLib.heart1
        else:
            raise Exception( str(self.health) )
        
    def hitten(self, time):
        print("last hitten" , self.lastHttenTime, time)
        if time - self.lastHttenTime > 100:
            print("heath" , self.health)
            self.health -= 1
            self.lastHttenTime = time


class Wizard1:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0
        self.lastFiredTIme = 0
        # import image
        self.img = GLib.wizardHero
        #change the size of the wizard
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        bounceIn(self, 0, 100, 350, 600)


    def fire(self, time):
        if time - self.lastFiredTIme > 30:
            self.lastFiredTIme = time
            return Fireball(self.x, self.y)
        
class Fireball:
    def __init__(self, x ,y):
        self.x = x
        self.y = y + 30 
        self.img = GLib.Fireball

    def update (self):
        self.x += 20

class Bullet:
    def __init__(self,ammox,ammoy,velox,veloy):
        self.img = GLib.enemyfireball
        self.x =ammox
        self.y =ammoy
        self.vx = velox
        self.vy = veloy

    def update(self):
        self.x -=self.vx
        self.y +=self.vy
        
class Enemynw:
    def __init__(self,life,entype,weapon,exposition,whyposition, direct):
        self.lives=life
        self.entyp=entype
        self.wepn=weapon
        self.x =exposition
        self.y =whyposition
        self.vx = -10
        self.vy = 10
        self.img = GLib.enemyImage
        self.bltlst=[]
        self.up=direct

    def fire(self,plrx, plry):
        ammox=self.x 
        ammoy=self.y 
        if self.wepn== "Firebolt":
            velox=[5]
            veloy=[0]
            numb=1
        elif self.wepn== "Fireblast":
            velox=[10,10,10,10,10]
            veloy=[ 10,5,0,-5,-10]
            numb=5
        elif self.wepn== "Aimfire":
            velox=[-(plrx-self.x)/50]
            veloy=[(plry-self.y)/50]
            numb=1
        for i in range(numb):
            nwbullet=Bullet(ammox,ammoy,velox[i],veloy[i])
            self.bltlst.append(nwbullet)
        return numb                                             #in testing
    def update(self):
        if self.up==True:
            self.x += self.vx
            self.y -= self.vy
            if self.y<=0:
                self.up=False
        elif self.up==False:
            self.x += self.vx
            self.y += self.vy
        bounceIn(self, 350, 0, 800, 600)
        
        
class Game:
    def __init__(self):
        # initialize the timer to zero. This is like a little clock
        self.timer = self.stateTimer = 0
        self.hero = Wizard1(100,300)
        self.background = GLib.background_start
        self.healthPoint = Health()
        self.scoreBoard = Points()
        self.resil = 1
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
        self.prirtimor=0
        self.first=True
        self.swtcerup=True
    
    def fire (self):
        fireball = self.hero.fire(self.timer)
        if fireball:
            self.fireballLs.append(fireball)
            GLib.fireball.play()

    def spawndcd(self, difficulty):
        EnLst=["grunt"]                             #Current list of all enemies except bosses
        WpnLst=["Firebolt","Fireblast","Aimfire"]   #Current list of all weapons except boss weapons, they are single forward shot, scatter shot, and targeted shot respectively, they do not require new art, but each one will have slightly different behavior programming.
        whm=random.randint(0,0)                     #Change this if we add more enemies
        wpn=random.randint(0,2)                     #Change this if we add more enemy weapons
        Etype=EnLst[whm]
        Ewpn=WpnLst[wpn]
        num=1
        rndspwn=10*(.00001+random.random())
        xval=800                                    #enum is the number of enemies
        ymod=(600/(rndspwn+1))                          #ymod is the value which you must multiply by each ship's number to get it's position.     Change this if y changes from 500.
        self.resil=self.resil+(difficulty//5)
        if (difficulty//5)>=1:
            difficulty=1
        for i in range (num):
            yval=(i+1)*ymod
            if self.swtcerup==True: 
                Newen=Enemynw(self.resil, Etype, Ewpn,xval,yval,True)
                self.swtcerup=False
            elif self.swtcerup==False:
                Newen=Enemynw(self.resil, Etype, Ewpn,xval,yval,False)
                self.swtcerup=True
            holder=Newen.fire(self.hero.x,self.hero.y)
            self.enemyLs.append(Newen)
            #self.enemiesBullets=[]
            #for i in range (len(self.enemyLs)):
            #    self.enemiesBullets.extend(self.enemyLs[i].bltlst)
            #self.enemiesBullets.extend(Newen.bltlst)
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
        diff=1                                          #currently a constant, but should be more fluid once the game is finished
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
        elif state == "Game Over":
            if self.stateTimer == 0:
                self.background = GLib.Game_Over
                self.objectsOnScreen = []
        elif state == "Game":
            self.timer += 1
            if self.stateTimer == 0:
                self.background = GLib.background_game
                self.objectsOnScreen = [self.hero, self.scoreBoard, self.fireballLs, self.enemyLs, self.enemiesBullets, self.healthPoint]
            self.scoreBoard.update()
            # TODO: what the game would do in this state
            # update the position of hero based on its velocity
            self.hero.update()
            showAnimationOn(self.hero, GLib.wizard_animation, self.timer/10)
            self.healthPoint.update()
            for f in self.fireballLs:
                f.update()
            for e in self.enemyLs:
                e.update()
            for e in self.enemyLs:
                for f in self.fireballLs:
                    if hasCollideRect(e, f):
                        self.fireballLs.remove(f)
                        if e in self.enemyLs:
                            self.scoreBoard.score += 1
                            self.enemyLs.remove(e)
            for b in self.enemiesBullets:
                if hasCollideRect(b, self.hero):
                    self.enemiesBullets.remove(b)
                    self.healthPoint.hitten(self.timer)
                    if self.healthPoint.health == 0:
                        return "Game Over"


            if self.first==True:
                self.prirtimor=self.timer
                self.first=False
            elif self.timer-self.prirtimor>=(100/diff):                  #this will eventually need fluidity, instead of being a constant  #change post testing
                self.spawndcd(diff)                                    #this will eventually need fluidity, instead of being a constant
                self.prirtimor=self.timer                     
                for e in self.enemyLs:
                    Newnum=e.fire(self.hero.x,self.hero.y)
                    bltlstlength=len(e.bltlst)
                    for i in range (Newnum):
                        self.enemiesBullets.append(e.bltlst[bltlstlength-(i+1)])            #in testing
            for i in self.enemiesBullets:
                i.update()
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