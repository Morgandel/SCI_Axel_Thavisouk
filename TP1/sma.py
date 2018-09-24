from agent import Agent
from environment import Environment
from random import randint,shuffle,seed
from tkinter import *
import config as c

class SMA:

    def __init__(self):
        if(c.p["seed"]!=None):
            seed(c.p["seed"])
        self.agentList = [Agent(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1), randint(-1,1), randint(-1,1),None) for i in range (c.p["nbParticules"])]
        self.envi = Environment(self.agentList)
        for agent in self.agentList:
            agent.setEnvir(self.envi)

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
            lastPos = agent.getPos()
            if(agent.decide(self.canvas1)):
                circle=agent.getCircle()
                self.canvas1.move(circle, agent.getPasX()*c.p["boxSize"], agent.getPasY()*c.p["boxSize"])
        if(turn!=-1):
            turn=turn-1
        if(turn!=0):
            self.window.after(c.p["refresh"], self.update,turn)


    def run(self):
        g_height = (c.p["gridSizeX"]*c.p["boxSize"])+1
        g_width = (c.p["gridSizeX"]*c.p["boxSize"])+1
        self.window = Tk()
        self.window.geometry(str(g_width)+"x"+str(g_height))

        self.canvas1 = Canvas(self.window, height=g_height, width=g_width)
        self.canvas1.grid(row=0, column=0, sticky='w')
        if(c.p["grid"]==1):
            for x in range(1,g_width+1, c.p["boxSize"]):
                self.canvas1.create_line(x, 1, x, g_width)
                self.canvas1.create_line(1, x, g_width, x)
        else:
            self.canvas1.create_line(1, 1, 1, g_height)
            self.canvas1.create_line(1, 1, g_width, 1)
            self.canvas1.create_line(g_width,g_height,1,g_height)
            self.canvas1.create_line(g_width,g_height,g_width,1)


        for agent in self.agentList:
            x = agent.getPosX()*c.p["boxSize"]
            y = agent.getPosY()*c.p["boxSize"]
            coord=[x, y, x+c.p["boxSize"], y+c.p["boxSize"]]
            agent.setCircle(self.canvas1.create_oval(coord, outline="red", fill="red"))

        if(c.p["nbTicks"]<=0):
            self.update(-1)
        else:
            self.update(c.p["nbTicks"])


        self.window.mainloop ()
