from Core.environment import Environment
from random import randint,shuffle,seed
from tkinter import *
from Core.display import Display
import Core.config as c
import numpy as np

class SMACore:
    '''
    Le classe SMACore permet la liaison entre l'affichage et les agents
    '''
    def __init__(self):
        self.circles=dict()
        grid=None


    '''
    turn: le nombre de tour restant. A mettre à -1 si infini
    Méthode abstraite qui est appellée à chaque tour
    '''
    def update(self,turn):
        pass

    '''
    agent: l'agent pour qui le cercle associé doit changerr de couleur
    color: la nouvelle couleur de cet agent
    Permet de changer la couleurs d'un cercle d'un agent
    '''
    def changeColor(self,agent,color):
        self.grid.changeColor(self.circles[agent],color)

    '''
    agentList: une liste d'agent pour qui un cercle doit être créé
    color: la couleur de ces cercles
    Crée des cercles pour tout les agent passé en paramètre
    '''
    def initializeCircles(self,agentList,color):
        for agent in agentList:
            x = agent.posX*c.p["boxSize"]
            y = agent.posY*c.p["boxSize"]
            self.circles[agent]=self.grid.drawCircle(x,y,color)

    '''
    agent: un agent pour qui un cercle doit être créé
    color: la couleur
    Crée un cercles l'agent
    '''
    def addCircle(self,agent,color):
        x = agent.posX*c.p["boxSize"]
        y = agent.posY*c.p["boxSize"]
        self.circles[agent]=self.grid.drawCircle(x,y,color)

    '''
    Fonction qui est appelée du main afin d'initialiser la grille et le sma
    '''
    def run(self):
        pass
