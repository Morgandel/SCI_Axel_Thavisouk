from Wator.shark import Shark
from Wator.fish import Fish
from Wator.watorEnvi import WatorEnvi
from random import randint,shuffle,seed
from tkinter import *
from Core.display import Display
from Core.smaCore import SMACore
import numpy as np
import Core.config as c

class Wator(SMACore):
    "Implémentation de la classe abstraite SMACore pour réaliser Wator"
    def __init__(self):
        super().__init__()
        if(c.p["seed"]!=None):
            seed(c.p["seed"])
        self.sharkList = [Shark(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1), self) for i in range (c.p["nbShark"])]
        self.fishList = [Fish(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1), self) for i in range (c.p["nbFish"])]
        self.agentList=self.sharkList+self.fishList
        self.envir = WatorEnvi()
        self.envir.addAgents(self.sharkList,c.p["nbShark"])
        self.envir.addAgents(self.fishList,c.p["nbFish"])

    def update(self,turn):
        if(c.p["trace"]==1):
            print("%10d %10d %10d" % (turn,len(self.fishList), len(self.sharkList)))
        self.agentList=self.sharkList+self.fishList
        if(c.p["scheduling"]=="sequentiel"):
            agentIte=self.agentList
        elif(c.p["scheduling"]=="random"):
            agentIte=[]
            for i in range(len(self.agentList)):
                agentIte.append(self.agentList[randint(0,len(self.agentList)-1)])
        else:
            shuffle(self.agentList)
            agentIte=self.agentList

        for agent in agentIte:
            if(agent.decide()):
                self.grid.moveCircleCoords(self.circles[agent], agent.posX, agent.posY)
        for fish in self.fishList:
            if(fish.dead):
                self.fishList.remove(fish)
                self.envir.removeAgent(fish)
                self.grid.removeCircle(self.circles[fish])
                del self.circles[fish]
        for shark in self.sharkList:
            if(shark.dead):
                self.sharkList.remove(shark)
                self.envir.removeAgent(shark)
                self.grid.removeCircle(self.circles[shark])
                del self.circles[shark]

        if(turn!=-1):
            turn=turn+1
        if(turn!=c.p["nbTicks"] or turn==-1):
            self.grid.window.after(c.p["refresh"], self.update,turn)

    '''
    x: la coordonnée x du nouveau poisson
    y: la coordonnée y du nouveau poisson
    Fonction qui crée un nouveau poisson, le rajoute à sa liste, dans l'environement et qui crée le cercle pour l'afficher"
    '''
    def addFish(self,x,y):
        newFish=Fish(x, y, self)
        self.fishList.append(newFish)
        self.envir.addAgent(newFish)
        self.addCircle(newFish,c.p["newFishColor"])

    '''
    x: la coordonnée x du nouveau requin
    y: la coordonnée y du nouveau requin
    Fonction qui crée un nouveau requin, le rajoute à sa liste, dans l'environement et qui crée le cercle pour l'afficher"
    '''
    def addShark(self,x,y):
        newShark=Shark(x,y,self)
        self.sharkList.append(newShark)
        self.envir.addAgent(newShark)
        self.addCircle(newShark,c.p["newSharkColor"])

    '''
    agent: agent à supprimer
    Fonction qui permet de supprimer un agent
    '''
    def removeAgent(self,agent):
        agentType=agent.type()
        if(agentType=="fish"):
            self.fishList.remove(agent)
        else:
            self.sharkList.remove(agent)
        self.grid.removeCircle(self.circles[agent])
        self.envir.removeAgent(agent)
        del self.circles[agent]

    def run(self):
        self.grid = Display()
        self.initializeCircles(self.fishList, c.p["fishColor"])
        self.initializeCircles(self.sharkList, c.p["sharkColor"])
        if(c.p["nbTicks"]<=0):
            self.update(-1)
        else:
            self.update(0)

        self.grid.mainloop()
