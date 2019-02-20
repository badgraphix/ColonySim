#Kevin Dunn
#CSC 305
#Colony Sim Game
#2/17/2019

import pickle
import pygame
from pygame.locals import *
import sys, random, os.path
import math
from Tile import *
from Map import *

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
loadMap=1# if 1, Save.txt will be imediately loaded 

screen=pygame.display.set_mode((tileSize*xlength+10,tileSize*ylength+10))


    

#Kevin's
def drawCursor(gameMap):#draws the cursor, with brush size and shape, in all loops of the map
    mapTempX=-offsetX//gameMap.xSize
    mapLengthX=((xlength)//gameMap.xSize)+1
    mapTempY=-offsetY//gameMap.ySize
    mapLengthY=((ylength)//gameMap.ySize)+1
    for mapX in range(mapTempX-1,mapLengthX+mapTempX+1):
        for mapY in range(mapTempY-1,mapLengthY+mapTempY+1):
            for tempX in range(-brushSize,brushSize+1):
                        for tempY in range(-brushSize,brushSize+1):
                            if brushType==0:#fix local stuff
                                if loopMap==1 or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize:
                                    #gameMap.setColor((dotX+tempX)%gameMap.xSize,(dotY+tempY)%gameMap.ySize, 0)
                                    pygame.draw.rect(screen,(0,0,0),(5+tileSize*((dotX%gameMap.xSize+tempX+offsetX)+(mapX*gameMap.xSize)),5+tileSize*(((dotY%gameMap.ySize+tempY+offsetY)+(mapY*gameMap.ySize))),tileSize,tileSize),tileSize//4)
                                    #pygame.draw.rect(screen,(0,0,0),(200+((dotX%gameMap.xSize+tempX)+(mapX*gameMap.xSize)),200+(((dotY%gameMap.ySize+tempY)+(mapY*gameMap.ySize))),tileSize,tileSize),tileSize//4)
                            elif brushType==1:
                                if (loopMap==1 and abs(tempX)+abs(tempY)<=brushSize) or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize and abs(tempX)+abs(tempY)<=brushSize:
                                    pygame.draw.rect(screen,(100,0,0),(5+tileSize*((dotX%gameMap.xSize+tempX+offsetX)+(mapX*gameMap.xSize)),5+tileSize*(((dotY%gameMap.ySize+tempY+offsetY)+(mapY*gameMap.ySize))),tileSize,tileSize),tileSize//4)
                            elif brushType==2:
                                if (loopMap==1 and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=brushSize) or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=brushSize:
                                    pygame.draw.rect(screen,(50,0,100),(5+tileSize*((dotX%gameMap.xSize+tempX+offsetX)+(mapX*gameMap.xSize)),5+tileSize*(((dotY%gameMap.ySize+tempY+offsetY)+(mapY*gameMap.ySize))),tileSize,tileSize),tileSize//4)

#Kevin's
def drawAll(gameMap): #Draws all the objects, will need an update when unit actors arrive
    screen.fill((0,200,0))
    for x in range(0,xlength):
        for y in range(0,ylength):
            if loopMap==1 or gameMap.xSize+offsetX>x and offsetX<=x and gameMap.ySize+offsetY>y and offsetY<=y:
                pygame.draw.rect(screen,gameMap.getColor((x-offsetX)%(gameMap.xSize),(y-offsetY)%(gameMap.ySize)),(5+tileSize*x,5+tileSize*y,tileSize,tileSize),0)
            else:#else background rainbow
                pygame.draw.rect(screen,(255-(255*(x+y)/(xlength+ylength)),255*x/xlength,255*y/ylength),(5+tileSize*x,5+tileSize*y,tileSize,tileSize),0)
    drawCursor(gameMap)


def main():
    global tileSize
    global xlength
    global ylength
    global dotX
    global dotY
    global offsetX
    global offsetY
    global screen
    pygame.init()
    global brushSize
    global brushType
    global loopMap
    global loadMap

    gameMap=gMap(150,150)#creates the map object, change sizes here to resize a map
    if loadMap==1:
        with open("Save.txt","rb") as fp:
                gameMap=pickle.load(fp)

                
    i=0 #closes the window after a few minutes, will be changed later
    while (i<25000):
        i+=1
        
        #take keyboard input
        pygame.event.pump()
        keypress=pygame.key.get_pressed()
        offsetX-=keypress[K_RIGHT]-keypress[K_LEFT]#arrow keys are used to pan around the world
        offsetY-=keypress[K_DOWN]-keypress[K_UP]#^^
        dotX-=keypress[K_a]-keypress[K_d]#wasd are used to move the cursor around, the black tile
        dotY-=keypress[K_w]-keypress[K_s]#^^

        #here the number keys 1-4 can be pressed while the cursor is on the map, and it will assign a new type to that tile
        if keypress[K_1]:
            for tempX in range(-brushSize,brushSize+1):
                for tempY in range(-brushSize,brushSize+1):
                    if brushType==0:
                        if loopMap==1 or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize:
                            gameMap.setColor((dotX+tempX)%gameMap.xSize,(dotY+tempY)%gameMap.ySize, 0)
                    elif brushType==1:
                        if (loopMap==1 and abs(tempX)+abs(tempY)<=brushSize) or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize and abs(tempX)+abs(tempY)<=brushSize:
                            gameMap.setColor((dotX+tempX)%gameMap.xSize,(dotY+tempY)%gameMap.ySize, 0)
                    elif brushType==2:
                        if (loopMap==1 and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=brushSize) or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=brushSize:
                            gameMap.setColor((dotX+tempX)%gameMap.xSize,(dotY+tempY)%gameMap.ySize, 0)
        if keypress[K_2]:
            for tempX in range(-brushSize,brushSize+1):
                for tempY in range(-brushSize,brushSize+1):
                    if brushType==0:
                        if loopMap==1 or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize:
                            gameMap.setColor((dotX+tempX)%gameMap.xSize,(dotY+tempY)%gameMap.ySize, 1)
                    elif brushType==1:
                        if (loopMap==1 and abs(tempX)+abs(tempY)<=brushSize) or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize and abs(tempX)+abs(tempY)<=brushSize:
                            gameMap.setColor((dotX+tempX)%gameMap.xSize,(dotY+tempY)%gameMap.ySize, 1)
                    elif brushType==2:
                        if (loopMap==1 and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=brushSize) or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=brushSize:
                            gameMap.setColor((dotX+tempX)%gameMap.xSize,(dotY+tempY)%gameMap.ySize, 1)
        if keypress[K_3]:
            for tempX in range(-brushSize,brushSize+1):
                for tempY in range(-brushSize,brushSize+1):
                    if brushType==0:
                        if loopMap==1 or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize:
                            gameMap.setColor((dotX+tempX)%gameMap.xSize,(dotY+tempY)%gameMap.ySize, 2)
                    elif brushType==1:
                        if (loopMap==1 and abs(tempX)+abs(tempY)<=brushSize) or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize and abs(tempX)+abs(tempY)<=brushSize:
                            gameMap.setColor((dotX+tempX)%gameMap.xSize,(dotY+tempY)%gameMap.ySize, 2)
                    elif brushType==2:
                        if (loopMap==1 and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=brushSize) or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=brushSize:
                            gameMap.setColor((dotX+tempX)%gameMap.xSize,(dotY+tempY)%gameMap.ySize, 2)
        if keypress[K_4]:
            for tempX in range(-brushSize,brushSize+1):
                for tempY in range(-brushSize,brushSize+1):
                    if brushType==0:
                        if loopMap==1 or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize:
                            gameMap.setColor((dotX+tempX)%gameMap.xSize,(dotY+tempY)%gameMap.ySize, 3)
                    elif brushType==1:
                        if (loopMap==1 and abs(tempX)+abs(tempY)<=brushSize) or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize and abs(tempX)+abs(tempY)<=brushSize:
                            gameMap.setColor((dotX+tempX)%gameMap.xSize,(dotY+tempY)%gameMap.ySize, 3)
                    elif brushType==2:
                        if (loopMap==1 and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=brushSize) or dotY+tempY>=0 and dotY+tempY<gameMap.ySize and dotX+tempX>=0 and dotX+tempX<gameMap.xSize and math.sqrt(math.pow(tempX,2)+math.pow(tempY,2))-0.2<=brushSize:
                            gameMap.setColor((dotX+tempX)%gameMap.xSize,(dotY+tempY)%gameMap.ySize, 3)

        #adjusts the brush size
        if keypress[K_p]:
            brushSize+=1
        if keypress[K_o] and brushSize!=0:
            brushSize-=1
        if keypress[K_i]:#change brush shape between square, diamond, and round
            if brushType==0:
                brushType=1
            elif brushType==1:
                brushType=2
            elif brushType==2:
                brushType=0


        #here the plus and minus(without shift so - and =) are used to zoom in and out by powers of 2, the zoom is centered on the middle of the screen, and the cursor stays put relative to the map not the window(on purpose)    
        if keypress[K_EQUALS]:
            tileSize=tileSize*2
            xlength=xlength//2
            ylength=ylength//2
            offsetX-=xlength//2
            offsetY-=ylength//2
        if keypress[K_MINUS]:
            tileSize=tileSize//2
            xlength=xlength*2
            ylength=ylength*2
            offsetX+=xlength//4
            offsetY+=ylength//4

        #'9' is used to save the game to a text file, '0' is used to load the save, to save long term, make sure to make a copy of this file elsewhere.
        if keypress[K_9]:
            with open("Save.txt","wb") as fp:
                pickle.dump(gameMap, fp)
        if keypress[K_0]:
            with open("Save.txt","rb") as fp:
                gameMap=pickle.load(fp)

        drawAll(gameMap)#call the draw map function
        pygame.display.update()#update map once updated

        #game time
        pygame.time.wait(frameTime)#pause for a short while 
        
    #not my code *VVVVVV
    pygame.quit(); sys.exit();

    
#if python says run, let's run!
if __name__ == '__main__':
    main()
