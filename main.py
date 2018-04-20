
import pygame,math,time,os
from level import *
from pointer import *
from camera import *


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


class Rect(object):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def get(self):
        return (self.x,self.y,self.w+self.x,self.h+self.y)
def screenToWorld(cords):
    global pixelFactor,scalex,scaley
    x,y,z = cords[0],cords[1],0
    
    #x,y = x/pixelFactor,y/pixelFactor
    #x,y = scalex/2+x,scaley/2+y
    x,y = x+cam.pos[0],y+cam.pos[1]
    return [x,y,z]
def worldToScreen(cords):
    global pixelFactor,cx,cy
    x,y,z = cords[0],cords[1],cords[2]
    
    x,y,z = x-cam.pos[0],y-cam.pos[1],z+cam.pos[2]
    #pixelFactor = (pixelFactor*cam.pos[2])/z
    #f = 200/z
    #x,y = x*pixelFactor,y*pixelFactor
    #x,y = x*f,y*f
    #x,y = cx+int(x),cy+int(y)
    #x,y = scalex/2+x,scaley/2+y
    return [int(x),int(y)]

def display():
    global pointer, layer_0,Layer,cam,sprit
       
    for t in layer_0.tiles:        
        x,y = worldToScreen([t.x,t.y,50])
        if t.textureEnabled:
            screen.blit(convertPILtoPygame(t.texture),(int(x),int(y)))
        else:
            pygame.draw.rect(screen,color.RED,(int(x),int(y),int(t.width),int(t.height)))
    
    if pointer.textureEnabled:
        screen.blit(convertPILtoPygame(pointer.image),(int(pointer.x),int(pointer.y)))
    else:
        pygame.draw.rect(screen,color.RED,(int(pointer.x),int(pointer.y),int(pointer.width),int(pointer.height)))
    

def assetsLoader(sprit):
    global assets

    r1 = Rect(30,170,100,120)
    r2 = Rect(140,180,40,50)
    r3 = Rect(40,20,100,90)
    r4 = Rect(40,120,60,40)
    r5 = Rect(140,100,40,60)
    r6 = Rect(140,240,40,30)
    r7 = Rect(190,40,125,120)#tree
    r8 = Rect(190,180,50,45)
    r9 = Rect(190,240,35,65)
    r10 = Rect(250,180,40,45)
    r11 = Rect(240,240,65,30)
    r12 = Rect(320,40,65,100)
    r13 = Rect(400,40,15,100)
    r14 = Rect(430,40,60,100)
       
    assets.append(sprit.crop(r1.get()))
    assets.append(sprit.crop(r2.get()))
    assets.append(sprit.crop(r3.get()))
    assets.append(sprit.crop(r4.get()))
    assets.append(sprit.crop(r5.get()))
    assets.append(sprit.crop(r6.get()))
    assets.append(sprit.crop(r7.get()))
    assets.append(sprit.crop(r8.get()))
    assets.append(sprit.crop(r9.get()))
    assets.append(sprit.crop(r10.get()))
    assets.append(sprit.crop(r11.get()))
    assets.append(sprit.crop(r12.get()))
    assets.append(sprit.crop(r13.get()))
    assets.append(sprit.crop(r14.get()))
 
    
    

def convertPILtoPygame(image):
    mode = image.mode
    size = image.size
    data = image.tobytes()
    return pygame.image.fromstring(data, size, mode)

def _input(dt,mouse_rel,mouse_key):
    global layer_0,Layers,cam,sentToBack,currentPointerAssets,assets
    # loop through the events
    for event in pygame.event.get():
        #check if the event is the x button
        if event.type == pygame.QUIT:
            #if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                cam.update(dt,"back")
            if event.key == pygame.K_UP:
                cam.update(dt,"front")
            if event.key == pygame.K_LEFT:
                cam.update(dt,"left")
            if event.key == pygame.K_RIGHT:
                cam.update(dt,"right")
            if event.key == pygame.K_RCTRL:
                pass
            if event.key == pygame.K_c:
                if currentPointerAssets < len(assets):
                    currentPointerAssets = currentPointerAssets+1
                if currentPointerAssets >= len(assets):
                    currentPointerAssets = len(assets)-1
                pointer.setImage(assets[currentPointerAssets])
            if event.key == pygame.K_v:
                if currentPointerAssets != 0:
                    currentPointerAssets =currentPointerAssets -1
                pointer.setImage(assets[currentPointerAssets])
          
            if event.key == pygame.K_e:
                layer_0._export()
            if event.key == pygame.K_k:
                if sentToBack:
                    sentToBack = False
                else:
                    sentToBack = True
            
    if mouse_key[0] :
        # getting the current position of the mouse 
        p = pygame.mouse.get_pos()
        # convert the screen coordinates to world co-ordinates
        x,y,z = screenToWorld([pointer.x,pointer.y])
        t = Tile(x,y,pointer.width,pointer.height)
        t.setImage(pointer.image)
        if sentToBack:
            layer_0.addTileAtStart(t)
        else:
            layer_0.addTile(t)
    if mouse_key[2]:
        # converting the pointer position to world cordinates
        x,y,z = screenToWorld([pointer.x,pointer.y])
        # checking if the pointer is inside the tile
        flag = layer_0.checkCollision(x,y)
def pointerUpdate():
    global pointer

    p = pygame.mouse.get_pos()
    # convert the screen coordinates to world co-ordinates
    pointer.x = p[0]
    pointer.y = p[1]






# initilize the pygame
pygame.init()
# screen height and width
width ,height = 800,600
# center of the screen | environment cooords
cx,cy,cz = width/2,height/2, -5
# loading the icon  
#pygame.display.set_icon(pygame.image.load('Icon.png'))
# init the name of the window
pygame.display.set_caption("Game engin -2018")
# initilise the clock
clock = pygame.time.Clock()
# initilize the screen
screen = pygame.display.set_mode((width,height))
screen.fill(pygame.Color(255,255,255))
pygame.display.init()
pygame.display.update()
# graphics mode
color = colors()

# initilise the main camera
cam = camera((-0,0,30))
# world screen scales
pixelFactor = 200/cam.pos[2]
scalex,scaley = -width/pixelFactor,-height/pixelFactor

pos = pygame.mouse.get_pos()
pointer = Pointer(pos[0],pos[1],70,70)
# initlizing the camera 
cam = camera()
# initilizing the layers 
Layers = []
# starting the 
layer_0 = Level()

sprit = Image.open("assets/sprites/tileset.png")
assets = list()

assetsLoader(sprit)
currentPointerAssets = 0
pointer.setImage(assets[currentPointerAssets])
sentToBack = False

print len(assets)
def main():
    while True:
    
        screen.fill(color.BLACK)
        # setting the smallest time variation
        dt = float(clock.tick(60))/100
        clock.tick(60)


        pointerUpdate()
        
        display()

        
        mouse_rel = pygame.mouse.get_rel()
        mouse_buttons = pygame.mouse.get_pressed()
        _input(dt,mouse_rel,mouse_buttons)
        
        
        pygame.display.update()
        
    

if __name__ == "__main__":
    main()

    

    








