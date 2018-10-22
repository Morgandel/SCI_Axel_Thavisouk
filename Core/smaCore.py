from Core.environment import Environment
from random import randint,shuffle,seed
from tkinter import *
from Core.display import Display
import Core.config as c
import numpy as np

class SMACore:

    def __init__(self):
        self.circles=dict()
        grid=None

    def update(self,turn):
        pass

    def changeColor(self,agent,color):
        self.grid.changeColor(self.circles[agent],color)

    def moveCircle(self,circle,offsetX,offsetY):
        self.grid.moveCircle(circle,offsetX,offsetY)

    def initializeCircles(self,agentList,color):
        for agent in agentList:
            x = agent.posX*c.p["boxSize"]
            y = agent.posY*c.p["boxSize"]
            self.circles[agent]=self.grid.drawCircle(x,y,color)

    def addCircle(self,agent,color):
        x = agent.posX*c.p["boxSize"]
        y = agent.posY*c.p["boxSize"]
        self.circles[agent]=self.grid.drawCircle(x,y,color)

    def run(self):
        pass
