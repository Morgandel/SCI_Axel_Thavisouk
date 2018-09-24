from sma import SMA
from environment import Environment
import config as c

if __name__ == '__main__':
    c.initialize()
    print(c.width)
    instance=SMA()
    instance.run()
