import config as c
from agent import Agent

class Fish(Agent):
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX,pPosY, pSMA)
        self.breedTime=c.p["fishBreedTime"]
        self.dead=False

    def decide(self):
        if(not self.dead):
            emptySpace=self.sma.envir.findEmptySpace(self)
            self.breedTime=self.breedTime-1
            if(emptySpace!=None):
                newFishX=self.posX
                newFishY=self.posY
                self.sma.envir.moveAgentCoord(self, emptySpace)
                if(self.breedTime==0):
                    self.sma.addFish(newFishX,newFishY)
                    self.breedTime=c.p["fishBreedTime"]
                return True
            if(self.breedTime==0):
                self.breedTime=c.p["fishBreedTime"]
        return True

    def move(self):
        self.sma.envir.moveAgent(self)

    def canBeEaten(self):
        if(not self.dead):
            return True
        else:
            return False
