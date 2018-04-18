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
        self.bitx = 0
        self.bity = 0
        self.bitw = 0
        self.bith = 0
        # states 
        self.collision = True
        self.physicalState = 1
        self.display = True
        self.pressed = False
        self.textureEnabled = True
        self.textEnabled = True
        self.physicsEnabled = False

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

t=Tile(0,0,0,45)