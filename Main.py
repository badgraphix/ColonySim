# Kevin Dunn, add names
# CSC 305
# Colony Sim Game: Main
# 4/15/2019

import sys
from Display import *
import Config
import Building
import Unit
import time
actors = None
buildings = None

def main():
    pygame.init()

    Main.actors = Unit.Actor(Config.actors, Config.actorsx, Config.actorsy)
    Main.buildings = Building.Buildings(Config.actors, Config.actorsx, Config.actorsy)

    if Config.loadMap == 1:
        with open("Saves/Save.txt", "rb") as fp:
            Config.gameMap = pickle.load(fp)

    while Config.stop == 0:  # Main loop, ends if Config.stop is changed

        # take keyboard input
        if Config.gameMode==0:
            inputEditor()
        else:
            inputGame()

        if Config.pause == 0:Main.actors.allAct()

        drawAll()  # call the draw map function
        pygame.display.update()  # update map once updated

        # game time
        tempTime = time.time() * 1000
        while tempTime < Config.frameTime + 90:
            tempTime = time.time() * 1000
            pygame.time.wait(1)  # pause for a short while
        Config.frameTime = tempTime

    # If loops exits
    pygame.quit()
    sys.exit()


# if python says run, let's run! Taken from pygame example code
if __name__ == '__main__':
    main()
