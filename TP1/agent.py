import config as c

class Agent:
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pPasX, pPasY, pEnvir):
        self.posX=pPosX
        self.posY=pPosY
        self.pasX=pPasX
        self.pasY=pPasY
        self.envir=pEnvir
        self.circle=None
        self.rebound=0

    def getPos(self):
        return ((self.posX, self.posY))

    def getPas(self):
        return ((self.pasX, self.pasY))

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

    def getPasX(self):
        return self.pasX

    def getPasY(self):
        return self.pasY

    def setPasX(self,x):
        self.pasX=x

    def setPasY(self,y):
        self.pasY=y

    def setPosX(self, pPosX):
        self.posX=pPosX

    def setPosY(self, pPosY):
        self.posY=pPosY

    def setCircle(self, pCircle):
        self.circle=pCircle

    def getCircle(self):
        return self.circle

    def setEnvir(self, pEnvir):
        self.envir=pEnvir

    def getRebound(self):
        return self.rebound

    def incRebound(self):
        self.rebound=self.rebound+1
        if(self.rebound>9):
            self.rebound=0

    def isAgent(self):
        return True

    def decide(self,canvas):
        wall=False
        if(c.p["torus"]==0):
            bounds=self.envir.wallBounce(self.posX+self.pasX, self.posY+self.pasY)
            if(bounds[0] != 0 or bounds[1]!=0):
                if(bounds[0]!=0):
                    self.pasX=bounds[0]
                if(bounds[1]!=0):
                    self.pasY=bounds[1]
                if(c.p["trace"]==1):
                    print("Agent;"+str(self.posX)+";"+str(self.posY))
                return False
        else:
            newPos=self.envir.torus(self.posX+self.pasX, self.posY+self.pasY)
            wall=newPos[0]!=self.posX+self.pasX or newPos[1]!=self.posY+self.pasY
            offsetX=self.pasX
            offsetY=self.pasY
            if(self.posX+self.pasX!=newPos[0]):
                offsetX=newPos[0]-self.posX
            if(self.posY+self.pasY!=newPos[1]):
                offsetY=newPos[1]-self.posY

        if(c.p["torus"]==1):
            dest=self.envir.getAgent(newPos[0],newPos[1])
        else:
            dest=self.envir.getAgent(self.posX+self.pasX, self.posY+self.pasY)

        if(dest==None):
            if(wall):
                self.envir.moveAgentCoord(self, newPos)
                canvas.move(self.circle, offsetX*c.p["boxSize"], offsetY*c.p["boxSize"])
                return False
            self.move()
            return True
        elif(self!=dest):
            self.agentRebound(dest)
            self.changeColor(canvas)
            dest.changeColor(canvas)
            return False
        return True

    def move(self):
        self.envir.moveAgent(self)

    def agentRebound(self,agent):
        selfX = self.pasX
        selfY = self.pasY
        self.pasX=agent.getPasX()
        self.pasY=agent.getPasY()
        agent.setPasX(selfX)
        agent.setPasY(selfY)
        if(c.p["trace"]==1):
            print("Agent;"+str(self.posX)+";"+str(self.posY))
            print("Agent;"+str(agent.getPosX())+";"+str(agent.getPosY()))

    def changeColor(self,canvas):
        canvas.itemconfigure(self.circle,outline="grey", fill="grey")
