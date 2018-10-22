from Pacman.pacman import Pacman
import Core.config as c

if __name__ == '__main__':
    c.initialize('Pacman/maze.json')
    theSma = Pacman()
    theSma.run()
