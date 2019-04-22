#Kevin Dunn
#CSC 305
#Colony Sim Game: Display functions
#4/2/2019

from Input import *
import Main
import Config
import time


# Kevin's
def drawCursor():  # draws the cursor, with brush size and shape, in all loops of the map

    mapTempX = -Config.offsetX // Config.gameMap.xSize
    mapLengthX = (Config.xlength // Config.gameMap.xSize) + 1
    mapTempY = -Config.offsetY // Config.gameMap.ySize
    mapLengthY = (Config.ylength // Config.gameMap.ySize) + 1
    for mapX in range(mapTempX - 1, mapLengthX + mapTempX + 1):
        for mapY in range(mapTempY - 1, mapLengthY + mapTempY + 1):
            for tempX in range(-Config.brushSize, Config.brushSize + 1):
                for tempY in range(-Config.brushSize, Config.brushSize + 1):
                    if Config.brushType == 0:
                        if Config.loopMap == 1 or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize:
                            pygame.draw.rect(Config.screen, (0, 0, 0), (5 + Config.tileSize * (
                                    (Config.dotX % Config.gameMap.xSize + tempX + Config.offsetX) + (
                                    mapX * Config.gameMap.xSize)), 5 + Config.tileSize * ((
                                    (Config.dotY % Config.gameMap.ySize + tempY + Config.offsetY) + (mapY * Config.gameMap.ySize))), Config.tileSize, Config.tileSize),
                                             Config.tileSize // 4)
                    elif Config.brushType == 1:
                        if (Config.loopMap == 1 and abs(tempX) + abs(
                                tempY) <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and abs(tempX) + abs(tempY) <= Config.brushSize:
                            pygame.draw.rect(Config.screen, (100, 0, 0), (5 + Config.tileSize * (
                                    (Config.dotX % Config.gameMap.xSize + tempX + Config.offsetX) +
                                    (mapX * Config.gameMap.xSize)), 5 + Config.tileSize * ((
                                    (Config.dotY % Config.gameMap.ySize + tempY + Config.offsetY) +
                                    (mapY * Config.gameMap.ySize))), Config.tileSize, Config.tileSize),
                                             Config.tileSize // 4)
                    elif Config.brushType == 2:
                        if (Config.loopMap == 1 and math.sqrt(math.pow(tempX, 2) + math.pow(tempY,
                                                                                            2)) - 0.2 <= Config.brushSize) or 0 <= Config.dotY + tempY < Config.gameMap.ySize and 0 <= Config.dotX + tempX < Config.gameMap.xSize and \
                                math.sqrt(math.pow(tempX, 2) + math.pow(tempY, 2)) - 0.2 <= Config.brushSize:
                            pygame.draw.rect(Config.screen, (50, 0, 100), (5 + Config.tileSize * (
                                    (Config.dotX % Config.gameMap.xSize + tempX + Config.offsetX) + (mapX * Config.gameMap.xSize)), 5 + Config.tileSize *
                                    ((Config.dotY % Config.gameMap.ySize + tempY + Config.offsetY) + (mapY * Config.gameMap.ySize)), Config.tileSize, Config.tileSize),
                                             Config.tileSize // 4)


# Units
def drawUnit():
    mapTempX=-Config.offsetX//Config.gameMap.xSize
    mapLengthX=((Config.xlength)//Config.gameMap.xSize)+1
    mapTempY=-Config.offsetY//Config.gameMap.ySize
    mapLengthY=((Config.ylength)//Config.gameMap.ySize)+1
    for temp in range(0,Main.actors.totalActors):
        for mapX in range(mapTempX-1,mapLengthX+mapTempX+1):
            for mapY in range(mapTempY-1,mapLengthY+mapTempY+1):
                Config.screen.blit(Config.unitImg,(Config.tileSize*((Main.actors.data[temp].xPos%Config.gameMap.xSize+Config.offsetX)+(mapX*Config.gameMap.xSize))+Config.subTileX,Config.tileSize*(((Main.actors.data[temp].yPos%Config.gameMap.ySize+Config.offsetY)+(mapY*Config.gameMap.ySize)))+Config.subTileY,Config.tileSize,Config.tileSize))
                if Config.selectedUnitID==temp:
                    pygame.draw.rect(Config.screen,(200,200,200),(Config.tileSize*((Main.actors.data[temp].xPos%Config.gameMap.xSize+Config.offsetX)+(mapX*Config.gameMap.xSize))+Config.subTileX,Config.tileSize*(((Main.actors.data[temp].yPos%Config.gameMap.ySize+Config.offsetY)+(mapY*Config.gameMap.ySize)))+Config.subTileY,Config.tileSize,Config.tileSize),Config.tileSize//8)


def drawBuildings():
    mapTempX = -Config.offsetX // Config.gameMap.xSize
    mapLengthX = (Config.xlength // Config.gameMap.xSize) + 1
    mapTempY = -Config.offsetY // Config.gameMap.ySize
    mapLengthY = (Config.ylength // Config.gameMap.ySize) + 1
    for temp in range(0, 5):
        for mapX in range(mapTempX - 1, mapLengthX + mapTempX + 1):
            for mapY in range(mapTempY - 1, mapLengthY + mapTempY + 1):
                Config.screen.blit(Config.unitImg, (5 + Config.tileSize * (
                        (Main.actors.data[temp].xPos % Config.gameMap.xSize + Config.offsetX) + (
                        mapX * Config.gameMap.xSize)), 5 + Config.tileSize * ((
                        (Main.actors.data[temp].yPos % Config.gameMap.ySize + Config.offsetY) + (
                        mapY * Config.gameMap.ySize))), Config.tileSize, Config.tileSize))
                # pygame.draw.rect(Config.screen,(200,200,200),(5+Config.tileSize*((Config.actors.data[temp].xPos%Config.gameMap.xSize+Config.offsetX)+(mapX*Config.gameMap.xSize)),5+Config.tileSize*(((Config.actors.data[temp].yPos%Config.gameMap.ySize+Config.offsetY)+(mapY*Config.gameMap.ySize))),Config.tileSize,Config.tileSize),1)


def drawText(X, Y, Text, size):
    fontDisplay = pygame.font.Font(Config.gameFont, size)
    textRender = fontDisplay.render(Text, False, (0, 0, 0))
    Config.screen.blit(textRender, (X, Y))


def frameRate():
    tempTime = time.time() // 1
    if Config.timeSeconds == tempTime:
        Config.frameCount += 1
    else:
        Config.frameRate = Config.frameCount
        Config.frameCount = 0
        Config.timeSeconds = tempTime
    drawText(10, 10, str(Config.frameRate), 30)


def displayPause():
    tempTime = time.time() * 1000 - ((time.time() // 1) * 1000)
    if tempTime // 500 == 0:
        drawText(200, 200, "PAUSED", 50)

# Kevin's
def drawAll():  # Draws all the objects
    Config.screen.fill((0, 200, 0))
    for x in range(0, Config.xlength):
        for y in range(0, Config.ylength):
            if Config.loopMap == 1 or Config.gameMap.xSize + Config.offsetX > x >= Config.offsetX and Config.gameMap.ySize + Config.offsetY > y >= Config.offsetY:
                if Config.gameMap.getTile((x - Config.offsetX) % Config.gameMap.xSize,
                                          (y - Config.offsetY) % Config.gameMap.ySize).tileType == 0:
                    Config.screen.blit(Config.grassImg, (5 + Config.tileSize * x, 5 + Config.tileSize * y))
                elif Config.gameMap.getTile((x - Config.offsetX) % Config.gameMap.xSize,
                                            (y - Config.offsetY) % Config.gameMap.ySize).tileType == 1:
                    Config.screen.blit(Config.woodsImg, (5 + Config.tileSize * x, 5 + Config.tileSize * y))
                elif Config.gameMap.getTile((x - Config.offsetX) % Config.gameMap.xSize,
                                            (y - Config.offsetY) % Config.gameMap.ySize).tileType == 2:
                    Config.screen.blit(Config.waterImg, (5 + Config.tileSize * x, 5 + Config.tileSize * y))
                elif Config.gameMap.getTile((x - Config.offsetX) % Config.gameMap.xSize,
                                            (y - Config.offsetY) % Config.gameMap.ySize).tileType == 3:
                    Config.screen.blit(Config.rocksImg, (5 + Config.tileSize * x, 5 + Config.tileSize * y))
                elif Config.gameMap.getTile((x - Config.offsetX) % Config.gameMap.xSize,
                                            (y - Config.offsetY) % Config.gameMap.ySize).tileType == 4:
                    Config.screen.blit(Config.farmsImg, (5 + Config.tileSize * x, 5 + Config.tileSize * y))
                else:
                    pygame.draw.rect(Config.screen,
                                     Config.gameMap.getColor((x - Config.offsetX) % Config.gameMap.xSize,
                                                             (y - Config.offsetY) % Config.gameMap.ySize), (
                                         5 + Config.tileSize * x, 5 + Config.tileSize * y, Config.tileSize,
                                         Config.tileSize), 0)
            else:  # else background rainbow
                pygame.draw.rect(Config.screen, (255 - (255 * (x + y) / (Config.xlength + Config.ylength)), 255 * x / Config.xlength,255 * y / Config.ylength),
                                 (5 + Config.tileSize * x, 5 + Config.tileSize * y, Config.tileSize, Config.tileSize), 0)
    drawCursor()
    drawUnit()
    drawBuildings()
    frameRate()
    Config.bottomMenu.draw(Config.screen, Main.actors, Main.buildings)
    if Config.pause == 1:
        displayPause()
