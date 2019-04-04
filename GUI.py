import pygame
import Config


class Button:
    name = ''
    defaultImage = None
    highlightImage = None
    pressedImage = None
    function = None
    bounds = None
    triggered = False
    arguments = None

    def __init__(self, name, defaultImage, highlightImage, function, bounds, *args):
        self.name = name
        self.defaultImage = pygame.image.load(defaultImage)
        self.highlightImage = pygame.image.load(highlightImage)
        self.function = function
        self.bounds = bounds
        self.arguments = args

    def draw(self, surface):
        if self.triggered:
            pygame.draw.rect(surface, pygame.Color(255, 0, 0), self.bounds)
        elif (self.bounds.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]
                and not self.triggered):
            pygame.draw.rect(surface, pygame.Color(255, 0, 0), self.bounds)
            self.function(self.arguments)
            self.triggered = True
        elif self.triggered and self.drawHighlight < 10:
            pygame.draw.rect(surface, pygame.Color(255, 0, 0), self.bounds)
        elif self.defaultImage.get_rect(x=self.bounds.x, y=self.bounds.y).collidepoint(pygame.mouse.get_pos()):
            surface.blit(self.highlightImage, self.bounds)
        else:
            surface.blit(self.defaultImage, self.bounds)

        if not pygame.mouse.get_pressed()[0] and self.triggered:
            self.triggered = False


class Bar:
    highlightColor = None
    barColor = None
    backgroundColor = None

    name = None

    x = 0
    y = 0

    length = 0
    height = 0

    width = 0

    def __init__(self, highlightColor, barColor, name, x, y, length, height, width=2, backgroundColor=(174, 173, 173)):
        self.highlightColor = highlightColor
        self.barColor = barColor
        self.BACKGROUND_COLOR = backgroundColor
        self.name = name
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.width = width

    def draw(self, screen, percentage):
        if percentage > 1:
            percentage = 1

        pygame.draw.rect(screen, self.highlightColor, [self.x - (self.length / 2), self.y + (self.height / 2),
                                                       self.length, self.height], self.width)

        pygame.draw.rect(screen, self.BACKGROUND_COLOR, [self.x - (self.length / 2) + self.width / 2 + 1,
                                                        self.y + (self.height / 2) + self.width / 2 + 1,
                                                        self.length - self.width - 1,
                                                        self.height - self.width - 1])

        if percentage > 0:
            pygame.draw.rect(screen, self.barColor, [self.x - (self.length / 2) + self.width / 2 + 1,
                                                     self.y + (self.height / 2) + self.width / 2 + 1,
                                                     self.length * percentage - self.width - 1 if
                                                     self.length * percentage - self.width - 1 > 0 else
                                                     self.length * percentage,
                                                     self.height - self.width - 1])


