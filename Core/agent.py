import Core.config as c


class Agent:
    "Classe abstraite d'un agent"
    def __init__(self, pPosX, pPosY, pSMA):
        self.posX=pPosX
        self.posY=pPosY
        self.sma=pSMA
        self.circle=None

    def decide(self):
        pass
