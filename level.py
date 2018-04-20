
from PIL import Image, ImageDraw
from tile import *
import json

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
        self.tiles.append(tile)
    
    def _export(self):
        file_ = open("level.json","w+")

        string_ = '{Tiles:['
        for t in self.tiles:
            s = '{x:'+str(t.x)+',y:'+str(t.y)+',w:'+str(t.width)+',h:'+str(t.height)
            s += ',color:[254,254,254,254],collision:False,display:true}'
            string_ += s+','
        string_ += ']}'

        print string_
        file_.write(string_)
        file_.close()
    def _import(self):
        pass