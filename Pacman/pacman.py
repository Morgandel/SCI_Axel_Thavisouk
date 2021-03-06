from random import randint,shuffle,seed
from tkinter import *
from Pacman.avatar import Avatar
from Pacman.hunter import Hunter
from Pacman.winner import Winner
from Pacman.wall import Wall
from Pacman.defender import Defender
from Core.display import Display
from Core.environment import Environment
from Core.smaCore import SMACore
import Core.config as c
import numpy as np

class Pacman(SMACore):

    def __init__(self):
        super().__init__()
        if(c.p["seed"]!=None):
            seed(c.p["seed"])
        self.avatar=Avatar(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1),self)
        self.huntersList=[Hunter(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1),self) for i in range (c.p["nbHunter"])]
        self.defender=Defender(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1),self)
        self.winner=None
        self.agentList=[self.avatar]+self.huntersList+[self.defender]
        self.envir = Environment()
        if(c.p["maze"]==0):
            self.wallsList=[Wall(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1),self) for i in range (int((c.p["gridSizeX"]*c.p["gridSizeY"])*c.p["nbWall"]))]
        else:
            self.wallsList=[]
            self.generateMaze()
        self.envir.addAgents(self.wallsList,len(self.wallsList))
        self.envir.addAgent(self.avatar)
        self.dijkstra()
        self.envir.addAgents(self.huntersList,c.p["nbHunter"])
        self.envir.addAgent(self.defender)
        self.distance=None
        self.stop=False

    '''
    Fonction qui génére un labyrinthe qui utilise le growing tree algorithm et qui crée les murs"
    '''
    def generateMaze(self):
        cells = []
        intitialCoord = (randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1))
        grid=[[0 for x in range(c.p["gridSizeX"])] for y in range(c.p["gridSizeY"])]
        cells.append(intitialCoord)
        while(len(cells)!=0):
            #i = randint(0,len(cells)-1)
            i=len(cells)-1
            x, y = cells.pop(i)
            neighbors=self.getNeighbors(x,y)
            shuffle(neighbors)
            for next in neighbors:
                nx, ny = next
                if(grid[ny][nx]==0):
                    grid[y][x]=next
                    grid[ny][nx]= next*-1
                    cells.append(next)
                    i=None

        for x in range(c.p["gridSizeX"]):
            for y in range(c.p["gridSizeY"]):
                if(len(grid[y][x])!=2):
                    self.wallsList.append(Wall(x,y,self))

        for i in range(int(len(self.wallsList)*c.p["erosionLabyrinthe"])):
            self.wallsList.pop(randint(0,len(self.wallsList)-1))


    def update(self,turn):
        if(not self.stop):
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
            if(self.defender.dead):
                if(self.avatar.defenderConsumed==4 and self.winner==None):
                    self.envir.removeAgent(self.defender)
                    self.grid.removeCircle(self.circles[self.defender])
                    del self.circles[self.defender]
                    self.winner=Winner(randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1),self)
                    self.envir.addAgent(self.winner)
                    self.addCircle(self.winner, "purple")
                elif(self.avatar.defenderConsumed<4):
                    self.defender.life=c.p["defenderLife"]
                    self.defender.dead=False
                    coord=[randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1)]
                    while(self.envir.getAgent(coord[0],coord[1])!=None):
                        coord=[randint(0,c.p["gridSizeX"]-1), randint(0,c.p["gridSizeY"]-1)]
                    self.envir.moveAgentCoord(self.defender,coord)
                    self.grid.moveCircleCoords(self.circles[self.defender], self.defender.posX, self.defender.posY)
                elif(self.avatar.defenderConsumed==5):
                    print("Gagné !")

            self.dijkstra()
            if(not self.avatar.dead and self.avatar.defenderConsumed<5):
                if(turn!=-1):
                    turn=turn-1
        if(turn!=0  and self.avatar.defenderConsumed<5 and not self.avatar.dead):
            self.grid.window.after(c.p["refresh"], self.update,turn)
        else:

            print("fin")

    '''
    Fonction qui retourne Vrai si l'avatar est en état invincible, Faux sinon
    '''
    def isInvincible(self):
        if(self.avatar.invincibility==0):
            return False
        return True

    '''
    x: la coordonnée x du centre
    y: la coordonnée y du centre
    Fonction qui retourne le voisinage de Von Neumann
    '''
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

    '''
    x: la coordonnée x du centre
    y: la coordonnée y du centre
    comp: le choix du minimum(min) ou du maximum(max)
    Retourne les coordonnée de la distance max ou min
    '''
    def getMinDistance(self,x,y, comp):
        neighbors=self.getNeighbors(x,y)
        current=neighbors[0]
        minDis=self.distance[current[1]][current[0]]
        for e in neighbors[1:]:
            newDis=self.distance[e[1]][e[0]]
            agent=self.envir.getAgent(current[0],current[1])
            if(agent!=None and agent.type()=='wall'):
                current=e
                minDis=newDis
            else:
                if(comp=='max'):
                    minmax=minDis>self.distance[e[1]][e[0]]
                else:
                    minmax=maxDis<self.distance[e[1]][e[0]]
                if(newDis!=-1 and minDis>self.distance[e[1]][e[0]]):
                    current=e
                    minDis=newDis
        return current

    '''
    Calcule la distance de chaque cases possible à partir de l'avatar
    '''
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

    '''
    Fonction qui gère les touches du clavier
    '''
    def onPress(self,e):
        key=e.keysym.lower()
        if(key=="up"):
            self.avatar.dirY=-1
            self.avatar.dirX=0
        elif(key=="down"):
            self.avatar.dirY=1
            self.avatar.dirX=0
        elif(key=="left"):
            self.avatar.dirY=0
            self.avatar.dirX=-1
        elif(key=="right"):
            self.avatar.dirY=0
            self.avatar.dirX=1
        elif(key=="z"):
            c.p["speedHunter"]+=1
            print("Vitesse du hunter à "+str(c.p["speedHunter"]))
        elif(key=="a"):
            if(c.p["speedHunter"]>1):
                c.p["speedHunter"]-=1
            print("Vitesse du hunter à "+str(c.p["speedHunter"]))
        elif(key=="w"):
            if(c.p["refresh"]>1):
                c.p["refresh"]-=1
            print("Vitesse du jeu à "+str(c.p["refresh"]))
        elif(key=="x"):
            c.p["refresh"]+=1
            print("Vitesse du jeu à "+str(c.p["refresh"]))
        elif(key=="o"):
            if(c.p["speedAvatar"]>1):
                c.p["speedAvatar"]-=1
            print("Vitesse de l'avatar à "+str(c.p["speedAvatar"]))
        elif(key=="p"):
            c.p["speedAvatar"]+=1
            print("Vitesse de l'avatar à "+str(c.p["speedAvatar"]))
        elif(key=="space"):
            self.stop=not self.stop
            print(self.stop)

    def run(self):
        self.grid = Display()
        self.grid.drawRectangles(self.wallsList, "brown")
        self.initializeCircles([self.avatar], "blue")
        self.initializeCircles([self.defender], "black")
        self.initializeCircles(self.huntersList, "red")
        self.grid.listen(self.onPress)
        if(c.p["nbTicks"]<=0):
            self.update(-1)
        else:
            self.update(c.p["nbTicks"])

        self.grid.mainloop()
