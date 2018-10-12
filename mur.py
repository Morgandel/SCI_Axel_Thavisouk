import config as c
from agent import Agent
from pynput import keyboard


class Mur(Agent):
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX,pPosY, pSMA)

    def decide(self):
        pass
