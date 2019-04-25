# Kevin Dunn, add names
# CSC 305
# Colony Sim Game: Input
# 4/2/2019

import pygame
from pygame.locals import *
import Config
import pickle
import math
import Main


# When a scale change takes place, all the sprites are set to the correct size
def scaleSprites():
    if Config.tileSize == 4:
        Config.unitImg = Config.unitx4
        Config.baseImg = Config.basex4
        Config.grassImg = Config.grassx4
        Config.woodsImg = Config.woodsx4
        Config.waterImg = Config.waterx4
        Config.rocksImg = Config.rocksx4
        Config.farmsImg = Config.farmsx4
    if Config.tileSize == 8:
        Config.unitImg = Config.unitx8
        Config.baseImg = Config.basex8
        Config.grassImg = Config.grassx8
        Config.woodsImg = Config.woodsx8
        Config.waterImg = Config.waterx8
        Config.rocksImg = Config.rocksx8
        Config.farmsImg = Config.farmsx8
    if Config.tileSize == 16:
        Config.unitImg = Config.unitx16
        Config.baseImg = Config.basex16
        Config.grassImg = Config.grassx16
        Config.woodsImg = Config.woodsx16
        Config.waterImg = Config.waterx16
        Config.rocksImg = Config.rocksx16
        Config.farmsImg = Config.farmsx16
    if Config.tileSize == 32:
        Config.unitImg = Config.unitx32
        Config.baseImg = Config.basex32
        Config.grassImg = Config.grassx32
        Config.woodsImg = Config.woodsx32
        Config.waterImg = Config.waterx32
        Config.rocksImg = Config.rocksx32
        Config.farmsImg = Config.farmsx32
    if Config.tileSize == 64:
        Config.unitImg = Config.unitx64
        Config.baseImg = Config.basex64
        Config.grassImg = Config.grassx64
        Config.woodsImg = Config.woodsx64
        Config.waterImg = Config.waterx64
        Config.rocksImg = Config.rocksx64
        Config.farmsImg = Config.farmsx64
    if Config.tileSize == 128:
        Config.unitImg = Config.unitx128
        Config.baseImg = Config.basex128
        Config.grassImg = Config.grassx128
        Config.woodsImg = Config.woodsx128
        Config.waterImg = Config.waterx128
        Config.rocksImg = Config.rocksx128
        Config.farmsImg = Config.farmsx128


def testSelect():
    Config.selectedUnitID = Config.gameMap.getTile(Config.dotX, Config.dotY).getStationedUnitID()
    #print(Config.gameMap.getTile(Config.dotX, Config.dotY).getStationedUnitID())


