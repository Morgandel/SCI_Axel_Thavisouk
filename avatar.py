import config as c
from agent import Agent
from wall import Wall
from pynput.keyboard import Key, Controller
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

    def decide(self):
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
        print(self.posX,self.posY,"Avatar")
        if(dest==None):
            self.sma.envir.moveAgentCoord(self, [self.posX+self.dirX, self.posY+self.dirY])
        #if(isinstance(dest,Hunter)):
        elif(dest.type()=="hunter"):
            print("perdu avatar")
            self.dead=True
        elif(dest.type()=="wall"):
            print("mur")
            self.dirX=0
            self.dirY=0
            return False
        elif(dest.type()=="defender"):
            dest.dead=True
            self.defenderConsumed+=1
            self.invincibility=c.p["invincibility"]
            self.sma.envir.moveAgentCoord(self, [self.posX+self.dirX, self.posY+self.dirY])
        return True

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
