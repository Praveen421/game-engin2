
from PIL import Image

class Pointer():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = [254,254,254]
        self.image = Image
        # states 
        self.collision = True
        self.physicalState = 1
        self.display = True
        self.pressed = False
        self.textureEnabled = True
        self.textEnabled = True
        self.physicsEnabled = False
    def setImage(self,image):
        self.image = image
    def setPos(self,x,y):
        self.x = x
        self.y = y
    def setWidth(self,width):
        self.width = width
    def setHeight(self,height):
        self.height = height
    