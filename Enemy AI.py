import pygame
import zellegraphics as zg
import time
import random

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
        if ((self.ypos[ennum]>0)&(movedi="UP")):
            strty=strty-1
        elif ((self.ypos[ennum]<=0)&(movedi="UP")):
            movedi="DOWN"
        elif ((self.ypos[ennum]<500)&(movedi="DOWN")):
            strty=strty+1
        elif ((self.ypos[ennum]>=500)&(movedi="DOWN")):
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
