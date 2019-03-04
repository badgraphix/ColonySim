#Kevin Dunn, add names
#CSC 305
#Colony Sim Game: Main
#2/22/2019

import pickle
import pygame
from pygame.locals import *
import sys, random, os.path
import math
from Tile import *
from Map import *
from Input import *
from Display import *
import Config
   

def main():
    
    pygame.init()
    
    if Config.loadMap==1:
        Config.gameMap.load("Saves/save1.txt")

                
    
    while (Config.stop==0):#Main loop, ends if Config.stop is changed
        
        
        #take keyboard input
        inputEditor()
        
        drawAll()#call the draw map function
        pygame.display.update()#update map once updated

        #game time
        pygame.time.wait(Config.frameTime)#pause for a short while 
        
    #If loops exits
    pygame.quit()
    sys.exit()

    
#if python says run, let's run! Taken from pygame example code
if __name__ == '__main__':
    main()
