import config as c
from agent import Agent
from wall import Wall
import numpy as np


class Avatar(Agent):
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX,pPosY, pSMA)
        self.dirX = 0
        self.dirY = 0
        self.dead = False
        self.invincibility=0
        self.defenderConsumed=0
        self.turnCount=c.p["speedAvatar"]

    def decide(self):
        self.turnCount-=1
        if(self.turnCount<=0):
            self.turnCount=c.p["speedAvatar"]
            if(self.invincibility>0):
                self.invincibility-=1
                if(self.invincibility==0):
                    self.sma.changeColor(self.circle,"blue")
            if(c.p["torus"]==0):
                oob=self.sma.envir.isOutOfBound(self.posX+self.dirX, self.posY+self.dirY)
                if(oob):
                    self.dirX=0
                    self.dirY=0
                    return False
            else:

                # newPos=self.sma.envir.torus(self.posX+self.pasX, self.posY+self.pasY)
                # wall=newPos[0]!=self.posX+self.pasX or newPos[1]!=self.posY+self.pasY
                offsetX=self.dirX
                # offsetY=self.pasY
                # if(self.posX+self.pasX!=newPos[0]):
                #     offsetX=newPos[0]-self.posX
                # if(self.posY+self.pasY!=newPos[1]):
                #     offsetY=newPos[1]-self.posY

            # if(c.p["torus"]==1):
            #     dest=self.sma.envir.getAgent(newPos[0],newPos[1])
            # else:
            dest=self.sma.envir.getAgent(self.posX+self.dirX, self.posY+self.dirY)
            if(dest==None):
                self.sma.envir.moveAgentCoord(self, [self.posX+self.dirX, self.posY+self.dirY])
            #if(isinstance(dest,Hunter)):
            elif(dest.type()=="hunter"):
                print("Perdu !")
                self.dead=True
            elif(dest.type()=="wall"):
                self.dirX=0
                self.dirY=0
                return False
            elif(dest.type()=="defender"):
                dest.dead=True
                self.defenderConsumed+=1
                self.invincibility=c.p["invincibility"]
                self.sma.changeColor(self.circle,"pink")
                self.sma.envir.moveAgentCoord(self, [self.posX+self.dirX, self.posY+self.dirY])
            elif(dest.type()=="winner"):
                self.defenderConsumed+=1
                dest.dead=True
            return True
        return False

    def getNeibourgh(self):
        return np.array([(self.posX+1,self.posY),(self.posX-1,self.posY),(self.posX,self.posY+1),(self.posX,self.posY-1)])

    def type(self):
        return 'avatar'

    def onPress(self,e):
        key=e.keysym.lower()
        if(key=="up"):
            self.dirY=-1
            self.dirX=0
        elif(key=="down"):
            self.dirY=1
            self.dirX=0
        elif(key=="left"):
            self.dirY=0
            self.dirX=-1
        elif(key=="right"):
            self.dirY=0
            self.dirX=1
        elif(key=="z"):
            c.p["speedHunter"]+=1
            print("Vitesse du hunter à "+str(c.p["speedHunter"]))
        elif(key=="a"):
            if(c.p["speedHunter"]>1):
                c.p["speedHunter"]-=1
            print("Vitesse du hunter à "+str(c.p["speedHunter"]))
        elif(key=="w"):
            if(c.p["refresh"]>1):
                c.p["refresh"]-=1
            print("Vitesse du jeu à "+str(c.p["refresh"]))
        elif(key=="x"):
            c.p["refresh"]+=1
            print("Vitesse du jeu à "+str(c.p["refresh"]))
        elif(key=="o"):
            if(c.p["speedAvatar"]>1):
                c.p["speedAvatar"]-=1
            print("Vitesse de l'avatar à "+str(c.p["speedAvatar"]))
        elif(key=="p"):
            c.p["speedAvatar"]+=1
            print("Vitesse de l'avatar à "+str(c.p["speedAvatar"]))
