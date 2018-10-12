import config as c
from agent import Agent

class Particules(Agent):
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pPasX, pPasY, pSMA):
        self.posX=pPosX
        self.posY=pPosY
        self.pasX=pPasX
        self.pasY=pPasY
        self.sma=pSMA
        self.circle=None
        self.rebound=0


    def decide(self):
        wall=False
        if(c.p["torus"]==0):
            bounds=self.sma.envir.wallBounce(self.posX+self.pasX, self.posY+self.pasY)
            if(bounds[0] != 0 or bounds[1]!=0):
                if(bounds[0]!=0):
                    self.pasX=bounds[0]
                if(bounds[1]!=0):
                    self.pasY=bounds[1]
                if(c.p["trace"]==1):
                    print("Agent;"+str(self.posX)+";"+str(self.posY))
                return False
        else:
            newPos=self.sma.envir.torus(self.posX+self.pasX, self.posY+self.pasY)
            wall=newPos[0]!=self.posX+self.pasX or newPos[1]!=self.posY+self.pasY
            offsetX=self.pasX
            offsetY=self.pasY
            if(self.posX+self.pasX!=newPos[0]):
                offsetX=newPos[0]-self.posX
            if(self.posY+self.pasY!=newPos[1]):
                offsetY=newPos[1]-self.posY

        if(c.p["torus"]==1):
            dest=self.sma.envir.getAgent(newPos[0],newPos[1])
        else:
            dest=self.sma.envir.getAgent(self.posX+self.pasX, self.posY+self.pasY)

        if(dest==None):
            if(wall):
                self.sma.envir.moveAgentCoord(self, newPos)
                this.sma.moveCircle(circle, offsetX, offsetY)
                return False
            self.move()
            return True
        elif(self!=dest):
            self.agentRebound(dest)
            self.sma.changeColor(self.circle)
            self.sma.changeColor(dest.circle)
            return False
        return True

    def move(self):
        self.sma.envir.moveAgent(self)

    def agentRebound(self,agent):
        selfX = self.pasX
        selfY = self.pasY
        self.pasX=agent.pasX
        self.pasY=agent.pasY
        agent.pasX = selfX
        agent.pasY = selfY
        if(c.p["trace"]==1):
            print("Agent;"+str(self.posX)+";"+str(self.posY))
            print("Agent;"+str(agent.posX)+";"+str(agent.posY))
