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

class Tile(object):
    def __init__(self,x,y,width,height):
        
        # rectangle position 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # frame details
        self.fx = 0
        self.fy = 0
        self.fWidth = 100
        self.fHeight = 100
        # color
        self.color = []
        # text
        self.text = ""
        # texture
        self.texture = Image
        self.textureName = ''
        # states 
        self.collision = True
        self.physicalState = 1
        self.display = True
        self.pressed = False
        self.textureEnabled = True
        self.textEnabled = True
        self.physicsEnabled = False
        self.selected = True

    def setImage(self,texture):
        self.texture = texture
    def setFrame(self,fx,fy,fwidth,fheight):
        self.fx = fx
        self.fy = fy
        self.fWidth = fwidth
        self.fHeight = fheight

    def rect(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def equal(self,t):
        if t.x == self.x:
            if t.y == self.y:
                if t.width == self.width:
                    if t.height == self.height:
                        if t.textureName == self.textureName:
                            if t.fx == self.fx:
                                if t.fy == self.fy:
                                    return 1
                                else: return 0
                            else: return 0    
                        else: return 0
                    else: return 0
                else: return 0
            else: return 0
        else: return 0
if __name__ == "__main__":
    t=Tile(0,0,0,45)
