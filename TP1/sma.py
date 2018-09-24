from agent import Agent
from environment import Environment
from random import randint,shuffle
from tkinter import *
import config as c

class SMA:

    def __init__(self):
        self.agentList = [Agent(randint(0,c.width-1), randint(0,c.height-1), randint(-1,1), randint(-1,1),None) for i in range (c.nbAgents)]
        self.envi = Environment(self.agentList)
        for agent in self.agentList:
            agent.setEnvir(self.envi)

    def update(self,turn):
        for agent in self.agentList:
            #print("decision")
            lastPos = agent.getPos()
            if(agent.decide(self.canvas1)):
                circle=agent.getCircle()
                self.canvas1.move(circle, agent.getPasX()*c.circleSize, agent.getPasY()*c.circleSize)
        turn=turn-1
        if(turn>0):
            self.window.after(33, self.updatei,turn)


    def run(self):
        g_height = (c.height*c.circleSize)+1
        g_width = (c.width*c.circleSize)+1
        self.window = Tk()
        self.window.geometry(str(g_width)+"x"+str(g_height))

        self.canvas1 = Canvas(self.window, height=g_height, width=g_width)
        self.canvas1.grid(row=0, column=0, sticky='w')
        for x in range(1,g_width+1, c.circleSize):
            self.canvas1.create_line(x, 1, x, g_width)
            self.canvas1.create_line(1, x, g_width, x)


        for agent in self.agentList:
            x = agent.getPosX()*c.circleSize
            y = agent.getPosY()*c.circleSize
            coord=[x, y, x+c.circleSize, y+c.circleSize]
            agent.setCircle(self.canvas1.create_oval(coord, outline="red", fill="red"))

        self.update(c.turn)

        self.window.mainloop ()
