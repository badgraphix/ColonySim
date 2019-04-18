# Kevin Dunn, add names
# CSC 305
# Colony Sim Game: Main
# 3/22/2019

import sys
import Unit
import building
import Config

from Display import *

actors = None
buildings = None

def main():
    pygame.init()

    Main.actors = Unit.Actor(Config.actors, Config.actorsx, Config.actorsy)
    Main.buildings = building.Actor(Config.actors, Config.actorsx, Config.actorsy)

    if Config.loadMap == 1:
        with open("Saves/Save.txt", "rb") as fp:
            Config.gameMap = pickle.load(fp)

    while Config.stop == 0:  # Main loop, ends if Config.stop is changed

        # take keyboard input
        inputEditor()

        if Config.pause == 0:
            Main.actors.allAct()

        drawAll()  # call the draw map function
        pygame.display.update()  # update map once updated

        # game time
        pygame.time.wait(Config.frameTime)  # pause for a short while

    # If loops exits
    pygame.quit()
    sys.exit()


# if python says run, let's run! Taken from pygame example code
if __name__ == '__main__':
    main()
