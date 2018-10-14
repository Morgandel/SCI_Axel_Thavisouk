from random import randint,shuffle,seed
from tkinter import *
from avatar import Avatar
from hunter import Hunter
from wall import Wall
from display import Display
from environment import Environment
import config as c
import numpy as np

class MotionPlanning:

    def __init__(self):
        if(c.p["seed"]!=None):
            seed(c.p["seed"])
        self.avatar=Avatar(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1),self)
        self.huntersList=[Hunter(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1),self) for i in range (c.p["nbHunter"])]
        self.wallsList=[Wall(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1),self) for i in range (c.p["nbWall"])]
        self.agentList=[self.avatar]+self.huntersList
        self.defender=Defender(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1),self)
        #self.agentList = np.array([Particules(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1), randint(-1,1), randint(-1,1),self) for i in range (c.p["nbParticules"])])
        self.envir = Environment()
        self.envir.addAgents([self.avatar],1)
        self.envir.addAgents(self.huntersList,c.p["nbHunter"])
        self.envir.addAgents(self.wallsList,c.p["nbWall"])
        self.grid=None
        self.distance=None

    def update(self,turn):
        self.dijkstra()
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
        if(self.defender.dead):
            if(self.avatar.defenderConsumed==4):
                self.envir.removeAgent(self.defender)
                self.grid.removeCircle(self.defender.circle)
            else:
                self.envir.moveAgentCoord(self.defender,[randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1)])
                self.grid.moveCircleCoords(agent.circle, agent.posX, agent.posY)
        if(not self.avatar.dead):
            if(turn!=-1):
                turn=turn-1
            if(turn!=0):
                self.grid.window.after(c.p["refresh"], self.update,turn)

    def changeColor(self,circle):
        self.grid.changeColor(circle)

    def moveCircle(self,circle,offsetX,offsetY):
        self.grid.moveCircle(circle,offsetX,offsetY)

    def getNeighbors(self,x,y):
        neighbors=[]
        if(x+1<c.p["gridSizeX"]):
            neighbors.append((x+1,y))
        if(x-1>=0):
            neighbors.append((x-1,y))
        if(y+1<c.p["gridSizeY"]):
            neighbors.append((x,y+1))
        if(y-1>=0):
            neighbors.append((x,y-1))
        return neighbors

    def getMinDistance(self,x,y):
        neighbors=self.getNeighbors(x,y)
        current=neighbors[0]
        minDis=self.distance[current[1]][current[0]]
        for e in neighbors[1:]:
            newDis=self.distance[e[1]][e[0]]
            agent=self.envir.getAgent(current[0],current[1])
            if(agent!=None and agent.type()=='wall'):
                current=e
                minDis=newDis
            elif(newDis!=-1 and minDis>self.distance[e[1]][e[0]]):
                current=e
                minDis=newDis
        return current

    def getMaxDistance(self,x,y):
        neighbors=self.getNeighbors(x,y)
        current=neighbors[0]
        maxDis=self.distance[current[1]][current[0]]
        for e in neighbors[1:]:
            newDis=self.distance[e[1]][e[0]]
            agent=self.envir.getAgent(current[0],current[1])
            if(agent!=None and agent.type()=='wall'):
                current=e
                maxDis=newDis
            elif(newDis!=-1 and maxDis<self.distance[e[1]][e[0]]):
                current=e
                maxDis=newDis
        return current


    def dijkstra(self):
        frontier = []
        frontier.append((self.avatar.posX,self.avatar.posY))
        distance = [[None for x in range(c.p["gridSizeX"])] for y in range (c.p["gridSizeY"])]
        distance[self.avatar.posY][self.avatar.posX] = 0
        for wall in self.wallsList:
            x=wall.posX
            y=wall.posY
            distance[y][x]=-1

        while len(frontier)!=0:
           current = frontier.pop(0)
           for next in self.getNeighbors(current[0],current[1]):
              if distance[next[1]][next[0]]==None:
                 frontier.append(next)
                 distance[next[1]][next[0]] = 1 + distance[current[1]][current[0]]
        self.distance=distance

    def run(self):
        self.grid = Display()
        self.grid.drawRectangles(self.wallsList, "brown")
        self.grid.drawCircles([self.avatar], "blue")
        self.grid.drawCircles(self.huntersList, "red")
        self.grid.listen(self.avatar.onPress)
        if(c.p["nbTicks"]<=0):
            self.update(-1)
        else:
            self.update(c.p["nbTicks"])

        self.grid.mainloop()
