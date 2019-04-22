#Cam Brady, John Bertsch, Kevin Dunn, Cameron Burt
#CSC 305
#Colony Sim Game: buildings
#3/25/2019

import pickle
import pygame
from pygame.locals import *
import sys, random, os.path
import math
from Tile import *
import Config


class Buildings:
    data=[]
    totalBuildingss=0
    def __init__(self, num,x,y):
        self.totalBuildings=num
        for temp in range(0,num):
            buildingTemp=building(random.randint(0,x),random.randint(0,y),temp,1)
            self.data.append(buildingTemp)

    def allAct(self):
        for temp in range(0,self.totalBuildings):
            self.data[temp].perform()


class building:
    # Coordinates
    xPos = 0
    yPos = 0
    buildingType = 0
    # building type. Represented as an integer that is used #
    #as the parameter for a getbuildingData() function.
    # 1 = home base, 2 = farm, 3 = water tower, 4 = stonestorage, 5 = woodstrage
    # Inventory. Each entry in the array represents the quantity of that respective resource type. A building can only hold ONE type of resource at a time, so keep this in mind while developing.
    inventory = [0, 0, 0, 0, 0, 0]

    def __init__(self, x, y, buildingID, buildtype):
        self.buildingID = buildingID
        self.setXPos(x)
        self.setbuildingType = buildtype
        self.setYPos(y)
    def setInventory(self, resourceType, quantity):
        if (validateinventorytype(resourceType) == True) :
            self.inventory[resourceType] += quantity
    def getInventory(self):
        return self.inventory

    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos

    def getTargetXPos(self):
        return self.targetXPos

    def getTargetYPos(self):
        return self.targetYPos

    def getCurrentTile(self):
        # TODO: Create getTile(x, y) in gMap.
        return Config.gameMap.getTile(self.getXPos(), self.getYPos())  # .tileType (between 0 and 4)

    def setXPos(self, val):
        self.xPos = val

    def setYPos(self, val):
        self.yPos = val

    def assignbuildingtype(buildtype, self):
        buildingType = buildtype


# 1 = home base, 2 = farm, 3 = water tower, 4 = stonestorage, 5 = woodstorage
# figure out what the keys are (wheat = what? etc)
    def validateinventorytype(self, resourceType):
        if self.buildingType == 1:
            return True
        elif (self.buildingType == resourceType):
            return True
        else:
            return False
