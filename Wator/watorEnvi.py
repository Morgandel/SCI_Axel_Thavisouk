from fish import Fish
from shark import Shark
import config as c
from random import randint
from environment import Environment

class WatorEnvi(Environment):

    def __init__(self):
        super().__init__()
        self.moore=[None]*8

    def findEmptySpace(self,agent):
        nbSpace=0
        for i in range (-1,2):
            for j in range(-1,2):
                if((i!=0 or y!=0) and i!=j):
                    x=agent.posX+i
                    y=agent.posY+j
                    if(c.p["torus"]==0):
                        outOfBounds= x<0 or x>=c.p["gridSizeX"] or y<0 or y>=c.p["gridSizeY"]
                    else:
                        outOfBounds=False
                        x,y=self.torus(x,y)
                    if(not outOfBounds):
                        if(not self.envir[y][x]):
                            self.moore[nbSpace]=(x,y)
                            nbSpace=nbSpace+1
        if(nbSpace==0):
            return None
        return self.moore[randint(0,nbSpace-1)]

    def findFish(self,agent):
        nbFish=0
        for i in range(-1,2):
            for j in range(-1,2):
                if((i!=0 or y!=0) and i!=j):
                    x=agent.posX+i
                    y=agent.posY+j
                    if(c.p["torus"]==0):
                        outOfBounds= x<0 or x>=c.p["gridSizeX"] or y<0 or y>=c.p["gridSizeY"]
                    else:
                        outOfBounds=False
                        x,y=self.torus(x,y)
                    if(not outOfBounds):
                        if(self.envir[y][x]!=None):
                            if(self.envir[y][x].canBeEaten()):
                                self.moore[nbFish]=(x,y)
                                nbFish=nbFish+1
        if(nbFish==0):
            return None
        return self.moore[randint(0,nbFish-1)]

    def agentsCanMove(self,agent):
        for i in range(-1,2):
            for j in range(-1,2):
                x=agent.posX+i
                y=agent.posY+j
                if(c.p["torus"]==0):
                    outOfBounds= x<0 or x>=c.p["gridSizeX"] or y<0 or y>=c.p["gridSizeY"]
                else:
                    outOfBounds=False
                    x,y=self.torus(x,y)
                if(not outOfBounds):
                    if(self.envir[y][x]!=None):
                        self.envir[y][x].canMove=True

    def torus(self, posX, posY):
        pos=[posX,posY]
        if(posX < 0):
            pos[0]=c.p["gridSizeX"]-1
        elif(posX >= c.p["gridSizeX"]):
            pos[0]=0
        if(posY < 0):
            pos[1]=c.p["gridSizeY"]-1
        elif(posY >= c.p["gridSizeY"]):
            pos[1]=0
        return pos