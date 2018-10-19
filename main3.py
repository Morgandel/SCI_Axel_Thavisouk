from Avatar.motionPlanning import MotionPlanning
import Core.config as c

if __name__ == '__main__':
    c.initialize('Avatar/maze.json')
    theSma = MotionPlanning()
    theSma.run()
