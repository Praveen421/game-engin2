
import pygame

from level_designer import *
from pointer import *

'''
==========================================
    colors class
==========================================
'''  
class colors(object):
    def __init__(self):
        self.WHITE = (254,254,254)
        self.BLACK = (0,0,0)
        self.RED = (254,0,0)
        self.BLUE = (0,0,254)
        self.GREEN = (0,254,0)
        self.GRAY = (100,100,100)
        self.YELLOW = (254,254,0)
        self.MAGENTA = (254,0,254)

def display():
    global pointer
    pygame.draw.rect(screen,color.RED,(int(pointer.x),int(pointer.y),int(pointer.width),int(pointer.height)))

    for t in level.tiles:
        pygame.draw.rect(screen,color.RED,(int(.x),int(pointer.y),int(pointer.width),int(pointer.height)))

def _input(mouse_rel,mouse_key):
    global level,Layers
    # loop through the events
    for event in pygame.event.get():
        #check if the event is the x button
        if event.type == pygame.QUIT:
            #if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pgame.K_LEFT:
                pass
            if event.key == pgame.K_RIGHT:
                pass
    if(mouse_key[0]):
        # getting the current position of the mouse 
        p = pygame.mouse.get_pos()
        # convert the screen coordinates to world co-ordinates
        level.addTile(pointer)

def pointerUpdate():
    global pointer

    p = pygame.mouse.get_pos()
    # convert the screen coordinates to world co-ordinates
    pointer.x = p[0]
    pointer.y = p[1]



window = (900,600)
pygame.init()
screen = pygame.display.set_mode(window)
clock = pygame.time.Clock()
color = colors()




pos = pygame.mouse.get_pos()
pointer = Pointer(pos[0],pos[1],70,70)

Layers = []

level = Level()



while True:
   
    screen.fill(color.BLACK)
    # setting the smallest time variation
    dt = float(clock.tick(60))/1000
    clock.tick(60)


    pointerUpdate()
    
    display()

    
    mouse_rel = pygame.mouse.get_rel()
    mouse_buttons = pygame.mouse.get_pressed()
    _input(mouse_rel,mouse_buttons)
    
    
    pygame.display.update()


    

    








