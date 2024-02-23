import time

from DUELink.DUELinkController import DUELinkController
from TikTakToe import Game

availablePort = DUELinkController.GetConnectionPort()
BrainPad = DUELinkController(availablePort)
neoPin = 0
neoCount = 256

if __name__ == "__main__":
    BrainPad.Neo.Clear()
    BrainPad.Neo.Show(neoPin, neoCount)
    while True:
        XOGame = Game(BrainPad, neoPin=neoPin, neoCount=neoCount)
        XOGame.do_game()
        time.sleep(3)
