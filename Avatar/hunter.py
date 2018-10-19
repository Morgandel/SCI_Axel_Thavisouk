import Core.config as c
#from Avatar.avatar import Avatar
from agent import Agent

class Hunter(Agent):
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX,pPosY, pSMA)
        self.turnCount=c.p["speedHunter"]

    def decide(self):
        self.turnCount-=1
        if(self.turnCount<=0):
            self.turnCount=c.p["speedHunter"]
            if(self.sma.isInvincible()):
                newPos=self.sma.getMaxDistance(self.posX,self.posY)
            else:
                newPos=self.sma.getMinDistance(self.posX,self.posY)
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
