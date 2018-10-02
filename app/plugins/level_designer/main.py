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

    pygame.draw.rect(screen,(119, 121, 119),(int(0-cam.pos[0]),int(0-cam.pos[1]),int(12000-cam.pos[0]),int(550-cam.pos[1])))

    
    for i in range(0,800,50):
        pygame.draw.line(screen,(100,100,100),(0-cam.pos[0],i-cam.pos[1]),(12000-cam.pos[0],i-cam.pos[1]),1)
       
    for i in range(0,12000,50):
        pygame.draw.line(screen,(100,100,100),(i-cam.pos[0],0-cam.pos[1]),(i-cam.pos[0],800-cam.pos[1]),1)
        
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
        
def part(str):
    name,ext = str.split('.')
    return name
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
    r15 = Rect(300,190,40,30)
    r16 = Rect(350,190,20,30)
    r17 = Rect(380,190,40,30)
    r18 = Rect(420,160,40,50)
    r19 = Rect(480,190,20,30)
    r20 = Rect(320,230,30,40)
    r21 = Rect(370,230,30,40)
    r22 = Rect(410,230,40,40)
    r23 = Rect(460,240,40,50)
    r24 = Rect(510,180,50,90)
    r25 = Rect(510,50,45,40)
    r26 = Rect(560,50,50,40)
    r27 = Rect(620,50,40,20)
    r28 = Rect(620,73,50,25)
    r29 = Rect(510,95,40,40)
    r30 = Rect(550,95,55,40)
    r31 = Rect(510,130,70,50)
    r32 = Rect(585,120,50,50)
    r33 = Rect(610,110,15,20)
    r34 = Rect(640,110,35,35)
    r35 = Rect(680,35,240,105)
    r36 = Rect(675,140,50,40)
    r37 = Rect(730,140,35,40)
    r38 = Rect(780,140,50,40)
    r39 = Rect(840,140,30,40)
    r40 = Rect(725,190,95,115)
    r41 = Rect(840,190,40,35)
    r42 = Rect(890,190,35,35)
    r43 = Rect(580,185,45,40)
    r44 = Rect(640,185,30,40)
    r45 = Rect(685,185,50,40)
    r46 = Rect(570,240,70,50)
    r47 = Rect(650,240,60,50)

    rs0 = Rect(0,0,112,304)
    rc0 = Rect(0,0,544,236)
    rw0 = Rect(0,0,112,96)
    rg0 = Rect(0,0,616,110)

    for sprite in spritesList:
        if sprite[2] == "clouds.png":
            assets.append([sprite[1].crop(rc0.get()),rc0,part(sprite[2])])
        if sprite[2] == "sky.png":
            assets.append([sprite[1].crop(rs0.get()),rs0,part(sprite[2])])
        if sprite[2] == "sea.png":
            assets.append([sprite[1].crop(rw0.get()),rw0,part(sprite[2])])
        if sprite[2] == "far_grounds.png":
            assets.append([sprite[1].crop(rg0.get()),rg0,part(sprite[2])])
        if sprite[2] == "tileset.png":
            assets.append([sprite[1].crop(r1.get()),r1,part(sprite[2])])
            assets.append([sprite[1].crop(r2.get()),r2,part(sprite[2])])
            assets.append([sprite[1].crop(r3.get()),r3,part(sprite[2])])
            assets.append([sprite[1].crop(r4.get()),r4,part(sprite[2])])
            assets.append([sprite[1].crop(r5.get()),r5,part(sprite[2])])
            assets.append([sprite[1].crop(r6.get()),r6,part(sprite[2])])
            assets.append([sprite[1].crop(r7.get()),r7,part(sprite[2])])
            assets.append([sprite[1].crop(r8.get()),r8,part(sprite[2])])
            assets.append([sprite[1].crop(r9.get()),r9,part(sprite[2])])
            assets.append([sprite[1].crop(r10.get()),r10,part(sprite[2])])
            assets.append([sprite[1].crop(r11.get()),r11,part(sprite[2])])
            assets.append([sprite[1].crop(r12.get()),r12,part(sprite[2])])
            assets.append([sprite[1].crop(r13.get()),r13,part(sprite[2])])
            assets.append([sprite[1].crop(r14.get()),r14,part(sprite[2])])
            assets.append([sprite[1].crop(r15.get()),r15,part(sprite[2])])
            assets.append([sprite[1].crop(r16.get()),r16,part(sprite[2])])
            assets.append([sprite[1].crop(r17.get()),r17,part(sprite[2])])
            assets.append([sprite[1].crop(r18.get()),r18,part(sprite[2])])
            assets.append([sprite[1].crop(r19.get()),r19,part(sprite[2])])
            assets.append([sprite[1].crop(r20.get()),r20,part(sprite[2])])
            assets.append([sprite[1].crop(r21.get()),r21,part(sprite[2])])
            assets.append([sprite[1].crop(r22.get()),r22,part(sprite[2])])
            assets.append([sprite[1].crop(r23.get()),r23,part(sprite[2])])
            assets.append([sprite[1].crop(r24.get()),r24,part(sprite[2])])
            assets.append([sprite[1].crop(r25.get()),r25,part(sprite[2])])
            assets.append([sprite[1].crop(r26.get()),r26,part(sprite[2])])
            assets.append([sprite[1].crop(r27.get()),r27,part(sprite[2])])
            assets.append([sprite[1].crop(r28.get()),r28,part(sprite[2])])
            assets.append([sprite[1].crop(r29.get()),r29,part(sprite[2])])
            assets.append([sprite[1].crop(r30.get()),r30,part(sprite[2])])
            assets.append([sprite[1].crop(r31.get()),r31,part(sprite[2])])
            assets.append([sprite[1].crop(r32.get()),r32,part(sprite[2])])
            assets.append([sprite[1].crop(r33.get()),r33,part(sprite[2])])
            assets.append([sprite[1].crop(r34.get()),r34,part(sprite[2])])
            assets.append([sprite[1].crop(r35.get()),r35,part(sprite[2])])
            assets.append([sprite[1].crop(r36.get()),r36,part(sprite[2])])
            assets.append([sprite[1].crop(r37.get()),r37,part(sprite[2])])
            assets.append([sprite[1].crop(r38.get()),r38,part(sprite[2])])
            assets.append([sprite[1].crop(r39.get()),r39,part(sprite[2])])
            assets.append([sprite[1].crop(r40.get()),r40,part(sprite[2])])
            assets.append([sprite[1].crop(r41.get()),r41,part(sprite[2])])
            assets.append([sprite[1].crop(r42.get()),r42,part(sprite[2])])
            assets.append([sprite[1].crop(r43.get()),r43,part(sprite[2])])
            assets.append([sprite[1].crop(r44.get()),r44,part(sprite[2])])
            assets.append([sprite[1].crop(r45.get()),r45,part(sprite[2])])
            assets.append([sprite[1].crop(r46.get()),r46,part(sprite[2])])
            assets.append([sprite[1].crop(r47.get()),r47,part(sprite[2])])
            
            
