class tile(object):  # class for tiles, mostly a placeholder/template for tile guy

    tileType = 0  # identifies tile type, 0 for grassland, 1 for forest, 2 for water, 3 for mountain, 4 for farmland
    numWater = 0
    numStone= 0
    numWood = 0
    numFood = 0
    traversable = 1
    stationedUnitID = -1 # -1 means no unit is occupying this tile

    def __init__(self, tileType, numWater, numStone, numWood, numFood, traversable):  # initialized with it's tile type, grassland by default
        self.tileType = tileType
        self.numWater = 50
        self.numStone = numStone
        self.numWood = numWood
        self.numFood = numFood
        self.traversable = traversable

    def setType(self, tileType):  # setter for type
        self.tileType = tileType
        if self.tileType == 0:  # 0 for Grassland
            self.numWater = 0
            self.numStone = 0
            self.numWood = 0
            self.numFood = 0
            self.traversable = 1
        if self.tileType == 1:  # 1 for Forest
            self.numWater = 0
            self.numStone = 0
            self.numWood = 50
            self.numFood = 0
            self.traversable = 1
        if self.tileType == 2:  # 2 for Water
            self.numWater = 50
            self.numStone = 0
            self.numWood = 0
            self.numFood = 0
            self.traversable = 0
        if self.tileType == 3:  # 3 for Mountain
            self.numWater = 0
            self.numStone = 50
            self.numWood = 0
            self.numFood = 0
            self.traversable = 0
        if self.tileType == 4:  # 4 for Farmland
            self.numWater = 0
            self.numStone = 0
            self.numWood = 0
            self.numFood = 50
            self.traversable = 0

    def getType(self):
        return self.tileType

    def color(self):  # getter for color, used in display
        if self.tileType == 0:
            return (50, 200, 0)  # solid colors used in leiu of sprites for now, to be discussed later
        if self.tileType == 1:
            return (0, 100, 0)  # colors picked to make intuitively clear what the tile is
        if self.tileType == 2:
            return (0, 0, 200)
        if self.tileType == 3:
            return (50, 50, 50)
        if self.tileType == 4:  # not implemented, maybe farmland
            return (100, 100, 0)
        return (255, 255, 255)  # unknown tile types show up as white

    def collectResource(self, amount):
        if self.tileType == 1:
            if self.numWood >= amount:
                self.numWood = self.numWood - amount
                return (self.tileType, amount)
            else:
                amountRetrieved = self.numWood
                self.numWood = 0
                return (self.tileType, amountRetrieved)
        if self.tileType == 2:
            if self.numWater >= amount:
                self.numWater = self.numWater - amount
                return (self.tileType, amount)
            else:
                amountRetrieved = self.numWater
                self.numWater = 0
                return (self.tileType, amountRetrieved)
        if self.tileType == 3:
            if self.numStone >= amount:
                self.numStone = self.numStone - amount
                return (self.tileType, amount)
            else:
                amountRetrieved = self.numStone
                self.numStone = 0
                return (self.tileType, amountRetrieved)
        if self.tileType == 4:
            if self.numFood >= amount:
                self.numFood = self.numFood - amount
                return (self.tileType, amount)
            else:
                amountRetrieved = self.numFood
                self.numFood = 0
                return (self.tileType, amountRetrieved)
        else:
            return (0, 0)
    def setStationedUnitID(self, unitID):
        self.stationedUnitID = unitID
    def getStationedUnitID(self):
        return self.stationedUnitID
