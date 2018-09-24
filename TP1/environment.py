from agent import Agent
from random import randint
import config as c

class Environment:

    def __init__(self, pAgentList):
        self.envir= [[None for x in range(c.width)] for y in range(c.height)]
        for i in range(c.nbAgents):
            currentAgent=pAgentList[i]
            x,y=currentAgent.getPos()
            self.envir[y][x]=currentAgent

    def getAgent(self,x,y):
        print(x,y,len(self.envir),len(self.envir[x]))
        return self.envir[x][y]

    def getEnvironment(self):
        return self.envir

    def moveAgent(self, agent):
        x,y = agent.getPos()
        pasX, pasY = agent.getPas()
        print("on bouge l'agent de ["+str(x)+","+str(y)+"] à ["+str(x+pasX)+","+str(y+pasY)+"]")
        self.envir[y][x]=None
        self.envir[y+pasY][x+pasX]=agent
        agent.setPosX(x+pasX)
        agent.setPosY(y+pasY)

    def wallBounce(self, posX, posY):
        pas=[0,0]
        if(posX < 0):
            print("rebond gauche")
            pas[0]=1
        elif(posX >= c.width):
            print("rebond droit")
            pas[0]=-1
        if(posY < 0):
            print("rebond haut")
            pas[1]=1
        elif(posY >= c.height):
            print("rebond bas")
            pas[1]=-1
        return pas
