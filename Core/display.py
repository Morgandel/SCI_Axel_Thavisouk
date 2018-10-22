from random import randint,shuffle,seed
from tkinter import *
import Core.config as c

class Display:
    "Classe qui gére l'affichage de la grille 2D et de ses agents"
    def __init__(self):
        self.g_height = (c.p["gridSizeY"]*c.p["boxSize"])+1
        self.g_width = (c.p["gridSizeX"]*c.p["boxSize"])+1
        self.window = Tk()
        self.window.geometry(str(self.g_width)+"x"+str(self.g_height))

        self.canvas = Canvas(self.window, height=self.g_height, width=self.g_width)
        self.canvas.grid(row=0, column=0, sticky='w')
        self.drawGrid()

    '''
    Fonction qui permet de créer la grille
    '''
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

    def drawRectangles(self,agentList,color):
        for agent in agentList:
            x = agent.posX*c.p["boxSize"]
            y = agent.posY*c.p["boxSize"]
            agent.circle = self.canvas.create_rectangle(x, y, x+c.p["boxSize"], y+c.p["boxSize"], outline=color, fill=color)

    '''
    x: coordonnée x du cercle à créer
    y: coordonnée y du cercle à créer
    color: la couleur du cercle
    Fonction qui crée un cercle aux coordonnée donnée en paramètre et le renvoie
    '''
    def drawCircle(self,x,y,color):
        return self.canvas.create_oval([x, y, x+c.p["boxSize"], y+c.p["boxSize"]], outline=color, fill=color)

    '''
    circle: le cercle
    color: sa nouvelle couleur
    Change la couleur du cercle passé en paramètre
    '''
    def changeColor(self,circle,color):
        self.canvas.itemconfigure(circle,outline=color, fill=color)

    '''
    circle: le cercle à bouger
    posX: le x de la nouvelle position
    posY: le y de la nouvelle position
    Bouge un cercle aux coordonnées donnée
    '''
    def moveCircleCoords(self,circle, posX, posY):
        x = posX*c.p["boxSize"]
        y = posY*c.p["boxSize"]
        self.canvas.coords(circle,x, y, x+c.p["boxSize"], y+c.p["boxSize"])

    '''
    circle: le cercle
    Supprime le cercle donné en paramètre
    '''
    def removeCircle(self,circle):
        self.canvas.delete(circle)

    '''
    La boucle principale  de Tkinter pour pouvoir afficher
    '''
    def mainloop(self):
        self.window.mainloop()

    '''
    f: la fonction à appeller
    Permet d'écouter la pression d'une touche.
    à chaque pression, appelle la fonction f passée en paramètre
    '''
    def listen(self,f):
        self.window.bind('<KeyPress>', f)
