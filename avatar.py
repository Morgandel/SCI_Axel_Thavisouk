import config as c
from agent import Agent
from pynput import keyboard
import numpy as np


class Avatar(Agent):
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX,pPosY, pSMA)
        self.dirX = 0
        self.dirY = 0

    def decide(self):
        pass

    def getNeibourgh(self):
        return np.array([(self.posX+1,self.posY),(self.posX-1,self.posY),(self.posX,self.posY+1),(self.posX,self.posY-1)])

    def updateDistanceGraph(self):
