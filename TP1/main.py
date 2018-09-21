from sma import SMA
from environment import Environment

if __name__ == '__main__':
    height=100
    width=100
    circleSize=10
    nbAgents=1000
    turn=1
    instance=SMA(width, height, nbAgents, circleSize)
    instance.run(turn)
