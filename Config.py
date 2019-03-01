#Kevin Dunn, add names
#CSC 305
#Colony Sim Game: Config
#2/28/2019


import pickle
import pygame
from pygame.locals import *
import sys, random, os.path
import math
from Tile import *
from Map import *
from Unit import *
from Main import *


#GlobalVariables
xlength=32 #height and width of the window in tiles, a multiple of 2 for zoomability scale issues
ylength=16 #^^
tileSize=32 #length side of square tile, again multiple of two for scalability 
dotX=5 #position of "cursor" black square for map editing
dotY=5 #^^  Will most likely be moved into an actor class by the unit guy
offsetX=0 #shift of the map and actors on the grid, used to pan the screen, shifted in tiles not pixels
offsetY=0 #^^
brushSize=0#brush size for editor
brushType=0#shape of brush 
frameTime=100 #pause between frames edit here to experiment
loopMap=1#conditional, can be changed here before execution, 1 for looped infinite map, 0 for map with edges
loadMap=0# if 1, Save.txt will be imediately loaded
stop=0 #ends the game when set to 1
gameMap=gMap(150,150)#creates the map object, change sizes here to resize a map
actors=Actor(5,10,10)
screen=pygame.display.set_mode((tileSize*xlength+10,tileSize*ylength+10))
