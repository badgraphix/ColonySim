#Kevin Dunn
#CSC 305
#Colony Sim Game
#2/17/2019

import pickle
import pygame
from pygame.locals import *
import sys, random, os.path

#GlobalVariables
xlength=16 #height and width of the window in tiles, a multiple of 2 for zoomability scale issues
ylength=16 #^^
tileSize=32 #length side of square tile, again multiple of two for scalability 
dotX=5 #position of "cursor" black square for map editing
dotY=5 #^^  Will most likely be moved into an actor class by the unit guy
offsetX=0 #shift of the map and actors on the grid, used to pan the screen, shifted in tiles not pixels
offsetY=0 #^^
frameTime=100 #pause between frames edit here to experiment
screen=pygame.display.set_mode((tileSize*xlength+10,tileSize*ylength+10))


class tile(object):#class for tiles, mostly a placeholder/template for tile guy
    num=0 #identifies tile type, 0 for grassland, 1 for forest, 2 for water, 3 for mountain
    def __init__(self, num):#initialized with it's tile type, grassland by default
        self.num=num
    def setType(self,num):#setter for type
        self.num=num
    def color(self):#getter for color, used in display
        if self.num==0:
            return (50,200,0) #solid colors used in leiu of sprites for now, to be discussed later
        if self.num==1:
            return (0,100,0) #colors picked to make intuitively clear what the tile is
        if self.num==2:
            return (0,0,200)
        if self.num==3:
            return (50,50,50)
        return (255,255,255)#unknown tile types show up as white
    

class gMap:#class for map, comtains size information, and a list of all tiles within the map, can be saved in game and loaded
    xSize=2#default x,y size of class, not used when run
    ySize=2
    data=[]#data holds the tiles in a single list, but the setters and getters use x,y adressing, the rest of this class seems self explanatory
    def __init__(self, x, y):
        self.xSize=x
        self.ySize=y
        self.data= []
        for total in range(0,self.xSize*self.ySize):
            newTile=tile(total%4)#oh, by default, the map populates with all tile types alternating.
            self.data.append(newTile)
    def getColor(self, xInd,yInd):
        return self.data[yInd*self.xSize+xInd].color()
    def setColor(self, xInd,yInd,num):
        return self.data[yInd*self.xSize+xInd].setType(num)

def drawAll(gameMap): #not implemented correctly
    screen.fill((0,200,0))
    for x in range(0,xlength):
        for y in range(0,ylength):
            pygame.draw.rect(screen,(255-(255*(x+y)/(xlength+ylength)),255*x/xlength,255*y/ylength),(5+tileSize*x,5+tileSize*y,tileSize,tileSize),0)
            if gameMap.xSize+offsetX>x and offsetX<=x and gameMap.ySize+offsetY>y and offsetY<=y:
                 pygame.draw.rect(screen,gameMap.getColor(x-offsetX,y-offsetY),(5+tileSize*x,5+tileSize*y,tileSize,tileSize),0)
            if dotX+offsetX==x and dotY+offsetY==y:
                pygame.draw.rect(screen,(0,0,0),(5+tileSize*x,5+tileSize*y,tileSize,tileSize),0) 


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
    

    gameMap=gMap(30,20)#creates the map object, change sizes here to resize a map
    
    i=0 #closes the window after a few minutes, will be changed later
    while (i<2500):
        i+=1
        
        #take keyboard input
        pygame.event.pump()
        keypress=pygame.key.get_pressed()
        offsetX-=keypress[K_RIGHT]-keypress[K_LEFT]#arrow keys are used to pan around the world
        offsetY-=keypress[K_DOWN]-keypress[K_UP]#^^
        dotX-=keypress[K_a]-keypress[K_d]#wasd are used to move the cursor around, the black tile
        dotY-=keypress[K_w]-keypress[K_s]#^^

        #here the number keys 1-4 can be pressed while the cursor is on the map, and it will assign a new type to that tile
        if keypress[K_1] and dotY>=0 and dotY<gameMap.ySize and dotX>=0 and dotX<gameMap.xSize:
            gameMap.setColor(dotX,dotY, 0)
        if keypress[K_2] and dotY>=0 and dotY<gameMap.ySize and dotX>=0 and dotX<gameMap.xSize:
            gameMap.setColor(dotX,dotY, 1)
        if keypress[K_3] and dotY>=0 and dotY<gameMap.ySize and dotX>=0 and dotX<gameMap.xSize:
            gameMap.setColor(dotX,dotY, 2)
        if keypress[K_4] and dotY>=0 and dotY<gameMap.ySize and dotX>=0 and dotX<gameMap.xSize:
            gameMap.setColor(dotX,dotY, 3)

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
            with open("testsave.txt","wb") as fp:
                pickle.dump(gameMap, fp)
        if keypress[K_0]:
            with open("testsave.txt","rb") as fp:
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
