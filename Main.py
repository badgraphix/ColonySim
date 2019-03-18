#Kevin Dunn, add names
#CSC 305
#Colony Sim Game: Main
#2/28/2019

import pickle
import pygame
from pygame.locals import *
import sys, random, os.path
import math
from Tile import *
from Map import *
from Unit import *
from Input import *
from Display import *
import Config
   

def main():
    
    pygame.init()
    
    if Config.loadMap==1:
        with open("Saves/Save.txt","rb") as fp:
                Config.gameMap=pickle.load(fp)

                
    
    while (Config.stop==0):#Main loop, ends if Config.stop is changed
        
        
        #take keyboard input
        inputEditor()
        Config.actors.allAct()
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
