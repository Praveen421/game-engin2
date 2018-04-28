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
import pygame,math,time,os
from layer import *
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
    global pointer, Layers,currentSelectedLayer,Layer,cam
    
    if sentToBack:
        if pointer.textureEnabled:
            screen.blit(convertPILtoPygame(pointer.image),(int(pointer.x),int(pointer.y)))
        else:
            pygame.draw.rect(screen,pointer.color,(int(pointer.x),int(pointer.y),int(pointer.width),int(pointer.height)))
    
        for layer in Layers:
            if layer[2]:
                for t in layer[1].tiles:        
                    x,y = worldToScreen([t.x,t.y,50])
                    if t.textureEnabled:
                        screen.blit(convertPILtoPygame(t.texture),(int(x),int(y)))
                    else:
                        pygame.draw.rect(screen,pointer.color,(int(x),int(y),int(t.width),int(t.height)))
            
    else:
        for layer in Layers:
            if layer[2]:
                for t in layer[1].tiles:
                    x,y = worldToScreen([t.x,t.y,50])
                    if t.textureEnabled:
                        screen.blit(convertPILtoPygame(t.texture),(int(x),int(y)))
                    else:
                        pygame.draw.rect(screen,pointer.color,(int(x),int(y),int(t.width),int(t.height)))
                
        if pointer.textureEnabled:
            screen.blit(convertPILtoPygame(pointer.image),(int(pointer.x),int(pointer.y)))
        else:
            pygame.draw.rect(screen,pointer.color,(int(pointer.x),int(pointer.y),int(pointer.width),int(pointer.height)))
        

def assetsLoader():
    global assets,spritesList

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

    rs0 = Rect(0,0,112,304)
    rc0 = Rect(0,0,544,236)
    rw0 = Rect(0,0,112,96)
    rg0 = Rect(0,0,616,110)

    for sprite in spritesList:
        if sprite[2] == "clouds.png":
            assets.append([sprite[1].crop(rc0.get()),rc0,sprite[2]])
        if sprite[2] == "sky.png":
            assets.append([sprite[1].crop(rs0.get()),rs0,sprite[2]])
        if sprite[2] == "sea.png":
            assets.append([sprite[1].crop(rw0.get()),rw0,sprite[2]])
        if sprite[2] == "far_grounds.png":
            assets.append([sprite[1].crop(rg0.get()),rg0,sprite[2]])
        if sprite[2] == "tileset.png":
            assets.append([sprite[1].crop(r1.get()),r1,sprite[2]])
            assets.append([sprite[1].crop(r2.get()),r2,sprite[2]])
            assets.append([sprite[1].crop(r3.get()),r3,sprite[2]])
            assets.append([sprite[1].crop(r4.get()),r4,sprite[2]])
            assets.append([sprite[1].crop(r5.get()),r5,sprite[2]])
            assets.append([sprite[1].crop(r6.get()),r6,sprite[2]])
            assets.append([sprite[1].crop(r7.get()),r7,sprite[2]])
            assets.append([sprite[1].crop(r8.get()),r8,sprite[2]])
            assets.append([sprite[1].crop(r9.get()),r9,sprite[2]])
            assets.append([sprite[1].crop(r10.get()),r10,sprite[2]])
            assets.append([sprite[1].crop(r11.get()),r11,sprite[2]])
            assets.append([sprite[1].crop(r12.get()),r12,sprite[2]])
            assets.append([sprite[1].crop(r13.get()),r13,sprite[2]])
            assets.append([sprite[1].crop(r14.get()),r14,sprite[2]])
 
    
    

def convertPILtoPygame(image):
    mode = image.mode
    size = image.size
    data = image.tobytes()
    return pygame.image.fromstring(data, size, mode)

