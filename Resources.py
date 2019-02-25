class ResourceManager:
    # This list should be used exclusively to store all wood-holding buildings/tiles. It must be updated by some kind
    # of world event. It should be updated using the corresponding method.
    woodStorage = list()

    # For now, will accept any input. Will be changed to reject all non-wood-bearing input, improved or unimproved, once
    # the tile or building teams have finished their work.
    def addWoodBuilding(self, building):
        self.woodStorage.append(building)

    def removeWoodBuilding(self, building):
        self.woodStorage.remove(building)

    def getTotalWood(self):
        total = 0

        for building in self.woodStorage:
            total += building.currentStorage

        return total

    # This list should be used exclusively to store all food-holding buildings/tiles. It must be updated by some kind
    # of world event. It should be updated using the corresponding method.
    foodStorage = list()

    # For now, will accept any input. Will be changed to reject all non-food-bearing input, improved or unimproved, once
    # the tile or building teams have finished their work.
    def addFoodBuilding(self, building):
        self.foodStorage.append(building)

    def removeFoodBuilding(self, building):
        self.woodStorage.remove(building)

    def getTotalFood(self):
        total = 0

        for building in self.foodStorage:
            total += building.currentStorage

        return total


class ResourceBuilding:
    resourceType = ''
    maxCapacity = 0
    currentStorage = 0
    name = ''

    # Default constructor. Defaults to a wooden building with a max capacity of 500.
    def __init__(self):
        self.resourceType = "WOOD"
        self.maxCapacity = 500
        self.currentStorage = 0
        self.name = "Wood Shed"

    def __init__(self, resourceType, maxCapacity, currentStorage, name):
        self.resourceType = resourceType
        self.maxCapacity = maxCapacity
        self.currentStorage = currentStorage
        self.name = name

    # The argument quantity is how much you want to put in or take out. Negative arguments take items out. The function
    # then returns how much can be taken or removed
    def interactWithStorage(self, quantity):
        if(self.currentStorage + quantity) < 0:
            returnVal = self.currentStorage
            self.currentStorage = 0
            return returnVal
        elif(self.currentStorage + quantity) > self.maxCapacity:
            returnVal = quantity - (self.currentStorage + quantity - self.maxCapacity)
            self.currentStorage = self.maxCapacity
            return -returnVal
        else:
            self.currentStorage += quantity
            return -quantity
