import pygame
import zellegraphics as zg
import time
import random
import Proxies

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

def damage(life, invince, plrgrp, eblltgrp, enmygrp):
    if (((pygame.sprite.groupcollide(plrgrp, eblltgrp, False, True, collided = None)!=None)|(pygame.sprite.groupcollide(plrgrp, enmygrp, False, False, collided = None)))&(invince<=0)):
        life = life-1
        invince=5
    return (life, invince)

class Enms:
    def __init__ (self):
        self.lives=[]
        self.enemies=[]
        self.exst=[]
        self.wpn=[]
    def check (self, pblltgrp, enmygrp):
        for Enemies in (pygame.sprite.groupcolide(pblltgrp, enmygrp, True, False, collided = None)):
            pos=self.enemies.index(Enemies)
            self.lives[pos]=self.lives[pos]-1
            if (self.lives[pos]=0):
                self.enemies.exist[pos]=False
            
            

def spawndcd(difficulty):
    EnLst=["grunt"]             #Current list of all enemies except bosses
    whm=random.randint(0,0)     #Change this if we add more enemies
    seed=random.randint(1,5)    #Determines the number of enemies spawned, which is then further modulated by the difficulty.
    num=seed+difficulty         #For this to work difficulty must always be an integer
    return(EnLst[whm],num)

def spwning(enum):              #edit this function based on how large things become, it is currently expecting a 800 by 500 screen.
    xval=800                    #enum is the number of enemies
    ymod=(500/(enum+1))         #ymod is the value which you must multiply by each ship's number to get it's position
    return(xval, ymod)



'''
while(cont==False):
    x = Proxies.tstsrt()    #remove by the end, and replace with the real function
    if x=="procede":
        cont=True
'''
