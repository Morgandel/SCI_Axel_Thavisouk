import Core.config as c
from random import randint
import numpy as np

class Environment:
    "L'environement est la classe qui contient la grille et permet de situer les agents"
    def __init__(self):
        self.envir= np.array([[None for x in range(c.p["gridSizeX"])] for y in range(c.p["gridSizeY"])])

    '''
    pAgentList: la liste des agents
    pNbAgent: le nombre d'agents dans pAgentList
    Rajoute à l'environement les agents dans pAgentList
    '''
    def addAgents(self, pAgentList,pNbAgent):
        for i in range(pNbAgent):
            currentAgent=pAgentList[i]
            x,y=(currentAgent.posX,currentAgent.posY)
            while(self.envir[y][x]!=None):
                currentAgent.posX=randint(0,c.p["gridSizeX"]-1)
                currentAgent.posY=randint(0,c.p["gridSizeY"]-1)
                x,y=(currentAgent.posX,currentAgent.posY)
            self.envir[y][x]=currentAgent

    '''
    pAgent: l'agent à rajouter dans l'environement
    Permet de rajouter un agent à l'environement
    '''
    def addAgent(self, pAgent):
        x,y=(pAgent.posX,pAgent.posY)
        while(self.envir[y][x]!=None):
            pAgent.posX=randint(0,c.p["gridSizeX"]-1)
            pAgent.posY=randint(0,c.p["gridSizeY"]-1)
            x,y=(pAgent.posX,pAgent.posY)
        self.envir[y][x]=pAgent

    '''
    x: coordonnée x à récupérer
    y: coordonnée y à récupérer
    Renvoie ce qui est présent aux coordonnées x,y
    '''
    def getAgent(self,x,y):
        return self.envir[y][x]

    '''
    x: coordonnée x à supprimer
    y: coordonnée y à supprimer
    supprime ce qui est présent aux coordonnées x,y
    '''
    def removeAgent(self,agent):
        self.envir[agent.posY][agent.posX]=None

    '''
    agent: l'agent à bouger
    Permet à un agent de bouger selon un pax
    '''
    def moveAgent(self, agent):
        x = agent.posX
        y = agent.posY
        pasX = agent.pasX
        pasY = agent.pasY
        self.envir[y][x]=None
        self.envir[y+pasY][x+pasX]=agent
        agent.posX = x+pasX
        agent.posY = y+pasY


    '''
    x: coordonnée x à vérifier
    y: coordonnée y à vérifier
    Renvoie Vrai si x,y est en dehors de la grille
    Faux sinon
    '''
    def isOutOfBound(self,x,y):
        if(x<0 or x>=c.p["gridSizeX"] or y<0 or y>=c.p["gridSizeY"]):
            return True
        return False

    '''
    agent: l'agent à bouger
    newPos: les nouvelles coordonnées de l'agent
    Fonction qui permet de bouger un agent
    '''
    def moveAgentCoord(self, agent, newPos):
        self.envir[agent.posY][agent.posX]=None
        self.envir[newPos[1]][newPos[0]]=agent
        agent.posX = newPos[0]
        agent.posY = newPos[1]


    '''
    posX: la coordonnée x à vérifier
    posY: la coordonnée y à vérifier
    Fonction qui permet de récupérer les coordonnée correspondante à un environement torique
    '''
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
