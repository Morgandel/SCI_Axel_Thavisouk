from agent import Agent
from random import randint

class Environment:

    def __init__(self, pSize, pAgentList, pNbAgent):
        self.envir= [[None for x in range(pSize)] for y in range(pSize)]
        for i in range(pNbAgent):
            currentAgent=pAgentList[i]
            x,y=currentAgent.getPos()
            self.envir[y][x]=currentAgent

    def getAgent(self,x,y):
        return self.envir[x][y]
        
    def getEnvironment(self):
        return self.envir

    

