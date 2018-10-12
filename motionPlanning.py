from random import randint,shuffle,seed
from tkinter import *
from display import Display
import config as c

class MotionPlanning:

    def __init__(self):
        if(c.p["seed"]!=None):
            seed(c.p["seed"])
        self.agentList = np.array([Particules(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1), randint(-1,1), randint(-1,1),self) for i in range (c.p["nbParticules"])])
        self.envir = Environment(self.agentList)
        self.grid=None

    def update(self,turn):
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
                self.grid.moveCircle(agent.circle, agent.pasX, agent.pasY)
        if(turn!=-1):
            turn=turn-1
        if(turn!=0):
            self.grid.window.after(c.p["refresh"], self.update,turn)

    def changeColor(self,circle):
        self.grid.changeColor(circle)

    def moveCircle(self,circle,offsetX,offsetY):
        self.grid.moveCircle(circle,offsetX,offsetY)

    def run(self):
        self.grid = Display(self.agentList)
        if(c.p["nbTicks"]<=0):
            self.update(-1)
        else:
            self.update(c.p["nbTicks"])

        self.grid.mainloop()
