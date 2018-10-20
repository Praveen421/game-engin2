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

class Designer():
    def __init__(self,*args,**kwargs):
        print("Designer work")

        ###############################################################
        ###     importing modules
        ###############################################################
        print('Game Tester :',args,kwargs)
        # importing the Layer module
        self.Layer_module = args[0]
        # importing the Camera module
        self.Camera_module = args[1]
        # importing the Pointer module
        self.Pointer_module = args[2]
        # importing the Rect module
        self.Rect_module = args[3]
        # importing the Tile module
        self.Tile_module = args[4]

        # import the paths
        self.ABSPATH = kwargs['path']

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

        # initilise the main camera
        self.cam = self.Camera_module.camera((-0,0,30))
        # world screen scales
        self.pixelFactor = 200/self.cam.pos[2]
        self.scalex,self.scaley = -self.width/self.pixelFactor,-self.height/self.pixelFactor

        self.pos = pygame.mouse.get_pos()
        self.pointer = self.Pointer_module.Pointer(self.pos[0],self.pos[1],100,100)
        #pointer.textureEnabled = False
        
        # initilizing the layers 
        self.Layers = []
        # starting the first layer 
        self.layer_0 = self.Layer_module.Layer(0,self.Tile_module,self.ABSPATH)
        # added the default layer object to layers [id,layer,display]
        self.Layers.append([0,self.layer_0,True])
        self.currentSelectedLayer = 0

        self.spritesList = list()
        # read all the sprites
        self.readSprites()
        self.assets = list()

        self.assetsLoader()
        self.currentPointerAssets = 4
        self.pointer.setImage(self.assets[self.currentPointerAssets][0])
        self.pointer.setFrame(self.assets[self.currentPointerAssets][1])
        self.pointer.textureName = self.assets[self.currentPointerAssets][2]
        self.sentToBack = False

        print (len(self.assets))

    def screenToWorld(self,cords):
        x,y,z = cords[0],cords[1],0
        
        #x,y = x/pixelFactor,y/pixelFactor
        #x,y = scalex/2+x,scaley/2+y
        x,y = x+self.cam.pos[0],y+self.cam.pos[1]
        return [x,y,z]

    def worldToScreen(self,cords):
        x,y,z = cords[0],cords[1],cords[2]
        
        x,y,z = x-self.cam.pos[0],y-self.cam.pos[1],z+self.cam.pos[2]
        #pixelFactor = (pixelFactor*cam.pos[2])/z
        #f = 200/z
        #x,y = x*pixelFactor,y*pixelFactor
        #x,y = x*f,y*f
        #x,y = cx+int(x),cy+int(y)
        #x,y = scalex/2+x,scaley/2+y
        return [int(x),int(y)]

    def display(self):

        pygame.draw.rect(self.screen,(119, 121, 119),(int(0-self.cam.pos[0]),int(0-self.cam.pos[1]),int(12000-self.cam.pos[0]),int(550-self.cam.pos[1])))
        pygame.draw.rect(self.screen, (254,0,0,12), pygame.Rect(0, 0, 100, 50))
        
        for i in range(0,800,50):
            pygame.draw.line(self.screen,(100,100,100),(0-self.cam.pos[0],i-self.cam.pos[1]),(12000-self.cam.pos[0],i-self.cam.pos[1]),1)
        
        for i in range(0,12000,50):
            pygame.draw.line(self.screen,(100,100,100),(i-self.cam.pos[0],0-self.cam.pos[1]),(i-self.cam.pos[0],800-self.cam.pos[1]),1)
            
        if self.sentToBack:
            if self.pointer.textureEnabled:
                self.screen.blit(self.convertPILtoPygame(self.pointer.image),(int(self.pointer.x),int(self.pointer.y)))
            else:
                pygame.draw.rect(self.screen,self.pointer.color,(int(self.pointer.x),int(self.pointer.y),int(self.pointer.width),int(self.pointer.height)))
        
            for layer in self.Layers:
                if layer[2]:
                    for t in layer[1].tiles:        
                        x,y = self.worldToScreen([t.x,t.y,50])
                        if t.textureEnabled:
                            self.screen.blit(self.convertPILtoPygame(t.texture),(int(x),int(y)))
                        else:
                            pygame.draw.rect(self.screen,self.pointer.color,(int(x),int(y),int(t.width),int(t.height)))
                
        else:
            for layer in self.Layers:
                if layer[2]:
                    for t in layer[1].tiles:
                        x,y = self.worldToScreen([t.x,t.y,50])
                        if t.textureEnabled:
                            self.screen.blit(self.convertPILtoPygame(t.texture),(int(x),int(y)))
                        else:
                            pygame.draw.rect(self.screen,self.pointer.color,(int(x),int(y),int(t.width),int(t.height)))
                    
            if self.pointer.textureEnabled:
                self.screen.blit(self.convertPILtoPygame(self.pointer.image),(int(self.pointer.x),int(self.pointer.y)))
            else:
                pygame.draw.rect(self.screen,self.pointer.color,(int(self.pointer.x),int(self.pointer.y),int(self.pointer.width),int(self.pointer.height)))
            
    def part(self,str):
        name,ext = str.split('.')
        return name

    def assetsLoader(self):

        r1 = self.Rect_module.Rect(30,170,100,120)
        r2 = self.Rect_module.Rect(140,180,40,50)
        r3 = self.Rect_module.Rect(40,20,100,90)
        r4 = self.Rect_module.Rect(40,120,60,40)
        r5 = self.Rect_module.Rect(140,100,40,60)
        r6 = self.Rect_module.Rect(140,240,40,30)
        r7 = self.Rect_module.Rect(190,40,125,120)#tree
        r8 = self.Rect_module.Rect(190,180,50,45)
        r9 = self.Rect_module.Rect(190,240,35,65)
        r10 = self.Rect_module.Rect(250,180,40,45)
        r11 = self.Rect_module.Rect(240,240,65,30)
        r12 = self.Rect_module.Rect(320,40,65,100)
        r13 = self.Rect_module.Rect(400,40,15,100)
        r14 = self.Rect_module.Rect(430,40,60,100)
        r15 = self.Rect_module.Rect(300,190,40,30)
        r16 = self.Rect_module.Rect(350,190,20,30)
        r17 = self.Rect_module.Rect(380,190,40,30)
        r18 = self.Rect_module.Rect(420,160,40,50)
        r19 = self.Rect_module.Rect(480,190,20,30)
        r20 = self.Rect_module.Rect(320,230,30,40)
        r21 = self.Rect_module.Rect(370,230,30,40)
        r22 = self.Rect_module.Rect(410,230,40,40)
        r23 = self.Rect_module.Rect(460,240,40,50)
        r24 = self.Rect_module.Rect(510,180,50,90)
        r25 = self.Rect_module.Rect(510,50,45,40)
        r26 = self.Rect_module.Rect(560,50,50,40)
        r27 = self.Rect_module.Rect(620,50,40,20)
        r28 = self.Rect_module.Rect(620,73,50,25)
        r29 = self.Rect_module.Rect(510,95,40,40)
        r30 = self.Rect_module.Rect(550,95,55,40)
        r31 = self.Rect_module.Rect(510,130,70,50)
        r32 = self.Rect_module.Rect(585,120,50,50)
        r33 = self.Rect_module.Rect(610,110,15,20)
        r34 = self.Rect_module.Rect(640,110,35,35)
        r35 = self.Rect_module.Rect(680,35,240,105)
        r36 = self.Rect_module.Rect(675,140,50,40)
        r37 = self.Rect_module.Rect(730,140,35,40)
        r38 = self.Rect_module.Rect(780,140,50,40)
        r39 = self.Rect_module.Rect(840,140,30,40)
        r40 = self.Rect_module.Rect(725,190,95,115)
        r41 = self.Rect_module.Rect(840,190,40,35)
        r42 = self.Rect_module.Rect(890,190,35,35)
        r43 = self.Rect_module.Rect(580,185,45,40)
        r44 = self.Rect_module.Rect(640,185,30,40)
        r45 = self.Rect_module.Rect(685,185,50,40)
        r46 = self.Rect_module.Rect(570,240,70,50)
        r47 = self.Rect_module.Rect(650,240,60,50)

        rs0 = self.Rect_module.Rect(0,0,112,304)
        rc0 = self.Rect_module.Rect(0,0,544,236)
        rw0 = self.Rect_module.Rect(0,0,112,96)
        rg0 = self.Rect_module.Rect(0,0,616,110)

        for sprite in self.spritesList:
            if sprite[2] == "clouds.png":
                self.assets.append([sprite[1].crop(rc0.get()),rc0,self.part(sprite[2])])
            if sprite[2] == "sky.png":
                self.assets.append([sprite[1].crop(rs0.get()),rs0,self.part(sprite[2])])
            if sprite[2] == "sea.png":
                self.assets.append([sprite[1].crop(rw0.get()),rw0,self.part(sprite[2])])
            if sprite[2] == "far_grounds.png":
                self.assets.append([sprite[1].crop(rg0.get()),rg0,self.part(sprite[2])])
            if sprite[2] == "tileset.png":
                self.assets.append([sprite[1].crop(r1.get()),r1,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r2.get()),r2,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r3.get()),r3,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r4.get()),r4,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r5.get()),r5,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r6.get()),r6,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r7.get()),r7,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r8.get()),r8,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r9.get()),r9,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r10.get()),r10,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r11.get()),r11,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r12.get()),r12,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r13.get()),r13,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r14.get()),r14,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r15.get()),r15,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r16.get()),r16,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r17.get()),r17,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r18.get()),r18,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r19.get()),r19,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r20.get()),r20,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r21.get()),r21,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r22.get()),r22,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r23.get()),r23,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r24.get()),r24,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r25.get()),r25,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r26.get()),r26,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r27.get()),r27,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r28.get()),r28,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r29.get()),r29,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r30.get()),r30,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r31.get()),r31,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r32.get()),r32,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r33.get()),r33,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r34.get()),r34,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r35.get()),r35,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r36.get()),r36,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r37.get()),r37,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r38.get()),r38,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r39.get()),r39,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r40.get()),r40,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r41.get()),r41,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r42.get()),r42,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r43.get()),r43,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r44.get()),r44,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r45.get()),r45,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r46.get()),r46,self.part(sprite[2])])
                self.assets.append([sprite[1].crop(r47.get()),r47,self.part(sprite[2])])
                
    def ImageSet(self,t):
        for asset in self.assets:
            if asset[1].x == t.fx:
                if asset[1].y == t.fy:
                    if asset[1].w == t.fWidth:
                        if asset[1].h == t.fHeight:
                            return asset[0]
        #print(asset[1].x,"|",t.x)
    
    def convertPILtoPygame(self,image):
        mode = image.mode
        size = image.size
        data = image.tobytes()
        return pygame.image.fromstring(data, size, mode)

    def _input(self,dt,mouse_rel,mouse_key):
        # loop through the events
        for event in pygame.event.get():
            #check if the event is the x button
            if event.type == pygame.QUIT:
                #if it is quit the game
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.cam.update(dt,"back")
                if event.key == pygame.K_UP:
                    self.cam.update(dt,"front")
                if event.key == pygame.K_LEFT:
                    self.cam.update(dt,"left")
                if event.key == pygame.K_RIGHT:
                    self.cam.update(dt,"right")
                if event.key == pygame.K_RCTRL:
                    pass
                if event.key == pygame.K_c:
                    # change the asset
                    if self.currentPointerAssets < len(self.assets):
                        self.currentPointerAssets = self.currentPointerAssets+1
                    if self.currentPointerAssets >= len(self.assets):
                        self.currentPointerAssets = len(self.assets)-1
                    self.pointer.setImage(self.assets[self.currentPointerAssets][0])
                    self.pointer.setFrame(self.assets[self.currentPointerAssets][1])
                    self.pointer.textureName = self.assets[self.currentPointerAssets][2]
                if event.key == pygame.K_v:
                    # change the asset
                    if self.currentPointerAssets != 0:
                        self.currentPointerAssets =self.currentPointerAssets -1
                    self.pointer.setImage(self.assets[self.currentPointerAssets][0])
                    self.pointer.setFrame(self.assets[self.currentPointerAssets][1])
                    self.pointer.textureName = self.assets[self.currentPointerAssets][2]
                if event.key == pygame.K_h:
                    # increase pointer height
                    self.pointer.height += 10
                    self.Layers[self.currentSelectedLayer][1].transform(0,10)
                if event.key == pygame.K_j:
                    # increase the pointer width
                    self.pointer.width += 10
                    self.Layers[self.currentSelectedLayer][1].transform(10,0)
                if event.key == pygame.K_y:
                    # decrease pointer height
                    self.pointer.height -= 10
                    self.Layers[self.currentSelectedLayer][1].transform(0,-10)
                if event.key == pygame.K_u:
                    # decrease the pointer width
                    self.pointer.width -= 10
                    self.Layers[self.currentSelectedLayer][1].transform(-10,0)
                if event.key == pygame.K_i:
                    # toggle the pointer texture
                    if self.pointer.textureEnabled:
                        self.pointer.textureEnabled = False
                    else:
                        self.pointer.textureEnabled = True
                if event.key == pygame.K_e:
                    # export the layer
                    self.Layers[self.currentSelectedLayer][1]._export()
                if event.key == pygame.K_k:
                    # send to back toggle
                    if self.sentToBack:
                        self.sentToBack = False
                    else:
                        self.sentToBack = True
                if event.key == pygame.K_n:
                    # create new layer
                    id = len(self.Layers)
                    l = self.Layer_module.Layer(id,self.Tile_module,self.ABSPATH)
                    self.Layers.append([id,l,True])
                    self.currentSelectedLayer = id
                    print ("Layer Selected : ", self.currentSelectedLayer)
                if event.key == pygame.K_l:
                    # hide and un-hide the content of the layer
                    if self.Layers[self.currentSelectedLayer][2]:
                        self.Layers[self.currentSelectedLayer][2] = False
                    else:
                        self.Layers[self.currentSelectedLayer][2] = True
                if event.key == pygame.K_b:
                    # giving id to the tiles 
                    t = input("Enter the Text")
                    self.Layers[self.currentSelectedLayer][1].editText(t)
                if event.key == pygame.K_KP_PLUS:
                    # increse the current layer number
                    if self.currentSelectedLayer < len(self.Layers)-1:
                        self.currentSelectedLayer = self.currentSelectedLayer+1
                    if self.currentSelectedLayer >= len(self.Layers)-1:
                        self.currentSelectedLayer = len(self.Layers)-1
                    print ("Layer Selected : ", self.currentSelectedLayer)
                if event.key == pygame.K_KP_MINUS:
                    # decrese the current layer number
                    if self.currentSelectedLayer !=0:
                        self.currentSelectedLayer = self.currentSelectedLayer-1
                    print ("Layer Selected : ", self.currentSelectedLayer)
                if event.key == pygame.K_LCTRL:
                    if event.key == pygame.K_z:
                        self.Layers[self.currentSelectedLayer][1].removeRecentTile()
                if event.key == pygame.K_z:
                    # optimise the number redandend tiles
                    self.Layers[self.currentSelectedLayer][1].optimise()

                if event.key == pygame.K_a:
                    self.Layers[self.currentSelectedLayer][1].translate(-1,0)
                if event.key == pygame.K_d:
                    self.Layers[self.currentSelectedLayer][1].translate(1,0)
                if event.key == pygame.K_w:
                    self.Layers[self.currentSelectedLayer][1].translate(0,-1)
                if event.key == pygame.K_s:
                    self.Layers[self.currentSelectedLayer][1].translate(0,1)

                if event.key == pygame.K_r:
                    self.Layers[self.currentSelectedLayer][1].deSelectAll()
                if event.key == pygame.K_x:
                    self.Layers[self.currentSelectedLayer][1].deleteSelected()
                if event.key == pygame.K_m:
                    self.Layers[self.currentSelectedLayer][1]._import()
                    
                    for t in self.Layers[self.currentSelectedLayer][1].tiles:
                        t.setImage(self.ImageSet(t))

        if mouse_key[0] :
        
            # getting the current position of the mouse 
            p = pygame.mouse.get_pos()
            # convert the screen coordinates to world co-ordinates
            x,y,z = self.screenToWorld([self.pointer.x,self.pointer.y])
            t = self.Tile_module.Tile(x,y,self.pointer.width,self.pointer.height)
            t.setImage(self.pointer.image)
            t.setFrame(self.pointer.fx,self.pointer.fy,self.pointer.fWidth,self.pointer.fHeight)
            t.textureName = self.pointer.textureName
            t.textureEnabled = self.pointer.textureEnabled
            t.color = self.pointer.color
            if self.sentToBack:
                self.Layers[self.currentSelectedLayer][1].addTileAtStart(t)
                time.sleep(0.1)
            else:
                self.Layers[self.currentSelectedLayer][1].addTile(t)
                time.sleep(0.1)
        if mouse_key[2]:
            # converting the pointer position to world cordinates
            x,y,z = self.screenToWorld([self.pointer.x,self.pointer.y])
            # checking if the pointer is inside the tile
            flag = self.Layers[self.currentSelectedLayer][1].checkCollision(x,y)

    def pointerUpdate(self,):
        
        p = pygame.mouse.get_pos()
        # convert the screen coordinates to world co-ordinates
        self.pointer.x = p[0]
        self.pointer.y = p[1]

        if self.pointer.textureEnabled:
            self.pointer.width = self.pointer.fWidth
            self.pointer.height = self.pointer.fHeight

    def readSprites(self):
        # get the cuurent directory
        #path = os.getcwd()
        
        assetsDir = "\\resourses"
        spritesDir = "\\sprites"

        sprites = os.listdir(self.ABSPATH+assetsDir+spritesDir) 
        #print path+assetsDir+spritesDir

        print (sprites)
        s0 = Image.open("resourses/sprites/tileset.png")
        id = 0
        for name in sprites:
            s0 = Image.open("resourses/sprites/"+name)
            self.spritesList.append([id,s0,name])

    def help(self):
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

    def main(self):
        while True:
        
            self.screen.fill(self.color.BLACK)
            # setting the smallest time variation
            dt = float(self.clock.tick(60))/10
            self.clock.tick(60)
            # pointer update
            self.pointerUpdate()
            # display
            self.display()
            # mouse and keyboard event 
            mouse_rel = pygame.mouse.get_rel()
            mouse_buttons = pygame.mouse.get_pressed()
            self._input(dt,mouse_rel,mouse_buttons)
            # pygame display screen update
            pygame.display.update()
        
    

if __name__ == "__main__":
    d = Designer()
    d.help()
    d.main()

    

    








