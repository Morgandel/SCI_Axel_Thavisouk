import Core.config as c
from Core.agent import Agent

class Hunter(Agent):
    "Extension de Agent pour l'agent Hunter"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX,pPosY, pSMA)
        self.turnCount=c.p["speedHunter"]

    def decide(self):
        self.turnCount-=1
        if(self.turnCount<=0):
            self.turnCount=c.p["speedHunter"]
            if(self.sma.isInvincible()):
                newPos=self.sma.getMinDistance(self.posX,self.posY,'max')
            else:
                newPos=self.sma.getMinDistance(self.posX,self.posY,min)
            dest=self.sma.envir.getAgent(newPos[0], newPos[1])
            if(dest==None):
                self.sma.envir.moveAgentCoord(self,newPos)
            elif(dest.type()=="avatar"):
                print("perdu")
                dest.dead=True
            return True
        return False

    def type(self):
        return "hunter"
