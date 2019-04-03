#Kevin Dunn, add names
#CSC 305
#Colony Sim Game: Main
#4/2/2019

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
import time
   

def main():
    
    pygame.init()
    
    if Config.loadMap==1:
        with open("Saves/Save.txt","rb") as fp:
                Config.gameMap=pickle.load(fp)

                
    
    while (Config.stop==0):#Main loop, ends if Config.stop is changed
        
        
        #take keyboard input
        inputEditor()

        if Config.pause==0:
            Config.actors.allAct()
        drawAll()#call the draw map function
        pygame.display.update()#update map once updated

        #game time
        tempTime=time.time()*1000
        while(tempTime<Config.frameTime+90):
            tempTime=time.time()*1000
            pygame.time.wait(1)#pause for a short while
        Config.frameTime=tempTime
        
    #If loops exits
    pygame.quit()
    sys.exit()

    
#if python says run, let's run! Taken from pygame example code
if __name__ == '__main__':
    main()