def ImageSet(t):
    global assets
    for asset in assets:
        if asset[1].x == t.fx:
           if asset[1].y == t.fy:
               if asset[1].w == t.fWidth:
                   if asset[1].h == t.fHeight:
                      return asset[0]
    #print(asset[1].x,"|",t.x)
 
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
                Layers[currentSelectedLayer][1].transform(0,10)
            if event.key == pygame.K_j:
                # increase the pointer width
                pointer.width += 10
                Layers[currentSelectedLayer][1].transform(10,0)
            if event.key == pygame.K_y:
                # decrease pointer height
                pointer.height -= 10
                Layers[currentSelectedLayer][1].transform(0,-10)
            if event.key == pygame.K_u:
                # decrease the pointer width
                pointer.width -= 10
                Layers[currentSelectedLayer][1].transform(-10,0)
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
                id = len(Layers)
                l = Layer(id)
                Layers.append([id,l,True])
                currentSelectedLayer = id
                print ("Layer Selected : ", currentSelectedLayer)
            if event.key == pygame.K_l:
                if Layers[currentSelectedLayer][2]:
                    Layers[currentSelectedLayer][2] = False
                else:
                    Layers[currentSelectedLayer][2] = True
            if event.key == pygame.K_b:
                t = input("Enter the Text")
                Layers[currentSelectedLayer][1].editText(t)
            if event.key == pygame.K_KP_PLUS:
                # increse the current layer number
                if currentSelectedLayer < len(Layers)-1:
                    currentSelectedLayer = currentSelectedLayer+1
                if currentSelectedLayer >= len(Layers)-1:
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
            if event.key == pygame.K_z:
                # optimise the number redandend tiles
                Layers[currentSelectedLayer][1].optimise()

            if event.key == pygame.K_a:
                Layers[currentSelectedLayer][1].translate(-1,0)
            if event.key == pygame.K_d:
                Layers[currentSelectedLayer][1].translate(1,0)
            if event.key == pygame.K_w:
                Layers[currentSelectedLayer][1].translate(0,-1)
            if event.key == pygame.K_s:
                Layers[currentSelectedLayer][1].translate(0,1)

            if event.key == pygame.K_r:
                Layers[currentSelectedLayer][1].deSelectAll()
            if event.key == pygame.K_x:
                Layers[currentSelectedLayer][1].deleteSelected()
            if event.key == pygame.K_m:
                Layers[currentSelectedLayer][1]._import()
                
                for t in Layers[currentSelectedLayer][1].tiles:
                    t.setImage(ImageSet(t))

    if mouse_key[0] :
    
        # getting the current position of the mouse 
        p = pygame.mouse.get_pos()
        # convert the screen coordinates to world co-ordinates
        x,y,z = screenToWorld([pointer.x,pointer.y])
        t = Tile(x,y,pointer.width,pointer.height)
        t.setImage(pointer.image)
        t.setFrame(pointer.fx,pointer.fy,pointer.fWidth,pointer.fHeight)
        t.textureName = pointer.textureName
        t.textureEnabled = pointer.textureEnabled
        t.color = pointer.color
        if sentToBack:
            Layers[currentSelectedLayer][1].addTileAtStart(t)
            time.sleep(0.1)
        else:
            Layers[currentSelectedLayer][1].addTile(t)
            time.sleep(0.1)
    if mouse_key[2]:
        # converting the pointer position to world cordinates
        x,y,z = screenToWorld([pointer.x,pointer.y])
        # checking if the pointer is inside the tile
        flag = Layers[currentSelectedLayer][1].checkCollision(x,y)
