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
        self.backgroundColor = backgroundColor
        self.name = name
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.width = width

    def draw(self, screen, percentage):
        if percentage > 1:
            percentage = 1

        pygame.draw.rect(screen, self.highlightColor, [self.x, self.y,
                                                       self.length, self.height], self.width)

        pygame.draw.rect(screen, self.backgroundColor, [self.x + self.width / 2 + 1,
                                                        self.y + self.width / 2 + 1,
                                                        self.length - self.width - 1,
                                                        self.height - self.width - 1])

        if percentage > 0:
            pygame.draw.rect(screen, self.barColor, [self.x + self.width / 2 + 1,
                                                     self.y + self.width / 2 + 1,
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
    mode = 3

    # Color constants
    BACKGROUND_COLOR = pygame.Color(255, 128, 0)
    TEXT_COLOR = pygame.Color(0, 0, 0)

    # Spacing constants
    TEXT_OFFSET = 25

    # Setting the fonts used by this menu (A larger font for the three items on the side, one for the middle text, and one
    # the bar labels
    pygame.font.init()
    leftFont = None
    middleFont = None
    rightFont = None

    # The size of boxes for displaying units and buildings. It may be dynamically resized later based on the size of the
    # screen, but for now will be a constant
    boxSize = 40

    # The index of the currently selected unit in the units list. Defaults to zero
    selectedUnit = 0

    # The progress bar used to display unit health, and building health
    topBar = None

    # The progress bar used to display unit hunger, and building capacity
    middleBar = None

    # The progress bar used to display unit thirst

    # The number of boxes that fit into the middle box, the starting horizontal offset, and the starting
    # vertical offset. Calculated by breakBoxes() during __init__
    numRows = 0
    numColumns = 0
    horizontalOffset = 0
    verticalOffset = 0

    # The index of the first visible box
    firstVisibleBox = 0

    # Text members. Not necessarily constants
    buildingText = None
    unitText = None
    colonyText = None

    centerText = None

    healthText = None
    hungerText = None
    thirstText = None

    # Sizing and spacing variables for determining the drawing of items on the menu
    barHeight = 0
    menuHeight = 0

    def __init__(self, width, height, coverage=.2):
        self.trueHeight = height
        self.height = height * (1 - coverage)
        self.width = width

        self.barHeight = self.height / 24
        self.menuHeight = self.trueHeight - self.height

        spacing = self.calculateVerticalSpacing(4, self.barHeight)

        self.numRows, self.numColumns, self.horizontalOffset, self.verticalOffset = self.breakBoxes()

        self.topBar = Bar(self.TEXT_COLOR, pygame.Color(0, 255, 0), "Top Bar", (2 * self.width / 3) + self.width / 120,
                          self.height + spacing, self.width / 6, self.barHeight)
        self.middleBar = Bar(self.TEXT_COLOR, pygame.Color(0, 255, 0), "Top Bar", (2 * self.width / 3) + self.width / 120,
                          self.height + 2 * spacing + self.height / 32, self.width / 6, self.barHeight)
        self.bottomBar = Bar(self.TEXT_COLOR, pygame.Color(0, 255, 255), "Top Bar", (2 * self.width / 3) + self.width / 120,
                          self.height + 3 * spacing + 2 * self.height / 32, self.width / 6, self.barHeight)

        self.leftFont = pygame.font.Font(Config.gameFont, self.sizeFont(self.menuHeight / 3, self.width / 3, "1. Buildings"))
        self.buildingText = self.leftFont.render("1. Buildings", True, self.TEXT_COLOR)
        self.unitText = self.leftFont.render("2. Units", True, self.TEXT_COLOR)
        self.colonyText = self.leftFont.render("3. Colony View", True, self.TEXT_COLOR)

        self.middleFont = pygame.font.Font(Config.gameFont, self.sizeFont(self.verticalOffset + self.TEXT_OFFSET, self.width / 3, "Colony Overview"))
        self.centerText = self.middleFont.render("Colony Overview", True, self.TEXT_COLOR)

        self.rightFont = pygame.font.Font(Config.gameFont, self.sizeFont(self.width / 24, self.height / 6, "Hunger"))
        self.healthText = self.rightFont.render("Health", True, self.TEXT_COLOR)
        self.hungerText = self.rightFont.render("Hunger", True, self.TEXT_COLOR)
        self.thirstText = self.rightFont.render("Thirst", True, self.TEXT_COLOR)

    def draw(self, surface, units, buildings):
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

        # If mode == 1, meaning we want the building view
        if self.mode == 1:
            horizontalOffset = self.horizontalOffset
            verticalOffset = self.verticalOffset

            for i in range(self.firstVisibleBox, self.firstVisibleBox + (self.numColumns * self.numRows)
            if self.firstVisibleBox + (self.numColumns * self.numRows) < len(buildings.data)
            else len(buildings.data)):
                pygame.draw.rect(surface, self.TEXT_COLOR, (self.width / 3 + horizontalOffset,
                                                            self.height + self.TEXT_OFFSET + verticalOffset,
                                                            self.boxSize, self.boxSize))

                if buildings.data[i] == buildings.data[self.selectedUnit]:
                    pygame.draw.rect(surface, pygame.Color(255, 0, 0), (self.width / 3 + horizontalOffset - 2,
                                                                        self.height + self.TEXT_OFFSET + verticalOffset - 2,
                                                                        self.boxSize + 2, self.boxSize + 2), 2)

                    self.topBar.draw(surface, buildings.data[i].hitPoints / Config.MAX_UNIT_HUNGER)
                    self.middleBar.draw(surface, buildings.data[i].inventory[0] / Config.MAX_UNIT_HUNGER)

                    textX = self.topBar.x + self.width / 6 + self.width / 72
                    surface.blit(self.healthText, (textX, self.topBar.y - self.barHeight / 4))
                    surface.blit(self.hungerText, (textX, self.topBar.y - self.barHeight / 4 +
                                                   self.middleBar.y - self.topBar.y))

                horizontalOffset += 50
                if self.width / 3 + horizontalOffset + self.boxSize > 2 * self.width / 3:
                    verticalOffset += 50
                    horizontalOffset = self.horizontalOffset

        # If mode == 2, meaning we want the unit view
        if self.mode == 2:
            horizontalOffset = self.horizontalOffset
            verticalOffset = self.verticalOffset

            for i in range(self.firstVisibleBox, self.firstVisibleBox + (self.numColumns * self.numRows)
                    if self.firstVisibleBox + (self.numColumns * self.numRows) < len(units.data)
                    else len(units.data)):
                pygame.draw.rect(surface, self.TEXT_COLOR, (self.width / 3 + horizontalOffset,
                                                            self.height + self.TEXT_OFFSET + verticalOffset,
                                                            self.boxSize, self.boxSize))

                if units.data[i] == units.data[self.selectedUnit]:
                    pygame.draw.rect(surface, pygame.Color(255, 0, 0), (self.width / 3 + horizontalOffset - 2,
                                                                        self.height + self.TEXT_OFFSET + verticalOffset - 2,
                                                                        self.boxSize + 2, self.boxSize + 2), 2)

                    self.topBar.draw(surface, units.data[i].hitPoints / Config.MAX_UNIT_HUNGER)
                    self.middleBar.draw(surface, units.data[i].hungerPoints / Config.MAX_UNIT_HUNGER)
                    self.bottomBar.draw(surface, units.data[i].thirstPoints / Config.MAX_UNIT_HUNGER)

                    textX = self.topBar.x + self.width / 6 + self.width / 72
                    surface.blit(self.healthText, (textX, self.topBar.y - self.barHeight / 4))
                    surface.blit(self.hungerText, (textX, self.topBar.y - self.barHeight / 4 +
                                                   self.middleBar.y - self.topBar.y))
                    surface.blit(self.thirstText, (textX, self.topBar.y - self.barHeight / 4 +
                                                   self.bottomBar.y - self.topBar.y))

                    behaviorBoxDimension = self.height / 16

                    pygame.draw.rect(surface, pygame.Color(0, 153, 30), (self.bottomBar.x,
                                                                          self.bottomBar.y + self.barHeight +
                                                                          self.calculateVerticalSpacing(4, self.barHeight) / 2,
                                                                          behaviorBoxDimension, behaviorBoxDimension))
                    pygame.draw.rect(surface, pygame.Color(0, 0, 0), (self.bottomBar.x + self.barHeight + (self.width / 6 - (4 * self.barHeight)) / 4,
                                                                         self.bottomBar.y + self.barHeight +
                                                                         self.calculateVerticalSpacing(4, self.barHeight) / 2,
                                                                         behaviorBoxDimension, behaviorBoxDimension))
                    pygame.draw.rect(surface, pygame.Color(255, 0, 0), (self.bottomBar.x + 2 * self.barHeight +
                                                                         2 * (self.width / 6 - (4 * self.barHeight)) / 4,
                                                                         self.bottomBar.y + self.barHeight +
                                                                         self.calculateVerticalSpacing(4, self.barHeight) / 2,
                                                                         behaviorBoxDimension, behaviorBoxDimension))
                    pygame.draw.rect(surface, pygame.Color(0, 0, 102), (self.bottomBar.x + 3 * self.barHeight +
                                                                         3 * (self.width / 6 - (4 * self.barHeight)) / 4,
                                                                         self.bottomBar.y + self.barHeight +
                                                                         self.calculateVerticalSpacing(4, self.barHeight) / 2,
                                                                         behaviorBoxDimension, behaviorBoxDimension))
                    pygame.draw.rect(surface, pygame.Color(192, 192, 192), (self.bottomBar.x + units.data[i].behavior * self.barHeight +
                                                                        units.data[i].behavior * (self.width / 6 - (4 * self.barHeight)) / 4,
                                                                        self.bottomBar.y + self.barHeight +
                                                                        self.calculateVerticalSpacing(4, self.barHeight) / 2,
                                                                        behaviorBoxDimension, behaviorBoxDimension), 4)

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
            self.centerText = self.middleFont.render("Building List", True, self.TEXT_COLOR)

            spacing = self.calculateVerticalSpacing(2, self.barHeight)

            self.topBar = Bar(self.TEXT_COLOR, pygame.Color(0, 255, 0), "Top Bar",
                              (2 * self.width / 3) + self.width / 120,
                              self.height + spacing - spacing / 2, self.width / 6, self.barHeight)
            self.middleBar = Bar(self.TEXT_COLOR, pygame.Color(0, 255, 0), "Top Bar",
                                 (2 * self.width / 3) + self.width / 120,
                                 self.height + spacing + self.height / 24 + self.height / 48,
                                 self.width / 6, self.barHeight)

            self.rightFont = pygame.font.Font(Config.gameFont,
                                              self.sizeFont(self.width / 24, self.height / 6, "Hunger"))
            self.healthText = self.rightFont.render("Health", True, self.TEXT_COLOR)
            self.hungerText = self.rightFont.render("Inventory", True, self.TEXT_COLOR)

        elif mode == 2:
            self.mode = 2
            self.centerText = self.middleFont.render("Unit List", True, self.TEXT_COLOR)

            spacing = self.calculateVerticalSpacing(4, self.barHeight)

            self.topBar = Bar(self.TEXT_COLOR, pygame.Color(0, 255, 0), "Top Bar",
                              (2 * self.width / 3) + self.width / 120,
                              self.height + spacing, self.width / 6, self.barHeight)
            self.middleBar = Bar(self.TEXT_COLOR, pygame.Color(0, 255, 0), "Top Bar",
                                 (2 * self.width / 3) + self.width / 120,
                                 self.height + 2 * spacing + self.height / 32, self.width / 6, self.barHeight)
            self.bottomBar = Bar(self.TEXT_COLOR, pygame.Color(0, 255, 255), "Top Bar",
                                 (2 * self.width / 3) + self.width / 120,
                                 self.height + 3 * spacing + 2 * self.height / 32, self.width / 6, self.barHeight)

            self.rightFont = pygame.font.Font(Config.gameFont,
                                              self.sizeFont(self.width / 24, self.height / 6, "Hunger"))
            self.healthText = self.rightFont.render("Health", True, self.TEXT_COLOR)
            self.hungerText = self.rightFont.render("Hunger", True, self.TEXT_COLOR)
            self.thirstText = self.rightFont.render("Thirst", True, self.TEXT_COLOR)

        else:
            self.mode = 3
            self.centerText = self.middleFont.render("Colony Overview", True, self.TEXT_COLOR)

    # Input method to change the selected unit by changing the selected unit variable. Is put into its' own function
    # to account for wrapping, and to handle up and down presses (since it is a 1-D list).
    def changeSelectedUnit(self, change, units):
        if change == 1:
            self.selectedUnit = (self.selectedUnit + 1)
            if self.selectedUnit >= len(units.data):
                self.selectedUnit = 0
                self.firstVisibleBox = 0
            elif self.selectedUnit >= self.firstVisibleBox + (self.numColumns * self.numRows):
                self.firstVisibleBox += self.numColumns

        elif change == -1:
            self.selectedUnit = (self.selectedUnit - 1)
            if self.selectedUnit < 0:
                self.selectedUnit = len(units.data) - 1
                if len(units.data) > self.numColumns * self.numRows:
                    self.firstVisibleBox = self.numColumns * (len(units.data) // self.numColumns)
            elif self.selectedUnit < self.firstVisibleBox:
                self.firstVisibleBox -= self.numColumns

        elif change == -10:
            self.selectedUnit -= self.numColumns

            if self.selectedUnit < self.firstVisibleBox:
                if self.selectedUnit < 0:
                    if self.numColumns + self.selectedUnit + self.numColumns * \
                            (len(units.data) // self.numColumns) < len(units.data):
                        self.firstVisibleBox = self.numColumns * (len(units.data) // self.numColumns)
                        self.selectedUnit = self.numColumns + self.selectedUnit + self.numColumns * \
                                            (len(units.data) // self.numColumns)
                    else:
                        self.selectedUnit += self.numColumns

                else:
                    self.firstVisibleBox -= self.numColumns

        elif change == 10:
            self.selectedUnit += self.numColumns

            if self.selectedUnit >= self.firstVisibleBox + (self.numColumns * self.numRows):
                if self.numColumns * (len(units.data) // self.numColumns) <= \
                        self.selectedUnit - self.numColumns < len(units.data):

                    self.firstVisibleBox = 0
                    self.selectedUnit = (self.selectedUnit - self.numColumns) % self.numColumns
                elif self.selectedUnit <= len(units.data):
                    self.firstVisibleBox += self.numColumns
                else:
                    self.selectedUnit -= self.numColumns
            elif self.selectedUnit >= len(units.data):
                self.selectedUnit -= self.numColumns

    # Method that breaks up how many boxes will fit into the middle square, and sets the padding accordingly. Will not
    # be perfect
    def breakBoxes(self):
        columns = 0
        totalSpace = 0

        while totalSpace + self.boxSize + 10 < self.width / 3:
            columns += 1
            totalSpace += self.boxSize + 10

        horizontalOffset = (self.width / 3 - totalSpace) / 2

        totalSpace = 25
        rows = 0

        while totalSpace + self.boxSize < self.menuHeight:
            rows += 1
            totalSpace += self.boxSize + 10

        verticalOffset = (self.menuHeight - totalSpace) / 2

        return rows, columns, horizontalOffset, verticalOffset

    # Method used to determine vertical spacing between objects of equal size
    def calculateVerticalSpacing(self, numObjects, objectHeight):
        return (self.menuHeight - objectHeight * numObjects) / numObjects

    # Method that sizes a font to maximally fill out a given space
    def sizeFont(self, verticalSpace, horizontalSpace, renderText):
        size = 10
        testFont = pygame.font.Font(Config.gameFont, size)
        testText = testFont.render(renderText, True, self.TEXT_COLOR)

        while testFont.get_linesize() < verticalSpace and testText.get_width() < horizontalSpace - horizontalSpace * .05:
            size += 1
            testFont = pygame.font.Font(Config.gameFont, size)
            testText = testFont.render(renderText, True, self.TEXT_COLOR)

        return size
