from sma import SMA
from environment import Environment

if __name__ == '__main__':
    height=5
    width=5
    nbAgents=1
    turn=1
    instance=SMA(width, height, nbAgents)
    instance.run(turn)
