from agent import Agent
import config as c
from random import randint

class Environment:

    def __init__(self, pAgentList):
        self.envir= [[None for x in range(c.p["gridSizeX"])] for y in range(c.p["gridSizeY"])]
        for i in range(c.p["nbParticules"]):
            currentAgent=pAgentList[i]
            x,y=currentAgent.getPos()
            while(self.envir[y][x]!=None):
                currentAgent.setPosX(randint(0,c.p["gridSizeX"]-1))
                currentAgent.setPosY(randint(0,c.p["gridSizeY"]-1))
                x,y=currentAgent.getPos()
            self.envir[y][x]=currentAgent

    def getAgent(self,x,y):
        return self.envir[y][x]

    def getEnvironment(self):
        return self.envir

    def moveAgent(self, agent):
        x,y = agent.getPos()
        pasX, pasY = agent.getPas()
        self.envir[y][x]=None
        self.envir[y+pasY][x+pasX]=agent
        agent.setPosX(x+pasX)
        agent.setPosY(y+pasY)

    def moveAgentCoord(self, agent, newPos):
        self.envir[agent.getPosY()][agent.getPosX()]=None
        self.envir[newPos[1]][newPos[0]]=agent
        agent.setPosX(newPos[0])
        agent.setPosY(newPos[1])

    def wallBounce(self, posX, posY):
        pas=[0,0]
        if(posX < 0):
            pas[0]=1
        elif(posX >= c.p["gridSizeX"]):
            pas[0]=-1
        if(posY < 0):
            pas[1]=1
        elif(posY >= c.p["gridSizeY"]):
            pas[1]=-1
        return pas

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
