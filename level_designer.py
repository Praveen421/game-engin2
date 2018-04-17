
from PIL import Image, ImageDraw
from tile import *

class Level(object):

    def __init__(self):
        self.tiles = []
        self.background = Image
        self.levelCode = 1
    
    def createLevel(self,level,type):
        if type == '.json':
            pass
        if type == '.xml':
            pass
    def addTile(self,tile):
        self.tiles.add(tile)
    def _export(self):
        pass

    def _import(self):
        pass