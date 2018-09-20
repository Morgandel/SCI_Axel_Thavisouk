from agent import Agent
from environment import Environment
from random import randint,shuffle
from tkinter import *

class SMA:

    def __init__(self, pWidth, pHeight, pNbAgent):
        self.agentList = [Agent(randint(0,pSize-1), randint(0,pSize-1), randint(-1,-1), randint(-1,1), self) for i in range (pNbAgent)]
        self.envi = Environment(pWidth, pHeight, self.agentList, pNbAgent)

    def run(self, turn):
        for i in range(turn
            self.agentList=shuffle(self.agentList)
            for elem in self.agentList:
                elem.decide()



