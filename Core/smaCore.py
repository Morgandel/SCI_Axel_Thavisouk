from Core.environment import Environment
from random import randint,shuffle,seed
from tkinter import *
from Core.display import Display
import Core.config as c
import numpy as np

class SMACore:

    def update(self,turn):
        pass

    def changeColor(self,circle,color):
        self.grid.changeColor(circle,color)

    def moveCircle(self,circle,offsetX,offsetY):
        self.grid.moveCircle(circle,offsetX,offsetY)

    def run(self):
        pass
