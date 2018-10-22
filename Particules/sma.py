from Particules.particules import Particules
from Core.environment import Environment
from random import randint,shuffle,seed
from tkinter import *
from Core.display import Display
import Core.config as c
import numpy as np
from Core.smaCore import SMACore

class SMA(SMACore):

    def __init__(self):
        if(c.p["seed"]!=None):
            seed(c.p["seed"])
        self.agentList = np.array([Particules(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1), randint(-1,1), randint(-1,1),self) for i in range (c.p["nbParticules"])])
        self.envir = Environment()
        self.envir.addAgents(self.agentList,c.p["nbParticules"])
        self.grid=None
        self.turnCpt=0

    def update(self,turn):
        if(c.p["trace"]==1):
            print("Turn "+str(self.turnCpt))
            self.turnCpt+=1
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
                self.grid.moveCircleCoords(agent.circle, agent.posX, agent.posY)
        if(turn!=-1):
            turn=turn-1
        if(turn!=0):
            self.grid.window.after(c.p["refresh"], self.update,turn)

    def run(self):
        self.grid = Display()
        self.grid.drawCircles(self.agentList, "red")
        if(c.p["nbTicks"]<=0):
            self.update(-1)
        else:
            self.update(c.p["nbTicks"])

        self.grid.mainloop()
