import Core.config as c
from Core.agent import Agent


class Wall(Agent):
    "Extension de Agent pour l'agent Wall"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX, pPosY, pSMA)

    def decide(self):
        return False

    def type(self):
        return "wall"
