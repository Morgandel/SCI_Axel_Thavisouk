import config as c
from agent import Agent


class Wall(Agent):
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX,pPosY, pSMA)

    def decide(self):
        return False

    def type(self):
        return "wall"
