import Core.config as c


class Agent:
    "Classe abstraite d'un agent"
    def __init__(self, pPosX, pPosY, pSMA):
        self.posX=pPosX
        self.posY=pPosY
        self.sma=pSMA
        self.circle=None

    '''
    decide() est une fonction qui est disponibles pour tout les agents et qui permet de décider une action.
    Renvoie un booléen, Vrai si l'agent a bougé ou Faux sinon
    '''
    def decide(self):
        pass
