#Name
#CSC 305
#Colony Sim Game: Tile
#2/22/2019

class tile(object):#class for tiles, mostly a placeholder/template for tile guy
    num=0 #identifies tile type, 0 for grassland, 1 for forest, 2 for water, 3 for mountain
    def __init__(self, num):#initialized with it's tile type, grassland by default
        self.num=num
    def setType(self,num):#setter for type
        self.num=num
    def getType(self):
        return self.num
    def color(self):#getter for color, used in display
        if self.num==0:
            return (50,200,0) #solid colors used in leiu of sprites for now, to be discussed later
        if self.num==1:
            return (0,100,0) #colors picked to make intuitively clear what the tile is
        if self.num==2:
            return (0,0,200)
        if self.num==3:
            return (50,50,50)
        if self.num==4:#not implemented, maybe farmland
            return (100,100,0)
        return (255,255,255)#unknown tile types show up as white
    