def inputEditor():
    pygame.event.pump()
    keypress = pygame.key.get_pressed()

    # Quits the game if "ESCAPE" or the corner 'x' are pressed
    if pygame.event.peek(QUIT) or keypress[K_ESCAPE]:
        Config.stop = 1

    if keypress[K_t]:
        Main.actors.data[0].translatePosition(0,1)
    if keypress[K_5]:
        Main.actors.data[0].translatePosition(0,-1)
    if keypress[K_r]:
        Main.actors.data[0].translatePosition(-1,0)
    if keypress[K_y]:
        Main.actors.data[Config.selectedUnitID].translatePosition(1,0)

    # Movement across map
    Config.subTileX-=(keypress[K_RIGHT]-keypress[K_LEFT])*(32//Config.tileSize+5)*3#arrow keys are used to pan around the world
    Config.subTileY-=(keypress[K_DOWN]-keypress[K_UP])*(32//Config.tileSize+5)*3#^^
    
    Config.offsetX += Config.subTileX // Config.tileSize
    Config.offsetY += Config.subTileY // Config.tileSize
    Config.subTileX = Config.subTileX % Config.tileSize
    Config.subTileY = Config.subTileY % Config.tileSize
    Config.dotX = (Config.dotX - (keypress[K_a] - keypress[K_d])) \
                  % Config.gameMap.xSize  # wasd are used to move the cursor around, the black tile
    Config.dotY = (Config.dotY - (keypress[K_w] - keypress[K_s]))\
                  % Config.gameMap.ySize  # ^^
    '''
    if keypress[K_RIGHT]:
        Config.bottomMenu.changeSelectedUnit(1, Main.actors)
    if keypress[K_LEFT]:
        Config.bottomMenu.changeSelectedUnit(-1, Main.actors)
    if keypress[K_UP]:
        Config.bottomMenu.changeSelectedUnit(-10, Main.actors)
    if keypress[K_DOWN]:
        Config.bottomMenu.changeSelectedUnit(10, Main.actors)
    '''
    
    # New controls for changing tile types. The new choices are E, R, T, and Y. This is so the bottom menu controls correspond to
    # their labels
    if keypress[K_1]:
        for tempX in range(-Config.brushSize, Config.brushSize + 1):
            for tempY in range(-Config.brushSize, Config.brushSize + 1):
                if Config.brushType == 0:
                    if Config.loopMap == 1 or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 0)
                elif Config.brushType == 1:
                    if (Config.loopMap == 1 and abs(tempX) + abs(
                            tempY) <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and abs(
                        tempX) + abs(tempY) <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 0)
                elif Config.brushType == 2:
                    if (Config.loopMap == 1 and math.sqrt(math.pow(tempX, 2) + math.pow(tempY,
                                                                                        2)) - 0.2 <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and math.sqrt(
                        math.pow(tempX, 2) + math.pow(tempY, 2)) - 0.2 <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 0)

    if keypress[K_2]:
        for tempX in range(-Config.brushSize, Config.brushSize + 1):
            for tempY in range(-Config.brushSize, Config.brushSize + 1):
                if Config.brushType == 0:
                    if Config.loopMap == 1 or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 1)
                elif Config.brushType == 1:
                    if (Config.loopMap == 1 and abs(tempX) + abs(
                            tempY) <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and abs(
                        tempX) + abs(tempY) <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 1)
                elif Config.brushType == 2:
                    if (Config.loopMap == 1 and math.sqrt(math.pow(tempX, 2) + math.pow(tempY,
                                                                                        2)) - 0.2 <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and math.sqrt(
                        math.pow(tempX, 2) + math.pow(tempY, 2)) - 0.2 <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 1)

    if keypress[K_3]:
        for tempX in range(-Config.brushSize, Config.brushSize + 1):
            for tempY in range(-Config.brushSize, Config.brushSize + 1):
                if Config.brushType == 0:
                    if Config.loopMap == 1 or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 2)
                elif Config.brushType == 1:
                    if (Config.loopMap == 1 and abs(tempX) + abs(
                            tempY) <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and abs(
                        tempX) + abs(tempY) <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 2)
                elif Config.brushType == 2:
                    if (Config.loopMap == 1 and math.sqrt(math.pow(tempX, 2) + math.pow(tempY,
                                                                                        2)) - 0.2 <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and math.sqrt(
                        math.pow(tempX, 2) + math.pow(tempY, 2)) - 0.2 <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 2)

    if keypress[K_4]:
        for tempX in range(-Config.brushSize, Config.brushSize + 1):
            for tempY in range(-Config.brushSize, Config.brushSize + 1):
                if Config.brushType == 0:
                    if Config.loopMap == 1 or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 3)
                elif Config.brushType == 1:
                    if (Config.loopMap == 1 and abs(tempX) + abs(
                            tempY) <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and abs(
                        tempX) + abs(tempY) <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 3)
                elif Config.brushType == 2:
                    if (Config.loopMap == 1 and math.sqrt(math.pow(tempX, 2) + math.pow(tempY,
                                                                                        2)) - 0.2 <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and math.sqrt(
                        math.pow(tempX, 2) + math.pow(tempY, 2)) - 0.2 <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 3)

    if keypress[K_5]:
        for tempX in range(-Config.brushSize, Config.brushSize + 1):
            for tempY in range(-Config.brushSize, Config.brushSize + 1):
                if Config.brushType == 0:
                    if Config.loopMap == 1 or Config.dotY + tempY >= 0 and Config.dotY + tempY < Config.gameMap.ySize and Config.dotX + tempX >= 0 and Config.dotX + tempX < Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 4)
                elif Config.brushType == 1:
                    if (Config.loopMap == 1 and abs(tempX) + abs(
                            tempY) <= Config.brushSize) or Config.dotY + tempY >= 0 and Config.dotY + tempY < Config.gameMap.ySize and Config.dotX + tempX >= 0 and Config.dotX + tempX < Config.gameMap.xSize and abs(
                        tempX) + abs(tempY) <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 4)
                elif Config.brushType == 2:
                    if (Config.loopMap == 1 and math.sqrt(math.pow(tempX, 2) + math.pow(tempY,
                                                                                        2)) - 0.2 <= Config.brushSize) or Config.dotY + tempY >= 0 and Config.dotY + tempY < Config.gameMap.ySize and Config.dotX + tempX >= 0 and Config.dotX + tempX < Config.gameMap.xSize and math.sqrt(
                        math.pow(tempX, 2) + math.pow(tempY, 2)) - 0.2 <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 4)

    # Here are the controls for the bottom menu, which is located in Config.py
    '''
    if keypress[K_1]:
        Config.bottomMenu.changeMode(1)
    if keypress[K_2]:
        Config.bottomMenu.changeMode(2)
    if keypress[K_3]:
        Config.bottomMenu.changeMode(3)
'''
    # adjusts the brush size
    if keypress[K_p]:
        Config.brushSize += 1
    if keypress[K_o] and Config.brushSize != 0:
        Config.brushSize -= 1

    # change brush shape between square, diamond, and round
    if keypress[K_i]:
        Config.brushType = (Config.brushType + 1) % 3

    # Select a unit.
    if keypress[K_u]:
        testSelect()

    # here the plus and minus(without shift so - and =) are used to zoom in and out by powers of 2, the zoom is centered on the middle of the screen, and the cursor stays put relative to the map not the window(on purpose)
    if keypress[K_EQUALS] and Config.tileSize <= 80:
        Config.tileSize = Config.tileSize * 2
        Config.xlength = Config.xlength // 2
        Config.ylength = Config.ylength // 2
        Config.offsetX -= Config.xlength // 2
        Config.offsetY -= Config.ylength // 2
        scaleSprites()
    if keypress[K_MINUS] and Config.tileSize >= 5:
        Config.tileSize = Config.tileSize // 2
        Config.xlength = Config.xlength * 2
        Config.ylength = Config.ylength * 2
        Config.offsetX += Config.xlength // 4
        Config.offsetY += Config.ylength // 4
        scaleSprites()

    # '9' is used to save the game to a text file, '0' is used to load the save, to save long term, make sure to make a copy of this file elsewhere.
    if keypress[K_9]:
        with open("Saves/Save.txt", "wb") as fp:
            pickle.dump(Config.gameMap, fp)
    if keypress[K_0]:
        with open("Saves/Save.txt", "rb") as fp:
            Config.gameMap = pickle.load(fp)

    # Space is used to pause the game
    if keypress[K_SPACE]:
        Config.pause = (Config.pause + 1) % 2

