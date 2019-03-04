#Kevin Dunn, add names
#CSC 305
#Colony Sim Game: Input
#2/22/2019

import pickle
import pygame
from pygame.locals import *
import sys, random, os.path
import math
from Tile import *
from Map import *
import Main
import Config


def inputEditor():
    
    pygame.event.pump()
    keypress=pygame.key.get_pressed()

    if pygame.event.peek(QUIT):
        pygame.quit()
        sys.exit()
    
    Config.offsetX-=(keypress[K_RIGHT]-keypress[K_LEFT])*(32//Config.tileSize+1)#arrow keys are used to pan around the world
    Config.offsetY-=(keypress[K_DOWN]-keypress[K_UP])*(32//Config.tileSize+1)#^^
    Config.dotX-=keypress[K_a]-keypress[K_d]#wasd are used to move the cursor around, the black tile
    Config.dotY-=keypress[K_w]-keypress[K_s]#^^

        #here the number keys 1-4 can be pressed while the cursor is on the map, and it will assign a new type to that tile
    if keypress[K_1]:
        for tempX in range(-Config.brushSize,Config.brushSize+1):
            for tempY in range(-Config.brushSize,Config.brushSize+1):
                if Config.brushType==0:
                    if Config.loopMap==1 or Config.dotY+tempY>=0 and Config.dotY+tempY<Config.gameMap.ySize and Config.dotX+tempX>=0 and Config.dotX+tempX<Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX+tempX)%Config.gameMap.xSize,(Config.dotY+tempY)%Config.gameMap.ySize, 0)
                elif Config.brushType==1:
                    if (Config.loopMap==1 and abs(tempX)+abs(tempY)<=Config.brushSize) or Config.dotY+tempY>=0 and Config.dotY+tempY<Config.gameMap.ySize and Config.dotX+tempX>=0 and Config.dotX+tempX<Config.gameMap.xSize and abs(tempX)+abs(tempY)<=Config.brushSize:
                        Config.gameMap.setColor((Config.dotX+tempX)%Config.gameMap.xSize,(Config.dotY+tempY)%Config.gameMap.ySize, 0)
                elif Config.brushType==2:
                    if (Config.loopMap==1 and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=Config.brushSize) or Config.dotY+tempY>=0 and Config.dotY+tempY<Config.gameMap.ySize and Config.dotX+tempX>=0 and Config.dotX+tempX<Config.gameMap.xSize and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=Config.brushSize:
                        Config.gameMap.setColor((Config.dotX+tempX)%Config.gameMap.xSize,(Config.dotY+tempY)%Config.gameMap.ySize, 0)
    if keypress[K_2]:
        for tempX in range(-Config.brushSize,Config.brushSize+1):
            for tempY in range(-Config.brushSize,Config.brushSize+1):
                if Config.brushType==0:
                    if Config.loopMap==1 or Config.dotY+tempY>=0 and Config.dotY+tempY<Config.gameMap.ySize and Config.dotX+tempX>=0 and Config.dotX+tempX<Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX+tempX)%Config.gameMap.xSize,(Config.dotY+tempY)%Config.gameMap.ySize, 1)
                elif Config.brushType==1:
                    if (Config.loopMap==1 and abs(tempX)+abs(tempY)<=Config.brushSize) or Config.dotY+tempY>=0 and Config.dotY+tempY<Config.gameMap.ySize and Config.dotX+tempX>=0 and Config.dotX+tempX<Config.gameMap.xSize and abs(tempX)+abs(tempY)<=Config.brushSize:
                        Config.gameMap.setColor((Config.dotX+tempX)%Config.gameMap.xSize,(Config.dotY+tempY)%Config.gameMap.ySize, 1)
                elif Config.brushType==2:
                    if (Config.loopMap==1 and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=Config.brushSize) or Config.dotY+tempY>=0 and Config.dotY+tempY<Config.gameMap.ySize and Config.dotX+tempX>=0 and Config.dotX+tempX<Config.gameMap.xSize and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=Config.brushSize:
                        Config.gameMap.setColor((Config.dotX+tempX)%Config.gameMap.xSize,(Config.dotY+tempY)%Config.gameMap.ySize, 1)
    if keypress[K_3]:
        for tempX in range(-Config.brushSize,Config.brushSize+1):
            for tempY in range(-Config.brushSize,Config.brushSize+1):
                if Config.brushType==0:
                    if Config.loopMap==1 or Config.dotY+tempY>=0 and Config.dotY+tempY<Config.gameMap.ySize and Config.dotX+tempX>=0 and Config.dotX+tempX<Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX+tempX)%Config.gameMap.xSize,(Config.dotY+tempY)%Config.gameMap.ySize, 2)
                elif Config.brushType==1:
                    if (Config.loopMap==1 and abs(tempX)+abs(tempY)<=Config.brushSize) or Config.dotY+tempY>=0 and Config.dotY+tempY<Config.gameMap.ySize and Config.dotX+tempX>=0 and Config.dotX+tempX<Config.gameMap.xSize and abs(tempX)+abs(tempY)<=Config.brushSize:
                        Config.gameMap.setColor((Config.dotX+tempX)%Config.gameMap.xSize,(Config.dotY+tempY)%Config.gameMap.ySize, 2)
                elif Config.brushType==2:
                    if (Config.loopMap==1 and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=Config.brushSize) or Config.dotY+tempY>=0 and Config.dotY+tempY<Config.gameMap.ySize and Config.dotX+tempX>=0 and Config.dotX+tempX<Config.gameMap.xSize and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=Config.brushSize:
                        Config.gameMap.setColor((Config.dotX+tempX)%Config.gameMap.xSize,(Config.dotY+tempY)%Config.gameMap.ySize, 2)
    if keypress[K_4]:
        for tempX in range(-Config.brushSize,Config.brushSize+1):
            for tempY in range(-Config.brushSize,Config.brushSize+1):
                if Config.brushType==0:
                    if Config.loopMap==1 or Config.dotY+tempY>=0 and Config.dotY+tempY<Config.gameMap.ySize and Config.dotX+tempX>=0 and Config.dotX+tempX<Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX+tempX)%Config.gameMap.xSize,(Config.dotY+tempY)%Config.gameMap.ySize, 3)
                elif Config.brushType==1:
                    if (Config.loopMap==1 and abs(tempX)+abs(tempY)<=Config.brushSize) or Config.dotY+tempY>=0 and Config.dotY+tempY<Config.gameMap.ySize and Config.dotX+tempX>=0 and Config.dotX+tempX<Config.gameMap.xSize and abs(tempX)+abs(tempY)<=Config.brushSize:
                        Config.gameMap.setColor((Config.dotX+tempX)%Config.gameMap.xSize,(Config.dotY+tempY)%Config.gameMap.ySize, 3)
                elif Config.brushType==2:
                    if (Config.loopMap==1 and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=Config.brushSize) or Config.dotY+tempY>=0 and Config.dotY+tempY<Config.gameMap.ySize and Config.dotX+tempX>=0 and Config.dotX+tempX<Config.gameMap.xSize and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=Config.brushSize:
                        Config.gameMap.setColor((Config.dotX+tempX)%Config.gameMap.xSize,(Config.dotY+tempY)%Config.gameMap.ySize, 3)

        #adjusts the brush size
    if keypress[K_p]:
        Config.brushSize+=1
    if keypress[K_o] and Config.brushSize!=0:
        Config.brushSize-=1
    if keypress[K_i]:#change brush shape between square, diamond, and round
        if Config.brushType==0:
            Config.brushType=1
        elif Config.brushType==1:
            Config.brushType=2
        elif Config.brushType==2:
            Config.brushType=0


        #here the plus and minus(without shift so - and =) are used to zoom in and out by powers of 2, the zoom is centered on the middle of the screen, and the cursor stays put relative to the map not the window(on purpose)    
    if keypress[K_EQUALS] and Config.tileSize<=150:
        Config.tileSize=Config.tileSize*2
        Config.xlength=Config.xlength//2
        Config.ylength=Config.ylength//2
        Config.offsetX-=Config.xlength//2
        Config.offsetY-=Config.ylength//2
    if keypress[K_MINUS] and Config.tileSize>=5:
        Config.tileSize=Config.tileSize//2
        Config.xlength=Config.xlength*2
        Config.ylength=Config.ylength*2
        Config.offsetX+=Config.xlength//4
        Config.offsetY+=Config.ylength//4

        #'9' is used to save the game to a text file, '0' is used to load the save, to save long term, make sure to make a copy of this file elsewhere.
    if keypress[K_9]:
        Config.gameMap.save()
    if keypress[K_0]:
        Config.gameMap.load("Saves/save1.txt")
