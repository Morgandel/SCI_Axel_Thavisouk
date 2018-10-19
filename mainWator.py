from Wator.wator import Wator
from Wator.watorEnvi import WatorEnvi
import Core.config as c

if __name__ == '__main__':
    c.initialize("Wator/wator.json")
    instance=Wator()
    instance.run()
