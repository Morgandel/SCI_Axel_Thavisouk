from Avatar.pacman import Pacman
import Core.config as c

if __name__ == '__main__':
    c.initialize('Avatar/maze.json')
    theSma = Pacman()
    theSma.run()
