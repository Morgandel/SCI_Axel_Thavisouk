from Wator.fish import Fish
from Wator.shark import Shark
import Core.config as c
from random import randint
from Core.environment import Environment

class WatorEnvi(Environment):
    "WatorEnvi est une classe qui étends la classe environment car elle posséde des fonctions qui sont propres à Wator"
    def __init__(self):
        super().__init__()
        self.moore=[None]*8

    '''
    Récupére les cases vide dans le voisinage de moore de l'agent et retourne une coordonnée aléatoire dans ceux trouvées sous forme de tuple.
    Retourne None si aucune case vide n'a été trouvée
    '''
    def findEmptySpace(self,agent):
        nbSpace=0
        for i in range (-1,2):
            for j in range(-1,2):
                if((i!=0 or y!=0) and i!=j):
                    x=agent.posX+i
                    y=agent.posY+j
                    if(c.p["torus"]==0):
                        outOfBounds= x<0 or x>=c.p["gridSizeX"] or y<0 or y>=c.p["gridSizeY"]
                    else:
                        outOfBounds=False
                        x,y=self.torus(x,y)
                    if(not outOfBounds):
                        if(not self.envir[y][x]):
                            self.moore[nbSpace]=(x,y)
                            nbSpace=nbSpace+1
        if(nbSpace==0):
            return None
        return self.moore[randint(0,nbSpace-1)]


    '''
    Récupére les poissons dans le voisinage de moore de l'agent et retourne une coordonnée aléatoire dans ceux trouvées sous forme de tuple.
    Retourne None si aucune case vide n'a été trouvée
    '''
    def findFish(self,agent):
        nbFish=0
        for i in range(-1,2):
            for j in range(-1,2):
                if((i!=0 or y!=0) and i!=j):
                    x=agent.posX+i
                    y=agent.posY+j
                    if(c.p["torus"]==0):
                        outOfBounds= x<0 or x>=c.p["gridSizeX"] or y<0 or y>=c.p["gridSizeY"]
                    else:
                        outOfBounds=False
                        x,y=self.torus(x,y)
                    if(not outOfBounds):
                        if(self.envir[y][x]!=None):
                            if(self.envir[y][x].canBeEaten()):
                                self.moore[nbFish]=(x,y)
                                nbFish=nbFish+1
        if(nbFish==0):
            return None
        return self.moore[randint(0,nbFish-1)]

    '''
    Fonction qui retourne Vrai si l'agent passé en paramètre peut bouger dans le voisinage de moore
    retourne Faux sinon
    '''
    def agentsCanMove(self,agent):
        for i in range(-1,2):
            for j in range(-1,2):
                x=agent.posX+i
                y=agent.posY+j
                if(c.p["torus"]==0):
                    outOfBounds= x<0 or x>=c.p["gridSizeX"] or y<0 or y>=c.p["gridSizeY"]
                else:
                    outOfBounds=False
                    x,y=self.torus(x,y)
                if(not outOfBounds):
                    if(self.envir[y][x]!=None):
                        self.envir[y][x].canMove=True
