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
            buildingTemp=building(random.randint(0,x),random.randint(0,y), temp)
            self.data.append(buildingTemp)
    def allAct(self):
        for temp in range(0,self.totalBuildings):
            self.data[temp].perform()





class building:
    # Coordinates
    xPos = 0
    yPos = 0
    #Target coordinates
    targetXPos = None
    targetYPos = None
    # Hunger. When it hits 0, the building dies.
    hitPoints = 100
    # building type. Represented as an integer that is used as the parameter for a getbuildingData() function.
    buildingType = 1
    # Inventory. Each entry in the array represents the quantity of that respective resource type. A building can only hold ONE type of resource at a time, so keep this in mind while developing.
    inventory = [0, 0, 0, 0, 0, 0]
    behavior = 0  # Each behavior type is currently stored as an int. 0 is standby mode, where the building will not perform any actions.
    targetTile = None  # Specifies where the building is heading towards. Does not always contain a value.
    priorityQueue = [1, 2, 3, 4, 5]

    def __init__(self, x, y, buildingID):
        self.buildingID = buildingID
        self.setXPos(x)
        self.setYPos(y)
        self.setInPriorityQueue(1,0)
    def setInventory(self, resourceType, quantity):
        self.inventory[resourceType] += quantity

    def setBehavior(self, behaviorType):
        self.behavior = behaviorType

    def setInPriorityQueue(self, startingIndex, newIndex):
        priorityQ = self.priorityQueue
        movedElement = priorityQ[startingIndex]
        priorityQ.insert(newIndex, movedElement)

    def getInventory(self):
        return self.inventory

    def getPriorityQueue(self):
        return self.priorityQueue

    def getBehavior(self):
        return self.behavior

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

    def setTargetXPos(self, val):
        self.targetXPos = val % Config.gameMap.xSize

    def setTargetYPos(self, val):
        self.targetYPos = val % Config.gameMap.ySize

    def translatePosition(self, x, y):
        currentTile = Config.gameMap.getTile(self.getXPos(), self.getYPos())
        currentTile.setStationedbuildingID(-1)
        self.xPos += x
        self.yPos += y
        newTile = Config.gameMap.getTile(self.getXPos(), self.getYPos())
        newTile.setStationedbuildingID(self.buildingID)

    def collectResource(self):

        # Farms resource on the tile the building is standing on. This is fired for all buildings on every tick, if it is possible for them to farm something.
        currentTile = self.getCurrentTile() # TODO: add a function in Tile that lets us remove a resource from it and return it here.
        resourceData = currentTile.collectResource(1) #TODO: add a function to Tile called collectResource() that returns .type (resource type) and .amount.
        self.inventory[resourceData[0]] = self.inventory[resourceData[0]] + resourceData[1] #Add that to building's inventory.
        #print("Farming resource. Quantity ", resourceData[1], " of type ", resourceData[0])


    def isbuildingAtTargetPos(self): #Returns true if building is at target position, returns false if it is not.
        return (self.getXPos() == self.getTargetXPos()) and (self.getYPos() == self.getTargetYPos())

    def perform(self):  # This is fired every tick. What action the building performs is dependent on its behavior, as well as external factors.
        if self.getPriorityQueue()[0] == 1:  # Continuously travel right
            self.translatePosition(1, 0)
        elif self.getPriorityQueue()[0] == 2:  # Travel to the nearest tile of type 2.
            if self.getTargetXPos() == None:
                self.findClosestTileOfType(2) #sets as target

            if self.isbuildingAtTargetPos() == True: #If you are on the target tile, start collecting resources!
                self.collectResource()