class BottomMenu:
    # Height and width members
    trueHeight = 0
    height = 0
    width = 0

    # Governs the mode for the right two panels. Each number corresponds to the numbers on the first right panel (i.e.
    # the default colony view mode is 3, as it is displayed)
    mode = 2

    # Color constants
    BACKGROUND_COLOR = pygame.Color(255, 128, 0)
    TEXT_COLOR = pygame.Color(0, 0, 0)

    # The font used by this menu
    pygame.font.init()
    font = pygame.font.Font(Config.gameFont, 20)

    # The size of boxes for displaying units and buildings. It may be dynamically resized later based on the size of the
    # screen, but for now will be a constant
    boxSize = 40

    # The index of the currently selected unit in the units list. Defaults to zero
    selectedUnit = 0

    # The number of boxes that fit into the middle box, and the starting horizontal offset. Calculated by breakBoxes()
    # during __init__
    numBoxes = 0
    horizontalOffset = 0

    # Text members. Not necessarily constants
    buildingText = font.render("1. Buildings", True, TEXT_COLOR)
    unitText = font.render("2. Units", False, TEXT_COLOR)
    colonyText = font.render("3. Colony View", True, TEXT_COLOR)

    centerText = font.render("Colony Overview", True, TEXT_COLOR)

    def __init__(self, width, height, coverage=.2):
        self.trueHeight = height
        self.height = height * (1-coverage)
        self.width = width

        self.numBoxes, self.horizontalOffset = self.breakBoxes()

    def draw(self, surface, units):
        # Drawing the rectangles to form the base of the menu
        pygame.draw.rect(surface, self.BACKGROUND_COLOR, [0, self.height, self.width / 3 - 2, self.height])
        pygame.draw.rect(surface, self.BACKGROUND_COLOR, [self.width / 3,
                                                          self.height, self.width / 3 - 2, self.height])
        pygame.draw.rect(surface, self.BACKGROUND_COLOR, [2 * self.width / 3,
                                                          self.height, self.width / 3, self.height])

        # Drawing the text on the side
        surface.blit(self.buildingText, (0, self.height))

        surface.blit(self.unitText, (0, self.height + (self.trueHeight * .2) / 3))

        surface.blit(self.colonyText, (0, self.height + 2 * (self.trueHeight * .2) / 3))

        # Drawing the center text (which can change)
        surface.blit(self.centerText, (self.center(self.centerText), self.height))

        # Conditional drawing

        # If mode==1, meaning we want the building view

        # If mode==2, meaning we want the unit view
        if self.mode == 2:
            horizontalOffset = self.horizontalOffset
            verticalOffset = 25

            for unit in units.data:
                pygame.draw.rect(surface, self.TEXT_COLOR, (self.width / 3 + horizontalOffset,
                                                            self.height + verticalOffset, self.boxSize, self.boxSize))

                if unit == units.data[self.selectedUnit]:
                    pygame.draw.rect(surface, pygame.Color(255, 0, 0), (self.width / 3 + horizontalOffset - 2,
                                     self.height + verticalOffset - 2, self.boxSize + 2, self.boxSize + 2), 2)

                horizontalOffset += 50
                if self.width / 3 + horizontalOffset + self.boxSize > 2 * self.width / 3:
                    verticalOffset += 50
                    horizontalOffset = self.horizontalOffset

    # Helper function to center text on the top of a box. Currently focuses on middle, can be expanded if needed.
    # "text" argument is the already-rendered object that is being blitted onto a surface
    def center(self, text):
        return self.width / 3 + (self.width / 3 - text.get_size()[0]) / 2

    # Method used when changing the mode. Will be accessed by events in Input.py
    def changeMode(self, mode):
        if mode == 1:
            self.mode = 1
            self.centerText = self.font.render("Building List", True, self.TEXT_COLOR)
        elif mode == 2:
            self.mode = 2
            self.centerText = self.font.render("Unit List", True, self.TEXT_COLOR)
        else:
            self.mode = 3
            self.centerText = self.font.render("Colony Overview", True, self.TEXT_COLOR)

    # Input method to change the selected unit by changing the selected unit variable. Is put into its' own function
    # to account for wrapping, and to handle up and down presses (since it is a 1-D list).
    def changeSelectedUnit(self, change, units):
        if change == 1:
            self.selectedUnit = (self.selectedUnit + 1) % len(units.data)
        elif change == -1:
            self.selectedUnit = (self.selectedUnit - 1) % len(units.data)
        elif change == 10:
            if self.selectedUnit - self.numBoxes >= 0:
                self.selectedUnit -= self.numBoxes
            elif self.selectedUnit + self.numBoxes < len(units.data):
                self.selectedUnit += self.numBoxes
        elif change == -10:
            if self.selectedUnit + self.numBoxes < len(units.data):
                self.selectedUnit += self.numBoxes
            elif self.selectedUnit - self.numBoxes >= 0:
                self.selectedUnit -= self.numBoxes

        print(self.selectedUnit)

    # Method that breaks up how many boxes will fit into the middle square, and sets the padding accordingly. Will not
    # be perfect
    def breakBoxes(self):
        count = 0
        totalSpace = 0

        while totalSpace + self.boxSize < self.width / 3:
            count += 1
            totalSpace += self.boxSize + 10

        horizontalOffset = (self.width / 3 - totalSpace) / 2

        print(count)

        return count, horizontalOffset
