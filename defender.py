import config as c
from agent import Agent
from pynput import keyboard


class Defender(Agent):
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pSMA):
        super().__init__(pPosX,pPosY, pSMA)
        self.life=c.p["DefenderLife"]
        self.dead=False

    def decide(self):
        self.life-=1
        if(self.life==0):
            self.dead=True
        return False

    def type(self):
        return "defender"
