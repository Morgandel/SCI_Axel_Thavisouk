from particules import Particules
from random import randint,shuffle,seed
from tkinter import *
import config as c

class Display:

    def __init__(self):
        self.g_height = (c.p["gridSizeY"]*c.p["boxSize"])+1
        self.g_width = (c.p["gridSizeX"]*c.p["boxSize"])+1
        self.window = Tk()
        self.window.geometry(str(self.g_width)+"x"+str(self.g_height))

        self.canvas = Canvas(self.window, height=self.g_height, width=self.g_width)
        self.canvas.grid(row=0, column=0, sticky='w')
        self.drawGrid()

    def drawGrid(self):
        if(c.p["grid"]==1):
            for x in range(1,self.g_width+1, c.p["boxSize"]):
                self.canvas.create_line(x, 1, x, self.g_width)
                self.canvas.create_line(1, x, self.g_height, x)
        else:
            self.canvas.create_line(1, 1, 1, self.g_height)
            self.canvas.create_line(1, 1, self.g_width, 1)
            self.canvas.create_line(self.g_width,self.g_height,1,self.g_height)
            self.canvas.create_line(self.g_width,self.g_height,self.g_width,1)

    def drawCircles(self,agentList,color):
        for agent in agentList:
            x = agent.posX*c.p["boxSize"]
            y = agent.posY*c.p["boxSize"]
            agent.circle = self.canvas.create_oval(x, y, x+c.p["boxSize"], y+c.p["boxSize"], outline=color, fill=color)

    def drawRectangles(self,agentList,color):
        for agent in agentList:
            x = agent.posX*c.p["boxSize"]
            y = agent.posY*c.p["boxSize"]
            agent.circle = self.canvas.create_rectangle(x, y, x+c.p["boxSize"], y+c.p["boxSize"], outline=color, fill=color)

    def drawCircle(self,agent,color):
        x = agent.posX*c.p["boxSize"]
        y = agent.posY*c.p["boxSize"]
        agent.circle = self.canvas.create_oval([x, y, x+c.p["boxSize"], y+c.p["boxSize"]], outline=color, fill=color)
    def changeColor(self,circle,color):
        self.canvas.itemconfigure(circle,outline=color, fill=color)

    def moveCircle(self,circle,offsetX,offsetY):
        self.canvas.move(circle, offsetX*c.p["boxSize"], offsetY*c.p["boxSize"])

    def moveCircleCoords(self,circle, posX, posY):
        x = posX*c.p["boxSize"]
        y = posY*c.p["boxSize"]
        self.canvas.coords(circle,x, y, x+c.p["boxSize"], y+c.p["boxSize"])

    def removeCircle(self,circle):
        self.canvas.delete(circle)

    def mainloop(self):
        self.window.mainloop()

    def listen(self,f):
        self.window.bind('<KeyPress>', f)
