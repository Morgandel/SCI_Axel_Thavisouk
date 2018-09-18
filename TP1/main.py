from sma import SMA
from environment import Environment

if __name__ == '__main__':
    size=5
    nbAgents=1
    instance=SMA(size,nbAgents)
    instance.run()