def _input(dt,mouse_rel,mouse_key):
    global currentSelectedLayer,Layers,cam,sentToBack,currentPointerAssets,assets
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
                pointer.setImage(assets[currentPointerAssets][0])
                pointer.setFrame(assets[currentPointerAssets][1])
                pointer.textureName = assets[currentPointerAssets][2]
            if event.key == pygame.K_v:
                if currentPointerAssets != 0:
                    currentPointerAssets =currentPointerAssets -1
                pointer.setImage(assets[currentPointerAssets][0])
                pointer.setFrame(assets[currentPointerAssets][1])
                pointer.textureName = assets[currentPointerAssets][2]
            if event.key == pygame.K_h:
                # increase pointer height
                pointer.height += 10
            if event.key == pygame.K_j:
                # increase the pointer width
                pointer.width += 10
            if event.key == pygame.K_i:
                # toggle the pointer texture
                if pointer.textureEnabled:
                    pointer.textureEnabled = False
                else:
                    pointer.textureEnabled = True
            if event.key == pygame.K_e:
                Layers[currentSelectedLayer][1]._export()
            if event.key == pygame.K_k:
                if sentToBack:
                    sentToBack = False
                else:
                    sentToBack = True
            if event.key == pygame.K_n:
                l = Layer()
                id = len(Layers)
                Layers.append([id,l,True])
                currentSelectedLayer = id
                print ("Layer Selected : ", currentSelectedLayer)
            if event.key == pygame.K_l:
                if Layers[currentSelectedLayer][2]:
                    Layers[currentSelectedLayer][2] = False
                else:
                    Layers[currentSelectedLayer][2] = True
            if event.key == pygame.K_KP_PLUS:
                # increse the current layer number
                if currentSelectedLayer < len(Layers):
                    currentSelectedLayer = currentSelectedLayer+1
                if currentSelectedLayer >= len(Layers):
                    currentSelectedLayer = len(Layers)-1
                print ("Layer Selected : ", currentSelectedLayer)
            if event.key == pygame.K_KP_MINUS:
                # decrese the current layer number
                if currentSelectedLayer !=0:
                    currentSelectedLayer = currentSelectedLayer-1
                print ("Layer Selected : ", currentSelectedLayer)
            if event.key == pygame.K_LCTRL:
                if event.key == pygame.K_z:
                    Layers[currentSelectedLayer][1].removeRecentTile()
    if mouse_key[0] :
        # getting the current position of the mouse 
        p = pygame.mouse.get_pos()
        # convert the screen coordinates to world co-ordinates
        x,y,z = screenToWorld([pointer.x,pointer.y])
        t = Tile(x,y,pointer.width,pointer.height)
        t.setImage(pointer.image)
        t.setFrame(pointer.fx,pointer.fy,pointer.fWidth,pointer.fHeight)
        t.textureName = pointer.textureName
        t.color = pointer.color
        if sentToBack:
            Layers[currentSelectedLayer][1].addTileAtStart(t)
        else:
            Layers[currentSelectedLayer][1].addTile(t)
    if mouse_key[2]:
        # converting the pointer position to world cordinates
        x,y,z = screenToWorld([pointer.x,pointer.y])
        # checking if the pointer is inside the tile
        flag = Layers[currentSelectedLayer].checkCollision(x,y)
def pointerUpdate():
    global pointer

    p = pygame.mouse.get_pos()
    # convert the screen coordinates to world co-ordinates
    pointer.x = p[0]
    pointer.y = p[1]



def readSprites():
    # get the cuurent directory
    path = os.getcwd()
    
    assetsDir = "\\assets"
    spritesDir = "\\sprites"

    sprites = os.listdir(path+assetsDir+spritesDir) 
    #print path+assetsDir+spritesDir

    print (sprites)
    s0 = Image.open("assets/sprites/tileset.png")
    id = 0
    for name in sprites:
        s0 = Image.open("assets/sprites/"+name)
        spritesList.append([id,s0,name])

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
pointer = Pointer(pos[0],pos[1],100,100)
#pointer.textureEnabled = False
# initlizing the camera 
cam = camera()
# initilizing the layers 
Layers = []
# starting the first layer 
layer_0 = Layer()
# added the default layer object to layers
Layers.append([1,layer_0,True])
currentSelectedLayer = 0

spritesList = list()
# read all the sprites
readSprites()
assets = list()

assetsLoader()
currentPointerAssets = 4
pointer.setImage(assets[currentPointerAssets][0])
pointer.setFrame(assets[currentPointerAssets][1])
pointer.textureName = assets[currentPointerAssets][2]
sentToBack = False

print (len(assets))
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

    

    








