import Core.config as c
from Core.agent import Agent


class Winner(Agent):
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX,pPosY, pSMA)
        self.dead=False

    def decide(self):
        if(self.life==0):
            self.dead=True
        return False

    def type(self):
        return "winner"
