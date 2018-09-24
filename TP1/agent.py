from random import randint

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
        bounds=self.envir.wallBounce(self.posX+self.pasX, self.posY+self.pasY)
        #print("x:"+str(self.posX)+" y:"+str(self.posY)+" pasX:"+str(self.pasX)+" pasY:"+str(self.pasY))
        if(bounds[0] != 0 or bounds[1]!=0):
            if(bounds[0]!=0):
                #print("On change le pas de x "+str(self.pasX)+" à "+str(bounds[0]))
                self.pasX=bounds[0]
            if(bounds[1]!=0):
                #print("On change le pas de y "+str(self.pasY)+" à "+str(bounds[1]))
                self.pasY=bounds[1]
            #self.printGrid()
            return False
        else:
            dest=self.envir.getAgent(self.posX+self.pasX, self.posY+self.pasY)
            if(dest==None):
                self.move()
                #self.printGrid()
                return True
            elif(self!=dest):
                #dest.incRebound()
                #self.incRebound()
                #print("Les agent s'échange leurs pas")
                self.agentRebound(dest)
                self.changeColor(canvas)
                dest.changeColor(canvas)
                #self.printGrid()
                return False

    def printGrid(self):
        for line in self.envir.getEnvironment():
            for elem in line:
                if (elem==None):
                    print("#",end="")
                else:
                    print(elem.getRebound(),end="")
            print()

    def move(self):
        self.envir.moveAgent(self)

    def agentRebound(self,agent):
        selfX = self.pasX
        selfY = self.pasY
        self.pasX=agent.getPasX()
        self.pasY=agent.getPasY()
        agent.setPasX(selfX)
        agent.setPasY(selfY)

    def changeColor(self,canvas):
        canvas.itemconfigure(self.circle,outline="grey", fill="grey")
        #canvas.itemconfigure(agent.getCircle,outline="grey", fill="grey")
