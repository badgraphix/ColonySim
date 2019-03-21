#Cam Brady, John Bertsch, Kevin Dunn
#CSC 305
#Colony Sim Game: Units
#2/28/2019

import pickle
import pygame
from pygame.locals import *
import sys, random, os.path
import math
from Tile import *
#import Config

class Actor:
    data=[]
    #imgDisplay=[]
    totalActors=0
    def __init__(self, num,x,y):
        self.totalActors=num
        for temp in range(0,num):
            unitTemp=unit(0,random.randint(0,x),random.randint(0,y))
            #surfaceTemp=Surface(32,32)
            self.data.append(unitTemp)
    def allAct(self):
        for temp in range(0,self.totalActors):
            self.data[temp].perform()
        

class unit(object):
    xPos = 0# Coordinates
    yPos = 0
    hungerPoints = 100#Hunger. When it hits 0, the unit dies.
    unitType = 1#Unit type. Represented as an integer that is used as the parameter for a getUnitData() function.
    inventory = [0,0,0,0,0,0]#Inventory. Each entry in the array represents the quantity of that respective resource type. A unit can only hold ONE type of resource at a time, so keep this in mind while developing.
    behavior = 0 #Each behavior type is currently stored as an int. 0 is standby mode, where the unit will not perform any actions.
    def __init__(self, unitType, x, y):
        self.unitType = unitType
        self.xPos = x
        self.yPos = y
        self.behavior=0
        self.inventory=[0,0,0,0,0,0]
        self.unitType=1
        self.hungerPoints=0
    def setInventory(self, resourceType, quantity):
        self.inventory[resourceType] += quantity
    def setBehavior(self, behaviorType):
        self.behavior = behaviorType
    def getInventory(self):
        return self.inventory
    def getBehavior(self):
        return self.behavior
    def getCurrentTile(self):#TODO: Uses self.xPos and self.yPos to find the tile on the tile table and returns it.
        print("Hello")
        return Config.gameMap.getTile(self.xPos,self.yPos);
        #.tileType (between 0 and 4)
    def modifyPosition(self, x, y):
        self.xPos = (self.xPos+x)%Config.gameMap.xSize
        self.yPos = (self.yPos+y)%Config.gameMap.ySize
    def collectResource(self):#Farms resource on the tile the unit is standing on. This is fired for all units on every tick, if it is possible for them to farm something.
        currentTile = self.getCurrentTile()
        #TODO: add a function in tile that lets us remove a resource from it and return it here.
    def perform(self): #This is fired every tick. What action the unit performs is dependent on its behavior, as well as external factors.
        self.getCurrentTile()
        if self.getBehavior() == 0 and random.randint(0,4)==0: #Continuously travel right
            self.modifyPosition(random.randint(-1,1),random.randint(-1,1))



import Config
