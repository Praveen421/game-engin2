'''
MIT License

Copyright (c) 2018 sidd5sci

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
from PIL import Image
import pygame,math,time,os
import importlib
#from layer import *
#from pointer import *
#from camera import *


'''
==========================================
    colors class
==========================================
'''  
class colors(object):
    def __init__(self):
        self.WHITE = (254,254,254)
        self.BLACK = (0,0,0)
        self.RED = (254,0,0,128)
        self.BLUE = (0,0,254)
        self.GREEN = (0,254,0)
        self.GRAY = (100,100,100)
        self.YELLOW = (254,254,0)
        self.MAGENTA = (254,0,254)

class Node():
    def __init__(self,*args,**kwargs):
        # initilize the pygame
        pygame.init()
        # screen height and width
        self.width ,self.height = 800,600
        # center of the screen | environment cooords
        self.cx,self.cy,self.cz = self.width/2,self.height/2, -5
        # loading the icon  
        #pygame.display.set_icon(pygame.image.load('Icon.png'))
        # init the name of the window
        pygame.display.set_caption("PyTrack | v1.0.1")
        # initilise the clock
        self.clock = pygame.time.Clock()
        # initilize the screen 
        # ,pygame.DOUBLEBUF,pygame.SRCALPHA
        self.screen = pygame.display.set_mode((self.width,self.height),pygame.SRCALPHA, 32)
        #self.screen.set_alpha(254)
        #print(self.screen.get_alpha())
        self.screen.fill(pygame.Color(255,255,255))
        pygame.display.init()
        pygame.display.update()
        # graphics mode
        self.color = colors()
    def main(self):
        pass

if __name__ == "__main__":
    n = Node(6)
    n.main()