def inputGame():
    pygame.event.pump()
    keypress = pygame.key.get_pressed()

    # Quits the game if "ESCAPE" or the corner 'x' are pressed
    if pygame.event.peek(QUIT) or keypress[K_ESCAPE]:
        Config.stop = 1

    # Removing this as it interferes
    '''
    Config.subTileX-=(keypress[K_RIGHT]-keypress[K_LEFT])*(32//Config.tileSize+5)*3#arrow keys are used to pan around the world
    Config.subTileY-=(keypress[K_DOWN]-keypress[K_UP])*(32//Config.tileSize+5)*3#^^
    '''
    Config.offsetX += Config.subTileX // Config.tileSize
    Config.offsetY += Config.subTileY // Config.tileSize
    Config.subTileX = Config.subTileX % Config.tileSize
    Config.subTileY = Config.subTileY % Config.tileSize
    Config.dotX = (Config.dotX - (keypress[K_a] - keypress[K_d])) \
                  % Config.gameMap.xSize  # wasd are used to move the cursor around, the black tile
    Config.dotY = (Config.dotY - (keypress[K_w] - keypress[K_s]))\
                  % Config.gameMap.ySize  # ^^

    if keypress[K_RIGHT]:
        Config.bottomMenu.changeSelectedUnit(1, Main.actors)
    if keypress[K_LEFT]:
        Config.bottomMenu.changeSelectedUnit(-1, Main.actors)
    if keypress[K_UP]:
        Config.bottomMenu.changeSelectedUnit(-10, Main.actors)
    if keypress[K_DOWN]:
        Config.bottomMenu.changeSelectedUnit(10, Main.actors)

    # New controls for changing tile types. The new choices are E, R, T, and Y. This is so the bottom menu controls correspond to
    # their labels
    if keypress[K_e]:
        for tempX in range(-Config.brushSize, Config.brushSize + 1):
            for tempY in range(-Config.brushSize, Config.brushSize + 1):
                if Config.brushType == 0:
                    if Config.loopMap == 1 or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 0)
                elif Config.brushType == 1:
                    if (Config.loopMap == 1 and abs(tempX) + abs(
                            tempY) <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and abs(
                        tempX) + abs(tempY) <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 0)
                elif Config.brushType == 2:
                    if (Config.loopMap == 1 and math.sqrt(math.pow(tempX, 2) + math.pow(tempY,
                                                                                        2)) - 0.2 <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and math.sqrt(
                        math.pow(tempX, 2) + math.pow(tempY, 2)) - 0.2 <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 0)

    if keypress[K_r]:
        for tempX in range(-Config.brushSize, Config.brushSize + 1):
            for tempY in range(-Config.brushSize, Config.brushSize + 1):
                if Config.brushType == 0:
                    if Config.loopMap == 1 or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 1)
                elif Config.brushType == 1:
                    if (Config.loopMap == 1 and abs(tempX) + abs(
                            tempY) <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and abs(
                        tempX) + abs(tempY) <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 1)
                elif Config.brushType == 2:
                    if (Config.loopMap == 1 and math.sqrt(math.pow(tempX, 2) + math.pow(tempY,
                                                                                        2)) - 0.2 <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and math.sqrt(
                        math.pow(tempX, 2) + math.pow(tempY, 2)) - 0.2 <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 1)

    if keypress[K_t]:
        for tempX in range(-Config.brushSize, Config.brushSize + 1):
            for tempY in range(-Config.brushSize, Config.brushSize + 1):
                if Config.brushType == 0:
                    if Config.loopMap == 1 or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 2)
                elif Config.brushType == 1:
                    if (Config.loopMap == 1 and abs(tempX) + abs(
                            tempY) <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and abs(
                        tempX) + abs(tempY) <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 2)
                elif Config.brushType == 2:
                    if (Config.loopMap == 1 and math.sqrt(math.pow(tempX, 2) + math.pow(tempY,
                                                                                        2)) - 0.2 <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and math.sqrt(
                        math.pow(tempX, 2) + math.pow(tempY, 2)) - 0.2 <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 2)

    if keypress[K_y]:
        for tempX in range(-Config.brushSize, Config.brushSize + 1):
            for tempY in range(-Config.brushSize, Config.brushSize + 1):
                if Config.brushType == 0:
                    if Config.loopMap == 1 or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 3)
                elif Config.brushType == 1:
                    if (Config.loopMap == 1 and abs(tempX) + abs(
                            tempY) <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and abs(
                        tempX) + abs(tempY) <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 3)
                elif Config.brushType == 2:
                    if (Config.loopMap == 1 and math.sqrt(math.pow(tempX, 2) + math.pow(tempY,
                                                                                        2)) - 0.2 <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and math.sqrt(
                        math.pow(tempX, 2) + math.pow(tempY, 2)) - 0.2 <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 3)

    if keypress[K_u]:
        for tempX in range(-Config.brushSize, Config.brushSize + 1):
            for tempY in range(-Config.brushSize, Config.brushSize + 1):
                if Config.brushType == 0:
                    if Config.loopMap == 1 or Config.dotY + tempY >= 0 and Config.dotY + tempY < Config.gameMap.ySize and Config.dotX + tempX >= 0 and Config.dotX + tempX < Config.gameMap.xSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 4)
                elif Config.brushType == 1:
                    if (Config.loopMap == 1 and abs(tempX) + abs(
                            tempY) <= Config.brushSize) or Config.dotY + tempY >= 0 and Config.dotY + tempY < Config.gameMap.ySize and Config.dotX + tempX >= 0 and Config.dotX + tempX < Config.gameMap.xSize and abs(
                        tempX) + abs(tempY) <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 4)
                elif Config.brushType == 2:
                    if (Config.loopMap == 1 and math.sqrt(math.pow(tempX, 2) + math.pow(tempY,
                                                                                        2)) - 0.2 <= Config.brushSize) or Config.dotY + tempY >= 0 and Config.dotY + tempY < Config.gameMap.ySize and Config.dotX + tempX >= 0 and Config.dotX + tempX < Config.gameMap.xSize and math.sqrt(
                        math.pow(tempX, 2) + math.pow(tempY, 2)) - 0.2 <= Config.brushSize:
                        Config.gameMap.setColor((Config.dotX + tempX) % Config.gameMap.xSize,
                                                (Config.dotY + tempY) % Config.gameMap.ySize, 4)

    # Here are the controls for the bottom menu, which is located in Config.py
    if keypress[K_1]:
        Config.bottomMenu.changeMode(1)
    if keypress[K_2]:
        Config.bottomMenu.changeMode(2)
    if keypress[K_3]:
        Config.bottomMenu.changeMode(3)

    # adjusts the brush size
    if keypress[K_p]:
        Config.brushSize += 1
    if keypress[K_o] and Config.brushSize != 0:
        Config.brushSize -= 1

    # change brush shape between square, diamond, and round
    if keypress[K_i]:
        Config.brushType = (Config.brushType + 1) % 3

    # Select a unit.
    if keypress[K_u]:
        testSelect()

    # here the plus and minus(without shift so - and =) are used to zoom in and out by powers of 2, the zoom is centered on the middle of the screen, and the cursor stays put relative to the map not the window(on purpose)
    if keypress[K_EQUALS] and Config.tileSize <= 80:
        Config.tileSize = Config.tileSize * 2
        Config.xlength = Config.xlength // 2
        Config.ylength = Config.ylength // 2
        Config.offsetX -= Config.xlength // 2
        Config.offsetY -= Config.ylength // 2
        scaleSprites()
    if keypress[K_MINUS] and Config.tileSize >= 5:
        Config.tileSize = Config.tileSize // 2
        Config.xlength = Config.xlength * 2
        Config.ylength = Config.ylength * 2
        Config.offsetX += Config.xlength // 4
        Config.offsetY += Config.ylength // 4
        scaleSprites()

    # '9' is used to save the game to a text file, '0' is used to load the save, to save long term, make sure to make a copy of this file elsewhere.
    if keypress[K_9]:
        with open("Saves/Save.txt", "wb") as fp:
            pickle.dump(Config.gameMap, fp)
    if keypress[K_0]:
        with open("Saves/Save.txt", "rb") as fp:
            Config.gameMap = pickle.load(fp)

    # Space is used to pause the game
    if keypress[K_SPACE]:
        Config.pause = (Config.pause + 1) % 2
