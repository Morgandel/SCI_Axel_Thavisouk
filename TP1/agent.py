from random import randint

class Agent:
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pPasX, pPasY, pEnvir):
        self.posX=pPosX
        self.posY=pPosY
        self.pasX=pPasX
        self.pasY=pPasY
        self.envir=pEnvir

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

    def setPoxY(self, pPosY):
        self.posY=pPosY
    
    def decide():
        dest=self.envir.getAgent(self.posX+self.pasX, self.posY+self.pasY)
        if(dest==None):
            print("t")

    def move():


        

