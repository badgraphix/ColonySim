import pygame


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

        pygame.draw.rect(screen, self.highlightColor, [self.x - (self.length / 2), self.y + (self.height / 2),
                                                       self.length, self.height], self.width)

        pygame.draw.rect(screen, self.backgroundColor, [self.x - (self.length / 2) + self.width / 2 + 1,
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
