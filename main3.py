from wator import Wator
from motionPlanning import MotionPlanning
import config as c

if __name__ == '__main__':
    c.initialize('maze.json')
    instance=MotionPlanning()
    instance.run()
