
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
from PIL import Image, ImageDraw
from tile import *
import json

class Layer(object):

    def __init__(self):
        self.tiles = []
        self.background = Image
        self.layerCode = 1
    
    def createLayer(self,layer,type):
        if type == '.json':
            pass
        if type == '.xml':
            pass

    def checkCollision(x,y):
        FlagedTiles = []
        for t in self.tiles:
            if x > t.x and x < t.x+t.width:
                if y > t.y and y < t.y+t.height:
                    FlagedTiles.append(t)
                    t.textureEnabled = False
        return FlagedTiles

    def addTile(self,tile):
        self.tiles.append(tile)
    
    def addTileAtStart(self,tile):
        self.tiles.reverse()
        self.tiles.append(tile)
        self.tiles.reverse()
    def removeRecentTile(self):
        del self.tiles[-1]
    def _export(self):
        file_ = open("layer.json","w+")
                   
        string_ = '{Tiles:['
        for t in self.tiles:
            s = '{x:'+str(t.x)+',y:'+str(t.y)+',w:'+str(t.width)+',h:'+str(t.height)+',text:anything'
            s += ',color:[254,'+str(t.color[0])+','+str(t.color[1])+','+str(t.color[2])+'],collision:'+str(t.collision)+',display:'+str(t.display)
            s += ',spriteEnabled:'+str(t.textureEnabled)
            s += ',sprite:'+str(t.textureName)+',bitx:'+str(t.fx)+',bity:'+str(t.fy)+',bitw:'+str(t.fWidth)+',bith:'+str(t.fHeight)+',widthRatio:1,heightRatio:1}'
            string_ += s+','
        string_ += ']}'

        print (string_)
        file_.write(string_)
        file_.close()
    def _import(self):
        pass
