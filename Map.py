#Kevin Dunn
#CSC 305
#Colony Sim Game: Map
#2/22/2019

import pickle
import pygame
from pygame.locals import *
import sys, random, os.path
import math
from Tile import *

class gMap:#class for map, comtains size information, and a list of all tiles within the map, can be saved in game and loaded
    xSize=2#default x,y size of class, not used when run
    ySize=2
    data=[]#data holds the tiles in a single list, but the setters and getters use x,y adressing, the rest of this class seems self explanatory
    def __init__(self, x, y):
        self.xSize=x
        self.ySize=y
        self.data= []
        for total in range(0,self.xSize*self.ySize):
            newTile=tile(total%5,0,0,0,0,0)#oh, by default, the map populates with all tile types alternating.
            self.data.append(newTile)
    def getColor(self, xInd,yInd):
        return self.data[(yInd%self.ySize)*self.xSize+(xInd%self.xSize)].color()
    def setColor(self, xInd,yInd,num):
        return self.data[(yInd%self.ySize)*self.xSize+(xInd%self.xSize)].setType(num)
    def getTile(self,xInd,yInd):
        return self.data[(yInd%self.ySize)*self.xSize+(xInd%self.xSize)]
