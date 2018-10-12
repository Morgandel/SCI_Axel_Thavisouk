from wator import Wator
from watorEnvi import WatorEnvi
import config as c

if __name__ == '__main__':
    c.initializeWator()
    instance=Wator()
    instance.run()
