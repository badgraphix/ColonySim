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
            newTile=tile(total%5,0,0,0,0)#oh, by default, the map populates with all tile types alternating.
            self.data.append(newTile)

    def load(self, filename):
        with open(filename) as file:
            currentString = file.readline()
            self.xSize = int(currentString)
            currentString = file.readline()
            self.ySize = int(currentString)
            currentString = file.readline()
            self.data.clear()
            while(currentString):
                tileData = currentString.split()
                newTile = tile(int(tileData[0]), int(tileData[1]), int(tileData[2]), int(tileData[3]), int(tileData[4]))
                self.data.append(newTile)
                currentString = file.readline()
                               
    def getColor(self, xInd,yInd):
        return self.data[yInd*self.xSize+xInd].color()
    def setColor(self, xInd,yInd,num):
        return self.data[yInd*self.xSize+xInd].setType(num)

    def save(self, filename="Saves/save1.txt"):
        with open(filename, 'w') as file:
            file.seek(0)
            file.truncate()
            
            file.write(str(self.xSize) + '\n')
            file.write(str(self.ySize) + '\n')
            total = 0
            
            for tile in self.data:
                total += 1
                file.write(str(tile.tileType) + ' ' + str(tile.numWood) + ' ' + str(tile.numWater) + ' ' + str(tile.numFood) + ' ' + str(tile.traversable)+ '\n')

            print(total)
            print(len(self.data))
