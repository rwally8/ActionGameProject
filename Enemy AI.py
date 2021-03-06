import pygame
import time
import random

class Bullet:
    def __init__(self,ammox,ammoy,velox,veloy):
        self.xpos=ammox
        self.ypos=ammoy
        self.velocx=velox
        self.velocy=veloy
    def uppos(self):
        self.xpos+=self.velocx
        self.ypos+=self.velocy
        
class Enemynw:
    def __init__(self,life,entype,weapon,exposition,whyposition):
        self.lives=life
        self.entyp=entype
        self.wpn=weapon
        self.xpos=exposition
        self.ypos=whyposition
        self.bltlst=[]

    def fire (self):
        ammox=self.xpos
        ammoy=self.ypos
        if self.wpn== "Firebolt":
            velox=[1]
            veloy=[0]
            numb=1
        elif self.wpn== "Fireblast":
            velox=[1,1,1,1,1]
            veloy=[ 1,.5,0,-.5,-1]
            numb=5
        elif self.wpn== "Aimfire":
            velox=[(plrx-self.enemies[ennun].xpos)]
            veloy=[(plry-self.enemies[ennun].xpos)]
            numb=1
        for i in range (numb):
            nwbullet=Bullet(ammox,ammoy,velox[i],veloy[i])
            self.bltlst.append(nwbullet)
'''
e = Enemynw( ... )
e.fire()
e2 = Enemynw( ... )
for e in list:
    e.fire()
'''

class Enms:
    def __init__ (self):
        self.enemies=[]
        self.resil=1
    def spawndcd(difficulty):
        EnLst=["grunt"]                             #Current list of all enemies except bosses
        WpnLst=["Firebolt","Fireblast","Aimfire"]   #Current list of all weapons except boss weapons, they are single forward shot, scatter shot, and targeted shot respectively, they do not require new art, but each one will have slightly different behavior programming.
        whm=random.randint(0,0)                     #Change this if we add more enemies
        wpn=random.randint(0,2)                     #Change this if we add more enemy weapons
        seed=random.randint(1,5)                    #Determines the number of enemies spawned, which is then further modulated by the difficulty.
        Etype=EnLst[whm]
        Ewpn=WpnLst[wpn]
        num=seed+(difficulty//1)
        xval=800                                    #enum is the number of enemies
        ymod=(500/(num+1))                          #ymod is the value which you must multiply by each ship's number to get it's position.     Change this if y changes from 500.
        self.resil=self.resil+(difficulty//5)
        if (difficulty//5)>=1:
            difficulty=0
        for i in range (num):
            yval=(i+1)*ymod
            Newen=Enemynw(resil, whm, wpn,xval,yval)
            self.enemies.append(Newen)

'''
    def check (self, pblltlst):
        bulltnum=0
        for blt in pblltlst:
            enemynum=0
            for enmy in enmylst:
                if pygame.Rect.colliderect(pbltlst[bulltnum], self.enemies[enemynum].enm)!=False:
                    self.enemies[enemynum].lives-=1
                    if self.enemies[enemynum].lives<=0:
                        self.enemies.remove(self.enemies[enemynum])
                        enemynum-=1
                    pbltlst.remove(pbltlst[bulltnum])      #removes player shots which hit the enemy, post damage.
                    bulltnum-=1
                enemynum+=1
            bulltnum+=1
'''
    def volly(self):
        allxs=[]
        allys=[]
        allxvs=[]
        allyvs=[]
        for ship in self.enemies:
            a=ship.fire()
    def emovement (self, ennum, movedi):
        strtx=0
        strty=0
        if (self.enemies[ennum].xpos>=100):
            strtx=strtx-1
        if ((self.enemies[ennum].ypos>0)&(movedi="UP")):
            strty=strty-1
        elif ((self.enemies[ennum].ypos<=0)&(movedi="UP")):
            movedi="DOWN"
        elif ((self.enemies[ennum].ypos<500)&(movedi="DOWN")):
            strty=strty+1
        elif ((self.enemies[ennum].ypos>=500)&(movedi="DOWN")):
            movedi="UP"
        self.enemies[ennum].ypos+=strty
        self.enemies[ennum].xpos+=strtx
        return(movedi)

