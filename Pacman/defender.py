import Core.config as c
from Core.agent import Agent


class Defender(Agent):
    "Extension de Agent pour l'agent Defender"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX,pPosY, pSMA)
        self.life=c.p["defenderLife"]
        self.dead=False

    def decide(self):
        self.life-=1
        if(self.life==0):
            self.dead=True
        return False

    def type(self):
        return "defender"
