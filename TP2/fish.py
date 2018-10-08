import config as c
from agent import Agent
from random import randint

class Fish(Agent):
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX,pPosY, pSMA)
        self.breedTime=randint(1,c.p["fishBreedTime"])
        self.dead=False
        self.canMove=True

    def decide(self):
        if(not self.dead and self.canMove):
            emptySpace=self.sma.envir.findEmptySpace(self)
            self.breedTime=self.breedTime-1
            if(emptySpace!=None):
                #self.sma.envir.agentsCanMove(self)
                newFishX=self.posX
                newFishY=self.posY
                self.sma.envir.moveAgentCoord(self, emptySpace)
                if(self.breedTime==0):
                    self.sma.addFish(newFishX,newFishY)
                    self.breedTime=c.p["fishBreedTime"]
                return True
            self.canMove=False
            #if(self.breedTime==0):
            #    self.breedTime=c.p["fishBreedTime"]
            self.breedTime=self.breedTime+1
        return False


    def isFish(self):
        return True
    def move(self):
        self.sma.envir.moveAgent(self)

    def canBeEaten(self):
        if(not self.dead):
            return True
        else:
            return False
