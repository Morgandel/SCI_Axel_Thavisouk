from agent import Agent
from random import randint

class Environment:

    def __init__(self, pWidth, pHeight, pAgentList, pNbAgent):
        self.width=pWidth
        self.height=pHeight
        self.envir= [[None for x in range(pSize)] for y in range(pSize)]
        for i in range(pNbAgent):
            currentAgent=pAgentList[i]
            x,y=currentAgent.getPos()
            self.envir[y][x]=currentAgent

    def getAgent(self,x,y):
        return self.envir[x][y]
        
    def getEnvironment(self):
        return self.envir

    def moveAgent(self, agent):
        x,y = agent.getPos()
        pasX, pasY = agent.getPas()
        self.envir[y][x]=None
        self.envir[y+pasY][x+pasX]=agent

    

