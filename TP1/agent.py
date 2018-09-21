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

    def decide(self):
        bounds=self.envir.wallBounce(self.posX+self.pasX, self.posY+self.pasY)
        print("x:"+str(self.posX)+" y:"+str(self.posY)+" pasX:"+str(self.pasX)+" pasY:"+str(self.pasY))
        if(bounds[0] != 0 or bounds[1]!=0):
            if(bounds[0]!=0):
                print("On change le pas de x "+str(self.pasX)+" à "+str(bounds[0]))
                self.pasX=bounds[0]
            if(bounds[1]!=0):
                print("On change le pas de y "+str(self.pasY)+" à "+str(bounds[1]))
                self.pasY=bounds[1]
        else:
            dest=self.envir.getAgent(self.posX+self.pasX, self.posY+self.pasY)
            #if(dest==None):
            self.move()

    def move(self):
        self.envir.moveAgent(self)

        

