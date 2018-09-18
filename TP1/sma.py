from agent import Agent
from environment import Environment
from random import randint

class SMA:

    def __init__(self, pSize, pNbAgent):
        self.agentList = [Agent(randint(0,pSize-1), randint(0,pSize-1), randint(-1,-1), randint(-1,1)) for i in range (pNbAgent)]
        self.envi = Environment(pSize, self.agentList, pNbAgent)

    def run(self, turn):
        for i,j in enumerate(self.agentList):
            x,y=j.getPos()
            print(str(i)+" : ("+str(x)+","+str(y)+")")

        print("\n################################\n")
        for line in self.envi.getEnvironment():
            for elem in line:
                if not elem:
                    print(str(0), end="")
                else:
                    print(str(1), end="")
            print()


