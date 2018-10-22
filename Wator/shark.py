import Core.config as c
from Core.agent import Agent
from random import randint


class Shark(Agent):
    "Extension de Agent pour l'agent Shark"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX,pPosY, pSMA)
        self.breedTime=randint(1,c.p["sharkBreedTime"])
        self.starveTime=randint(1,c.p["sharkStarveTime"])
        self.dead=False

    def decide(self):
        theMove=self.sma.envir.findFish(self)
        self.breedTime=self.breedTime-1
        self.starveTime=self.starveTime-1
        newSharkX=self.posX
        newSharkY=self.posY
        if(theMove!=None):
            fishToEat=self.sma.envir.getAgent(theMove[0],theMove[1])
            fishToEat.dead=True
            self.sma.envir.moveAgentCoord(self, theMove)
            self.starveTime=c.p["sharkStarveTime"]
            if(self.breedTime==0):
                self.sma.addShark(newSharkX,newSharkY)
                self.breedTime=c.p["sharkBreedTime"]
            return True
        else:
            if(self.starveTime==0):
                self.dead=True
                return False
            emptySpace=self.sma.envir.findEmptySpace(self)
            if(emptySpace!=None):
                newSharkX=self.posX
                newSharkY=self.posY
                self.sma.envir.moveAgentCoord(self, emptySpace)
                if(self.breedTime==0):
                    self.sma.addShark(newSharkX,newSharkY)
                    self.breedTime=c.p["sharkBreedTime"]
                return True
        if(self.breedTime==0):
           self.breedTime=0
        self.breedTime=self.breedTime+1
        return False

    def type(self):
        return "shark"

    def canBeEaten(self):
        return False
