from shark import Shark
from fish import Fish
from environment import Environment
from random import randint,shuffle,seed
from tkinter import *
from display import Display
import numpy as np
import config as c

class Wator:

    def __init__(self):
        if(c.p["seed"]!=None):
            seed(c.p["seed"])
        self.sharkList = [Shark(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1), self) for i in range (c.p["nbShark"])]
        self.fishList = [Fish(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1), self) for i in range (c.p["nbFish"])]
        self.agentList=self.sharkList+self.fishList
        self.envir = Environment()
        self.envir.addAgents(self.sharkList,c.p["nbShark"])
        self.envir.addAgents(self.fishList,c.p["nbFish"])
        self.grid=None

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
                self.grid.moveCircleCoords(agent.circle, agent.posX, agent.posY)
        for fish in self.fishList:
            if(fish.dead):
                self.fishList.remove(fish)
                self.envir.removeAgent(fish)
                self.grid.removeCircle(fish.circle)
        for shark in self.sharkList:
            if(shark.dead):
                self.sharkList.remove(shark)
                self.envir.removeAgent(shark)
                self.grid.removeCircle(shark.circle)

        if(turn!=-1):
            turn=turn+1
        if(turn!=c.p["nbTicks"] or turn==-1):
            self.grid.window.after(c.p["refresh"], self.update,turn)

    def changeColor(self,circle):
        self.grid.changeColor(circle)

    def moveCircle(self,circle,offsetX,offsetY):
        self.grid.moveCircle(circle,offsetX,offsetY)

    def addFish(self,x,y):
        newFish=Fish(x, y, self)
        self.fishList.append(newFish)
        self.envir.addAgent(newFish)
        self.grid.drawCircle(newFish,"blue")

    def addShark(self,x,y):
        newShark=Shark(x,y,self)
        self.sharkList.append(newShark)
        self.envir.addAgent(newShark)
        self.grid.drawCircle(newShark,"red")

    def removeAgent(self,agent):
        if(agent.isFish()):
            self.fishList.remove(agent)
        else:
            self.sharkList.remove(agent)
        self.grid.removeCircle(agent.circle)
        self.envir.removeAgent(agent)

    def run(self):
        self.grid = Display()
        self.grid.drawCircles(self.fishList, "blue")
        self.grid.drawCircles(self.sharkList, "black")
        if(c.p["nbTicks"]<=0):
            self.update(-1)
        else:
            self.update(0)

        self.grid.mainloop()
