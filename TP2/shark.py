import config as c
from agent import Agent

class Shark(Agent):
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX,pPosY, pSMA)
        self.breedTime=c.p["sharkBreedTime"]
        self.starveTime=c.p["sharkStarveTime"]
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
            self.breedTime=c.p["sharkBreedTime"]
        return True

    def isFish(self):
        return False

    def canBeEaten(self):
        return False
