from agent import Agent
from random import randint

class Environment:

    def __init__(self, pWidth, pHeight, pAgentList, pNbAgent, pCircleSize):
        self.circleSize=pCircleSize
        self.width=pWidth
        self.height=pHeight
        self.envir= [[None for x in range(pWidth)] for y in range(pHeight)]
        for i in range(pNbAgent):
            currentAgent=pAgentList[i]
            x,y=currentAgent.getPos()
            self.envir[y][x]=currentAgent

    def getAgent(self,x,y):
        return self.envir[x][y]
        
    def getEnvironment(self):
        return self.envir

    def moveAgent(self, agent):
        print("on bouge l'agent")
        x,y = agent.getPos()
        pasX, pasY = agent.getPas()
        self.envir[y][x]=None
        self.envir[y+pasY][x+pasX]=agent
        agent.setPosX(x+pasX)
        agent.setPosY(y+pasY)
    
    def wallBounce(self, posX, posY):
        print("on rebondit sur un mur")
        pas=[0,0]
        print("x",posX,self.width)
        print("y",posY,self.height)
        if(posX <= 1):
            pas[0]=1
        elif(posX > self.width-1):
            pas[0]=-1
        if(posY <= 1):
            pas[1]=1
        elif(posY > self.height-1):
            pas[1]=-1
        return pas
    

