import config as c


class Agent:
    "L'agent c'est une bille"
    def __init__(self, pPosX, pPosY, pSMA):
        self.posX=pPosX
        self.posY=pPosY
        self.sma=pSMA
        self.circle=None

    def decide(self):
        pass
