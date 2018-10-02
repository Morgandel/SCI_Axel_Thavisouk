from wator import Wator
from environment import Environment
import config as c

if __name__ == '__main__':
    c.initialize()
    instance=Wator()
    instance.run()
