from agent import Agent
from environment import Environment
from random import randint,shuffle
from tkinter import *

class SMA:

    def __init__(self, pWidth, pHeight, pNbAgent,pCircleSize):
        self.circleSize=pCircleSize
        self.height=pHeight
        self.width = pWidth
        self.agentList = [Agent(randint(0,pWidth-1), randint(0,pHeight-1), randint(-1,1), randint(-1,1),None) for i in range (pNbAgent)]
        self.envi = Environment(pWidth, pHeight, self.agentList, pNbAgent, pCircleSize)
        for agent in self.agentList:
            agent.setEnvir(self.envi)
    
    def update(self,canvas1,window):
        for agent in self.agentList:
            print("decision")
            agent.decide()
            circle=agent.getCircle()
            canvas1.move(circle, agent.getPasX()*self.circleSize, agent.getPasY()*self.circleSize)
        window.after(1, self.update, canvas1, window)
    

    def run(self, turn):
        g_height = (self.height*self.circleSize)+1
        g_width = (self.width*self.circleSize)+1
        window = Tk()
        window.geometry("100x100")

        canvas1 = Canvas(window, height=g_height, width=g_width)
        canvas1.grid(row=0, column=0, sticky='w')
        for x in range(1,g_width+1, self.circleSize):
            canvas1.create_line(x, 1, x, g_width)
            canvas1.create_line(1, x, g_width, x)


        for agent in self.agentList:
            x = agent.getPosX()*self.circleSize
            y = agent.getPosY()*self.circleSize
            coord=[x, y, x+self.circleSize, y+self.circleSize]
            agent.setCircle(canvas1.create_oval(coord, outline="red", fill="red"))

        self.update(canvas1, window)

        window.mainloop ()

       
        for i in range(turn):
            self.agentList=shuffle(self.agentList)
            for elem in self.agentList:
                elem.decide()




