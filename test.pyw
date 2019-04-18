# Import and initialize
import pygame
import Config
import Unit
import building
import GUI

from pygame.locals import *


import random

pygame.init()
# Display
scr = pygame.display.set_mode((640, 480))
#scr = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Alt-F4 = QUIT")
# Entities
black = [0, 0, 0]
green = [0, 255, 0]

fnt = pygame.font.SysFont("None", 24)
lbl = fnt.render("IDEA-ALTER", 1, (255, 255, 0))

actors = Unit.Actor(5, Config.actorsx, Config.actorsy)
buildings = building.Actor(5, Config.actorsx, Config.actorsy)

for unit in actors.data:
    unit.hungerPoints = random.randint(0, 100)
    unit.behavior = random.randint(0, 3)


bot = GUI.BottomMenu(640, 480)
#bot = GUI.BottomMenu(1280, 720)
# Action -> ALTER
################
# Assign values
clock = pygame.time.Clock()
keepGoing = True
total = 0.024

# Loop
while keepGoing:
    # Timing
    clock.tick(60)
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
    # Refresh display
    scr.fill((0, 0, 0))
    bot.draw(scr, actors, buildings)

    pygame.event.pump()
    keys = pygame.key.get_pressed()

    if keys[K_1]:
        bot.changeMode(1)
    if keys[K_2]:
        bot.changeMode(2)
    if keys[K_3]:
        bot.changeMode(3)

    if keys[K_RIGHT]:
        bot.changeSelectedUnit(1, actors)
    if keys[K_LEFT]:
        bot.changeSelectedUnit(-1, actors)
    if keys[K_UP]:
        bot.changeSelectedUnit(-10, actors)
    if keys[K_DOWN]:
        bot.changeSelectedUnit(10, actors)

    pygame.display.flip()
    pygame.time.wait(100)