def pointerUpdate():
    global pointer

    p = pygame.mouse.get_pos()
    # convert the screen coordinates to world co-ordinates
    pointer.x = p[0]
    pointer.y = p[1]

    if pointer.textureEnabled:
        pointer.width = pointer.fWidth
        pointer.height = pointer.fHeight



def readSprites():
    import paths.py
    # get the cuurent directory
    path = os.getcwd()
    
    assetsDir = "\\resourses"
    spritesDir = "\\sprites"

    sprites = os.listdir(path+assetsDir+spritesDir) 
    #print path+assetsDir+spritesDir

    print (sprites)
    s0 = Image.open("resourses/sprites/tileset.png")
    id = 0
    for name in sprites:
        s0 = Image.open("resourses/sprites/"+name)
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
layer_0 = Layer(0)
# added the default layer object to layers [id,layer,display]
Layers.append([0,layer_0,True])
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

def help():
    print ('''Key Map
    use Arrow Key to move the camera 
    - : layer selection 
    + : layer selection 
    l : hide layer 
    n : create new layer 
    k : send to back
    c : change selected asset 
    v : change selected asset 
    i : toggle the pointer texture 
    h : increase pointer height 
    j : increase pointer width 
    y : decrease poiter height 
    u : decrease pointer width 
    z : optimise the draw
    e : export layer 
    p : help
    ''')
help()

def main():
    while True:
    
        screen.fill(color.BLACK)
        # setting the smallest time variation
        dt = float(clock.tick(60))/10
        clock.tick(60)


        pointerUpdate()
        
        display()

        
        mouse_rel = pygame.mouse.get_rel()
        mouse_buttons = pygame.mouse.get_pressed()
        _input(dt,mouse_rel,mouse_buttons)
        
        
        pygame.display.update()
        
    

if __name__ == "__main__":
    main()

    

    








