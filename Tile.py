class tile(object):#class for tiles, mostly a placeholder/template for tile guy
    
    tileType = 0 #identifies tile type, 0 for grassland, 1 for forest, 2 for water, 3 for mountain, 4 for farmland
    numWater = 0
    numFood = 0
    numWood = 0
    traversable = 1
    def __init__(self, tileType, numWater, numFood, numWood, traversable):#initialized with it's tile type, grassland by default
        self.tileType=tileType
        self.numWater = numWater
        self.numFood = numFood
        self.numWood = numWood
        self.traversable = traversable
        
    def setType(self,tileType):#setter for type
        self.tileType = tileType
        if self.tileType == 0: #0 for Grassland
            self.numWater = 0
            self.numFood = 0
            self.numWood = 0
            self.traversable = 1
        if self.tileType == 1: #1 for Forest
            self.numWater = 0
            self.numFood = 0
            self.numWood = 50
            self.traversable = 1
        if self.tileType == 2: #2 for Water
            self.numWater = 50
            self.numFood = 0
            self.numWood = 0
            self.traversable = 0
        if self.tileType == 3: #3 for Mountain
            self.numWater = 0
            self.numFood = 0
            self.numWood = 0
            self.traversable = 0
        if self.tileType == 4: #4 for Farmland
            self.numWater = 0
            self.numFood = 50
            self.numWood = 0
            self.traversable = 1
            
    def getType(self):
        return self.tileType
    
    def color(self):#getter for color, used in display
        if self.tileType==0:
            return (50,200,0) #solid colors used in leiu of sprites for now, to be discussed later
        if self.tileType==1:
            return (0,100,0) #colors picked to make intuitively clear what the tile is
        if self.tileType==2:
            return (0,0,200)
        if self.tileType==3:
            return (50,50,50)
        if self.tileType==4:#not implemented, maybe farmland
            return (100,100,0)
        return (255,255,255)#unknown tile types show up as white
