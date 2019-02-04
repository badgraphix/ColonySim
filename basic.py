#Import and initialize
import pygame
pygame.init()
#Display
scr=pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Alt-F4 = QUIT")
#Entities

##this is where we will do most of the setting up of the assets.
bg=pygame.Surface(scr.get_size()).convert()
bg.fill((250,150,50))
fnt=pygame.font.SysFont("None",24)
lbl=fnt.render("IDEA-ALTER",1,(255,255,0))
#Action -> ALTER
################
#Assign values
clock=pygame.time.Clock()
keepGoing = True
#Loop
while keepGoing:
#Timing
    clock.tick(30)
#Events
    for evnt in pygame.event.get():
        if evnt.type==pygame.QUIT:
            keepGoing = False
#Refresh display
    scr.blit(bg,(0,0))
    scr.blit(lbl,(100,100))
    pygame.display.flip()
