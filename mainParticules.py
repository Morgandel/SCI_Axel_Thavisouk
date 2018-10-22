from Particules.sma import SMA
from Core.environment import Environment
import Core.config as c

if __name__ == '__main__':
    c.initialize("Particules/parameter.json")
    instance=SMA()
    instance.run()
