# Cam Brady, John Bertsch, Kevin Dunn
# CSC 305
# Colony Sim Game: Units
# 3/25/2019

import pickle
import pygame
from pygame.locals import *
import sys, random, os.path
import math
from Tile import *
import Config


class Actor:
    data = []
    totalActors = 0

    def __init__(self, num, x, y):
        self.totalActors = num
        for temp in range(0, num):
            unitTemp = unit(random.randint(0, x), random.randint(0, y), temp)
            self.data.append(unitTemp)

    def allAct(self):
        for temp in range(0, self.totalActors):
            self.data[temp].perform()


# focusTileTypes: when pathfinding, the unit will move towards the closest tile that is one of these type
# Strategies for priority queue
class FarmerStrategy:
    focusTileTypes = [4]  # Farmland


class WoodcutterStrategy:
    focusTileTypes = [1]  # Forest


class WaterCollectorStrategy:
    focusTileTypes = [2]  # Water


class StoneCollectorStrategy:
    focusTileTypes = [3]  # Mountain


class SoldierStrategy:
    focusTileTypes = None


class IdleStrategy:
    focusTileTypes = None


class unit:
    # Coordinates
    xPos = 0
    yPos = 0
    # Target coordinates
    targetXPos = None
    targetYPos = None
    hitPoints = 100
    # Hunger. When it hits 0, the unit will lose 1 HP every tick.
    hungerPoints = 100
    thirstPoints = 100
    # Unit type. Represented as an integer that is used as the parameter for a getUnitData() function.
    unitType = 1
    # Inventory. Each entry in the array represents the quantity of that respective resource type. A unit can only hold ONE type of resource at a time, so keep this in mind while developing.
    inventory = [0, 0, 0, 0, 0, 0]
    behavior = 0  # Each behavior type is currently stored as an int. 0 is standby mode, where the unit will not perform any actions.
    targetTile = None  # Specifies where the unit is heading towards. Does not always contain a value.
    priorityQueue = [FarmerStrategy, WoodcutterStrategy, WaterCollectorStrategy, StoneCollectorStrategy,
                     SoldierStrategy, IdleStrategy]

    def __init__(self, x, y, unitID):
        self.unitID = unitID
        self.setXPos(x)
        self.setYPos(y)
        # self.setInPriorityQueue(1,0)

    def setInventory(self, resourceType, quantity):
        self.inventory[resourceType] += quantity

    def getCurrentStrategy(self, index):  # Returns the current strategy at the specified index in the priority queue.
        return self.priorityQueue[index]

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

    def getHungerPoints(self):
        return self.hungerPoints

    def getThirstPoints(self):
        return self.thirstPoints

    def getHitPoints(self):
        return self.hitPoints

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
        return self.getTileOfPos(self.getXPos(), self.getYPos())  # .tileType (between 0 and 4)

    def getTileOfPos(self, x, y):
        return Config.gameMap.getTile(x, y)

    def setXPos(self, val):
        self.xPos = val

    def setYPos(self, val):
        self.yPos = val

    def setTargetXPos(self, val):
        self.targetXPos = val % Config.gameMap.xSize

    def setTargetYPos(self, val):
        self.targetYPos = val % Config.gameMap.ySize

    def setTargetPos(self, x, y):
        self.setTargetXPos(x);
        self.setTargetYPos(y);

    def isUnitAtTargetPos(self):
        return self.getXPos() == self.getTargetXPos() and self.getYPos() == self.getTargetYPos();

    def translatePosition(self, x, y):
        currentTile = Config.gameMap.getTile(self.getXPos(), self.getYPos())
        currentTile.setStationedUnitID(-1)
        self.xPos += x
        self.yPos += y
        newTile = Config.gameMap.getTile(self.getXPos(), self.getYPos())
        newTile.setStationedUnitID(self.unitID)

    def collectResource(self):
        # Farms resource on the tile the unit is standing on. This is fired for all units on every tick, if it is possible for them to farm something.
        currentTile = self.getCurrentTile()  # TODO: add a function in Tile that lets us remove a resource from it and return it here.
        resourceData = currentTile.collectResource(
            1)  # TODO: add a function to Tile called collectResource() that returns .type (resource type) and .amount.
        self.inventory[resourceData[0]] = self.inventory[resourceData[0]] + resourceData[
            1]  # Add that to unit's inventory.
        # print("Farming resource. Quantity ", resourceData[1], " of type ", resourceData[0])

    def findClosestTileOfType(self, destinationTileType):
        # TODO: Basically this whole function.
        targetTile = None
        tiles = Config.gameMap.data
        # print("TOTAL TILES " + str(len(tiles)))
        # Search for the nearest tile of tileType
        mapSizeX = Config.gameMap.xSize
        mapSizeY = Config.gameMap.ySize
        tileFound = False
        for x in range(0,
                       mapSizeX):  # This should check all tiles around the unit, then the ones around them, and so on, continuing farther out each time.
            for y in range(0, mapSizeY):
                if tileFound == False:
                    tile = Config.gameMap.getTile(x, y)  # Right now we are using a much dumber algorithm to test with.
                    tileType = tile.getType()
                    # print(tileType, " vs ", destinationTileType)
                    if tileType == destinationTileType:
                        # print("Setting to ", x, ",", y)
                        self.setTargetXPos(x)
                        self.setTargetYPos(y)
                        tileFound = True
                else:
                    break
            if tileFound == True:
                break

    def pathfind(tileType):
        path = []

        # calculate the distance from the current tile to the target
        def calcH(x, y, targX, targY):
            return sqrt((abs(targX - x) ** 2) + (abs(targY - y) ** 2))

        # x and y are (x,y) g is distance from start pos(can be used to limit runtime), patharris a list of directions generated with recursive backtracking
        def recSearch(x, y, g, patharr):
            # base cases to terminate recursion
            if (0):
                patharr.pop(-1)
                return  # case for if current tile its checking is impassable //get clarification\\

            if (g >= 50):
                return  # limiting run time

            if (x == targetXPos and y == targetYPos):  # if we found a way to the target pos
                return patharr

            # calc f score for the 4 surrounding tiles put to a list
            fscores = []
            fscores += (g + 1) + calcH(xPos + 1, yPos)  # [0] right
            fscores += (g + 1) + calcH(xPos - 1, yPos)  # [1] left
            fscores += (g + 1) + calcH(xPos, yPos + 1)  # [2] up
            fscores += (g + 1) + calcH(xPos, yPos - 1)  # [3] down

            checked = [0, 0, 0, 0]

            for j in range(0, 4):
                min = fscores[0]
                minind = 0
                for i in range(0, 4 - j):
                    if (fscores[i] < min and not checked[i]):
                        min = fscores
                        minind = 0
                checked[minind] = 1

                if (minind == 0):
                    recSearch(x + 1, y, g + 1, patharr.append(minind))

                if (minind == 1):
                    recSearch(x - 1, y, g + 1, patharr.append(minind))

                if (minind == 2):
                    recSearch(x, y + 1, g + 1, patharr.append(minind))

                if (minind == 3):
                    recSearch(x, y - 1, g + 1, patharr.append(minind))

        # get the target x and y values for each unit
        findClosestTileOfType(self, tileType)

        # xPos yPos denote unit position, targetXPos and targetYPos denote destination

    def isUnitAtTargetPos(self):  # Returns true if unit is at target position, returns false if it is not.
        return (self.getXPos() == self.getTargetXPos()) and (self.getYPos() == self.getTargetYPos())

    def perform(
            self):  # This is fired every tick. What action the unit performs is dependent on its behavior, as well as external factors.
        if self.getPriorityQueue()[0] == 1:  # Continuously travel right
            self.translatePosition(1, 0)
        elif self.getPriorityQueue()[0] == 2:  # Travel to the nearest tile of type 2.
            if self.getTargetXPos() == None:
                self.findClosestTileOfType(2)  # sets as target

            if self.isUnitAtTargetPos() == True:  # If you are on the target tile, start collecting resources!
                self.collectResource()

            # TODO: If one unit is heading toward a tile, should other units try heading somewhere else?
            # Pathfind to (self.targetXPos, self.targetYPos)

    def reduceHungerPoints(self):
        if self.hungerPoints - 1 < 0:  # starve
            self.hungerPoints = 0
        else:
            self.hungerPoints -= 1;
        if self.hungerPoints >= 80:  # Heal if the user is well-fed.
            self.hitPoints += 1
            if self.hitPoints > 100:  # Enforce the cap
                self.hitPoints = 100;

    def collectResource(self):
        # Farms resource on the tile the unit is standing on. This is fired for all units on every tick, if it is possible for them to farm something.
        currentTile = self.getCurrentTile()
        resourceData = currentTile.collectResource(1)
        self.inventory[resourceData[0]] = self.inventory[resourceData[0]] + resourceData[
            1]  # Add that to unit's inventory.
        print("Farming resource. Quantity ", resourceData[1], " of type ", resourceData[0])

    def findPosOfClosestTileOfType(self,
                                   destinationTileTypeArray):  # Returns closest potential target tile instance given the array of tile types it could be.
        # Is the unit already on a potential target tile?
        if self.isTileOfType(Config.gameMap.getTile(self.getXPos(), self.getYPos()), destinationTileTypeArray) == True:
            return [self.getXPos(), self.getYPos()]

        # Search for the nearest tile of tileType
        tileFound = False
        maxDistance = 5  # The farthest distance the unit will bother scanning for tiles
        distance = 1  # The shortest distance the unit will bother scanning. This should probably start at 1.
        while tileFound == False:  # check all spaces [distance] tiles away from the unit
            x = distance
            y = 0
            tileFound = False
            while tileFound == False:  # Check each position that adds up to the specified distance.
                unitXPos = self.getXPos()
                unitYPos = self.getYPos()
                targetXPosArray = [unitXPos - x, unitXPos + x, unitXPos - x, unitXPos + x]
                targetYPosArray = [unitYPos - y, unitYPos - y, unitYPos + y, unitYPos + y]
                for i in range(0, 3):
                    targetXPos = targetXPosArray[i]
                    targetYPos = targetYPosArray[i]
                    if self.isTileOfType(Config.gameMap.getTile(targetXPos, targetYPos),
                                         destinationTileTypeArray) == True:
                        return [targetXPos, targetYPos]
                    # No tile found [distance] tiles away that's a target tile.
                x -= 1
                y += 1
                if y > distance:  # We have checked every tile [distance] tiles away.
                    break
            distance += 1  # Increase distance and check all tiles that distance away.
            if distance > maxDistance:  # Don't bother checking tiles more than the specified max distance away..
                # print("No tile found")
                break

    def isTileOfType(self, tile, destinationTileTypeArray):
        # Note: This function was written to simplify the structure of findClosestTileOfType. It was not really intended for general use.
        for destinationTileType in destinationTileTypeArray:
            tileType = tile.getType()
            if tileType == destinationTileType:
                return True

    def perform(
            self):  # This is fired every tick. What action the unit performs is dependent on its behavior, as well as external factors.
        self.reduceHungerPoints()
        # print('Top priority: ', self.getPriorityQueue()[0])
        priorityIndex = 0
        while self.getTargetXPos() == None:
            currentStrategy = self.getCurrentStrategy(priorityIndex)
            if currentStrategy.focusTileTypes:
                # Find target tile type of closet position
                targetPos = self.findPosOfClosestTileOfType(
                    currentStrategy.focusTileTypes)  # returns closest potential target tile
                if targetPos:
                    self.setTargetPos(targetPos[0], targetPos[1])
                else:  # Tile not found! Try next strategy.
                    priorityIndex += 1
            else:
                break  # This priority has no target tiles (meaning it asks us to idle). That's managable, so let's break the loop and settle on this!
        if self.isUnitAtTargetPos() == True:  # If you are on the target tile, start collecting resources!
            self.collectResource()

        # TODO: If one unit is heading toward a tile, should other units try heading somewhere else?
        # Pathfind to (self.targetXPos, self.targetYPos)
        if self.getTargetXPos():
            # print('At ', self.getTargetXPos(), ' going to ', self.getXPos())
            if self.getTargetXPos() < self.getXPos():
                self.translatePosition(-1, 0)
            elif self.getTargetXPos() > self.getXPos():
                self.translatePosition(1, 0)

            elif self.getTargetYPos() < self.getYPos():
                self.translatePosition(0, -1)
            elif self.getTargetYPos() > self.getYPos():
                self.translatePosition(0, 1)
