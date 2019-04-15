#Kevin Dunn, add names
#CSC 305
#Colony Sim Game: Config
#3/22/2019


import pickle
import pygame
from pygame.locals import *
import sys, random, os.path
import math
from Map import *
from Unit import *



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
pause=0#pauses the actors when set to 1
gameMap=gMap(150,150)#creates the map object, change sizes here to resize a map

actors=5 #Actor(5,150,150)
actorsx = 150
actorsy = 150
screen=pygame.display.set_mode((tileSize*xlength+10,tileSize*ylength+10))
gameFont = pygame.font.match_font('arial')
timeSeconds=0
frameCount=0
frameRate=0


unitx4= pygame.image.load("Textures/4xUnit.bmp")
unitx4.set_colorkey((255,0,255))
unitx8= pygame.image.load("Textures/8xUnit.bmp")
unitx8.set_colorkey((255,0,255))
unitx16= pygame.image.load("Textures/16xUnit.bmp")
unitx16.set_colorkey((255,0,255))
unitx32= pygame.image.load("Textures/32xUnit.bmp")
unitx32.set_colorkey((255,0,255))
unitx64= pygame.image.load("Textures/64xUnit.bmp")
unitx64.set_colorkey((255,0,255))
unitx128= pygame.image.load("Textures/128xUnit.bmp")
unitx128.set_colorkey((255,0,255))
unitImg= unitx32

grassx4= pygame.image.load("Textures/4xGrass.bmp")
grassx8= pygame.image.load("Textures/8xGrass.bmp")
grassx16= pygame.image.load("Textures/16xGrass.bmp")
grassx32= pygame.image.load("Textures/32xGrass.bmp")
grassx64= pygame.image.load("Textures/64xGrass.bmp")
grassx128= pygame.image.load("Textures/128xGrass.bmp")
grassImg= grassx32

woodsx4= pygame.image.load("Textures/4xWoods.bmp")
woodsx8= pygame.image.load("Textures/8xWoods.bmp")
woodsx16= pygame.image.load("Textures/16xWoods.bmp")
woodsx32= pygame.image.load("Textures/32xWoods.bmp")
woodsx64= pygame.image.load("Textures/64xWoods.bmp")
woodsx128= pygame.image.load("Textures/128xWoods.bmp")
woodsImg= woodsx32

waterx4= pygame.image.load("Textures/4xWater.bmp")
waterx8= pygame.image.load("Textures/8xWater.bmp")
waterx16= pygame.image.load("Textures/16xWater.bmp")
waterx32= pygame.image.load("Textures/32xWater.bmp")
waterx64= pygame.image.load("Textures/64xWater.bmp")
waterx128= pygame.image.load("Textures/128xWater.bmp")
waterImg= waterx32

rocksx4= pygame.image.load("Textures/4xRocks.bmp")
rocksx8= pygame.image.load("Textures/8xRocks.bmp")
rocksx16= pygame.image.load("Textures/16xRocks.bmp")
rocksx32= pygame.image.load("Textures/32xRocks.bmp")
rocksx64= pygame.image.load("Textures/64xRocks.bmp")
rocksx128= pygame.image.load("Textures/128xRocks.bmp")
rocksImg= rocksx32
