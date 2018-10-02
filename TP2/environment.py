from fish import Fish
from shark import Shark
import config as c
from random import randint

class Environment:

    def __init__(self):
        self.envir= [[None for x in range(c.p["gridSizeX"])] for y in range(c.p["gridSizeY"])]

    def addAgents(self, pAgentList,pNbAgent):
        for i in range(pNbAgent):
            currentAgent=pAgentList[i]
            x,y=(currentAgent.posX,currentAgent.posY)
            while(self.envir[y][x]!=None):
                currentAgent.posX=randint(0,c.p["gridSizeX"]-1)
                currentAgent.posY=randint(0,c.p["gridSizeY"]-1)
                x,y=(currentAgent.posX,currentAgent.posY)
            self.envir[y][x]=currentAgent

    def addAgent(self, pAgent):
        self.envir[pAgent.posY][pAgent.posX]=pAgent

    def getAgent(self,x,y):
        return self.envir[y][x]

    def removeAgent(self,agent):
        self.envir[agent.posY][agent.posX]=None

    def moveAgent(self, agent):
        x = agent.posX
        y = agent.posY
        pasX = agent.pasX
        pasY = agent.pasY
        self.envir[y][x]=None
        self.envir[y+pasY][x+pasX]=agent
        agent.posX = x+pasX
        agent.posY = y+pasY

    def moveAgentCoord(self, agent, newPos):
        self.envir[agent.posY][agent.posX]=None
        self.envir[newPos[1]][newPos[0]]=agent
        agent.posX = newPos[0]
        agent.posY = newPos[1]

    def findEmptySpace(self,agent):
        emptySpace=[]
        for i in range (-1,2):
            for j in range(-1,2):
                x=agent.posX+i
                y=agent.posY+j
                outOfBounds= x>=0 and x<c.p["gridSizeX"] and y>=0 and y<c.p["gridSizeY"]
                if(outOfBounds):
                    if(not self.envir[y][x]):
                        emptySpace.append((x,y))
        if(len(emptySpace)==0):
            return None
        return emptySpace[randint(0,len(emptySpace)-1)]

    def findFish(self,agent):
        fishFounds=[]
        for i in range(-1,2):
            for j in range(-1,2):
                x=agent.posX+i
                y=agent.posY+j
                outOfBounds= x>=0 and x<c.p["gridSizeX"] and y>=0 and y<c.p["gridSizeY"]
                if(outOfBounds):
                    if(self.envir[y][x]!=None):
                        if(self.envir[y][x].canBeEaten()):
                            fishFounds.append((x,y))
        if(len(fishFounds)==0):
            return None
        return fishFounds[randint(0,len(fishFounds)-1)]

    def torus(self, posX, posY):
        pos=[posX,posY]
        if(posX < 0):
            pos[0]=c.p["gridSizeX"]-1
        elif(posX >= c.p["gridSizeX"]):
            pos[0]=0
        if(posY < 0):
            pos[1]=c.p["gridSizeY"]-1
        elif(posY >= c.p["gridSizeY"]):
            pos[1]=0
        return pos
