'''
Copyright {2017} {siddhartha singh | sidd5sci@gmail.com}

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''


import wx
import wx.aui
import os
import threading
global pygame # when we import it, let's keep its proper name!
global pygame_init_flag
pygame_init_flag = False
from pygame.locals import *

import sys; sys.path.insert(0, "..")



class MainWindow(wx.aui.AuiMDIParentFrame):
    def __init__(self, parent, title,*args):
        # super(NodeEditor, self).__init__(parent, title=title,size=(550, 550))

        wx.aui.AuiMDIParentFrame.__init__(self, parent, -1,
                                          title=" PyTrack v 1.0 ",
                                          size=(640,480),
                                          style=wx.DEFAULT_FRAME_STYLE)
        self.node_module = args[0]
        self.designer = args[1]
        self.count = 0
        
        self.initEditor()
    
    def initEditor(self):
                
        #draw_button = wx.Button(self, label="Press Me")
        #self.Bind(wx.EVT_BUTTON, self.OnButtonPressed, draw_button)
        mb = self.MakeMenuBar()
        self.SetMenuBar(mb)
        self.CreateStatusBar()
        self.Maximize(True)
        self.Centre()
        self.Show()
        s =sizerMain()

    def sizerMain(self):
        return  wx.sizer(wx.HORIZONTAL)
    
    def onNewChild(self, evt):
        self.count += 1
        child = ChildFrameSDL(self, self.count,"sdl",self.designer)
        child.Show()

    def onDoClose(self, evt):
        self.Close()
    
    def onNewNode(self,evt):
        self.count += 1
        child = ChildFrameSDL(self, self.count,"node",self.node_module)
        child.Show()

    def MakeMenuBar(self):
        mb = wx.MenuBar()
        menu = wx.Menu()
        item = menu.Append(-1, "New SDL child window\tCtrl-N")
        self.Bind(wx.EVT_MENU, self.onNewChild, item)
        item = menu.Append(-1, "New node window\tCtrl-N")
        self.Bind(wx.EVT_MENU, self.onNewNode, item)
        item = menu.Append(-1, "Close parent")
        self.Bind(wx.EVT_MENU, self.onDoClose, item)
        mb.Append(menu, "&File")
        return mb
    
    

class NodeEditor(wx.Panel):
    def __init__(self,parent,ID,tplSize,*args):
        wx.Panel.__init__(self, parent, ID, size=tplSize)
        
        self.node_module = args[0]
        self.Nodes = []

        self.count = 0
        # mouse pos controls
        self.start = []
        self.current = []
        self.lastCurrent = []
        self.end = []
        self.radius = 7
        self.initEditor()

    def initEditor(self):
        # bind mouse ,key
        self.SetBackgroundColour("#0C1821")
        self.Bind(wx.EVT_PAINT, self.onPaint)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
        self.Bind(wx.EVT_LEFT_DOWN, self.onLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.onLeftUp)
        self.Bind(wx.EVT_RIGHT_DOWN, self.onRightDown)
        self.Bind(wx.EVT_RIGHT_UP, self.onRightUp)
    
    def drawTestRects(self,dc):
        dc.SetBrush(wx.Brush("#000000",style=wx.SOLID))
        dc.DrawRectangle(50,50,50,50)
        dc.DrawRectangle(100,100,100,100)
    
    def onPaint(self, event):
        event.Skip()

        dc=wx.PaintDC(self)
        dc.BeginDrawing()
        dc.EndDrawing()
    
    def onPaint(self, e):
        self.dc = wx.PaintDC(self)
        
        #dc.Clear() 
        #dc.DrawBitmap(wx.Bitmap("python.jpg"),10,10,True) 
        self.createNode("Palyer",200,200,100,100)
        self.createNode("Key Down",400,300,100,100)
        self.displayNodes()
        self.gc = wx.GraphicsContext.Create(self.dc)
        self.gc.PushState()
        self.drawBezier(300,200,400,300)
        self.gc.PopState()
        #self.dc.EndDrawing()
    
    def drawBezier(self,toX,toY,fromX,fromY):
        self.gc.SetPen(wx.Pen("#0E7C7B",2))
        path = self.gc.CreatePath()
        path.MoveToPoint(wx.Point2D(toX,toY)) # where to move
        # Adds a cubic Bezier curve from the current point, using two control points and an end point.
        path.AddCurveToPoint(wx.Point2D(toX+50,toY+10),
                             wx.Point2D(fromX-70,fromY-10),
                             wx.Point2D(fromX,fromY))
        self.gc.DrawPath(path)
    
    def OnMouseMove(self, event):
        if event.Dragging() and event.LeftIsDown():
            evtPos = event.GetPosition()
            #print("Drag",self.start)
            
            self.dc.Clear()
            dx = evtPos[0] - self.current[0]
            dy = evtPos[1] - self.current[1]
            self.current = evtPos
            for n in self.Nodes:
                if n.selected == True:
                    # send the delta x,y to nodes
                    n.translate(dx,dy)
            for n in self.Nodes:
                for p in n.pins:
                    if p.selected == True:
                        self.drawBezier(p.x+n.x,p.y+n.y,evtPos[0],evtPos[1])
                        
            
            
            self.displayNodes()
            
            try:
                rect = wx.Rect(topLeft=(0,0), bottomRight=evtPos)
            except TypeError as exc:  # topLeft = NoneType. Attempting to double click image or something
                return
            except Exception as exc:
                raise exc
    
    def onLeftDown(self,event):
        x = event.GetX()
        y = event.GetY()
        self.start = [x,y]
        self.current = self.start
        print("left down",self.start)
        noneSelected = 1
        for n in self.Nodes:
                if n.isInside(self.start[0],self.start[1]):
                    n.setSelectedTrue()
                    noneSelected = 0
                    wx.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
                
                
        if noneSelected == 1:
            for n in self.Nodes:
                    n.setSelectedFalse()
                    wx.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        
        
        self.displayNodes()
        
    def onLeftUp(self,event):
        x = event.GetX()
        y = event.GetY()
        self.end = [x,y]
        self.start = None
        print("left Up",self.start)
        
        flag,spid,sptp = 0,-1,''
        for n in self.Nodes:
            for p in n.pins:
                    if p.selected == True:
                        flag = 1
                        spid = p.id
                        sptp = p._type_
                        break
            if flag == 1:
                # search where the (x,y) lies
                for node in self.Nodes:
                    if node.isInsideOnly(x,y):
                        p = node.isInsidePinOnly(x,y)
                        if p:
                            n.createConnection(x,y,node.id,p.id,spid,sptp)


        for n in self.Nodes:
                for p in n.pins:
                    p.selected = False
    
    def onRightDown(self,event):
        x = event.GetX()
        y = event.GetY()
        print("Right down",x,y)
        self.createNode("New Node",x,y,100,100)
        #brush = wx.Brush(wx.Colour(192,192,192,0x80))
        self.displayNodes()
    
    def createMenu(self):
        self.dc.DrawRectangleList()
    
    def onRightUp(self,event):
        print("Right up")

    def createNode(self,title,x,y,width,height):
        n = self.node_module.Node(title,x,y,width,height)
        self.Nodes.append(n)
    
    def addPin(self,_type_):
        pass
    
    def createNodeConnector(self):
        pass
    
    def displayConnector(self):
        pass
    
    def displayNodes(self):
        self.dc = wx.ClientDC(self)
        for n in self.Nodes:
            if n.selected :
                #brush = wx.Brush(wx.Colour(192,192,192,0x80))
                self.dc.SetBrush(wx.Brush('#324A5F'))
                self.dc.DrawRectangle(n.x,n.y,n.width,n.height)
                self.dc.DrawRectangle(n.x,n.y-25,n.width,25)
                for p in n.pins:
                    if p._type_ == 'input':
                        # input pins
                        self.dc.SetBrush(wx.Brush('#324A5F'))
                        self.dc.DrawCircle(n.x,n.y+p.y,n.radius)
                        self.dc.SetBrush(wx.Brush('#CCC9DC'))
                        self.dc.DrawCircle(n.x,n.y+p.y,n.radius-2)
                    else:
                        # output pins
                        self.dc.SetBrush(wx.Brush('#324A5F'))
                        self.dc.DrawCircle(n.x+n.width,n.y+p.y,n.radius)
                        self.dc.SetBrush(wx.Brush('#CCC9DC'))
                        self.dc.DrawCircle(n.x+n.width,n.y+p.y,n.radius-2)
                

                font = wx.Font(14, wx.ROMAN, wx.ITALIC, wx.NORMAL) 
                self.dc.SetFont(font) 
                self.dc.DrawText(n.title,n.x+10,n.y-20) 
            else:
                self.dc.SetBrush(wx.Brush(n.COLOR))
                self.dc.DrawRectangle(n.x,n.y,n.width,n.height)
                self.dc.DrawRectangle(n.x,n.y-25,n.width,25)
                
                for p in n.pins:
                    if p._type_ == 'input':
                        # input pins
                        self.dc.SetBrush(wx.Brush('#324A5F'))
                        self.dc.DrawCircle(n.x,n.y+p.y,n.radius)
                        self.dc.SetBrush(wx.Brush('#CCC9DC'))
                        self.dc.DrawCircle(n.x,n.y+p.y,n.radius-2)
                    else:
                        # output pins
                        self.dc.SetBrush(wx.Brush('#324A5F'))
                        self.dc.DrawCircle(n.x+n.width,n.y+p.y,n.radius)
                        self.dc.SetBrush(wx.Brush('#CCC9DC'))
                        self.dc.DrawCircle(n.x+n.width,n.y+p.y,n.radius-2)
                

                font = wx.Font(14, wx.ROMAN, wx.ITALIC, wx.NORMAL) 
                self.dc.SetFont(font) 
                self.dc.DrawText(n.title,n.x+10,n.y-20) 
                #n.conection()

class ChildFrameSDL(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent, count,_type,*args):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1,
                                         title="Child: %d" % count)
        mb = parent.MakeMenuBar()
        menu = wx.Menu()
        item = menu.Append(-1, "This is child %d's menu" % count)
        mb.Append(menu, "&Child")
        self.SetMenuBar(mb)
        if _type == "sdl":
            p = SDLPanel(self, -1, (640,480),args[0])
        else:
            p = NodeEditor(self, -1, (640,480),args[0])
        # bSizer1 = wx.BoxSizer( wx.HORIZONTAL  )

        #sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 10,-1 ), wx.HSCROLL|wx.VSCROLL )
		
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		
        self.m_scrolledWindow1.SetMaxSize( wx.Size( 100,-1 ) )

		
        s = parent.sizerMain()
        
        s.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL,5 )
        
        s.Add(p, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
        wx.CallAfter(self.Layout)

class SDLThread:
    def __init__(self,designer):
        self.m_bKeepGoing = self.m_bRunning = False
        self.designer = designer
        self.color = (255,0,0)
        self.rect = (10,10,100,100)
        self.thread = None
        self.init = True

    def Start(self):
        #I rewrote this to use the higherlevel threading module
        self.m_bKeepGoing = self.m_bRunning = True
        self.thread = threading.Thread(group=None, target=self.Run, name=None, 
                                       args=(), kwargs={})
        self.thread.start()

    def Stop(self):
        self.m_bKeepGoing = False
        #this important line make sure that the draw thread exits before
        #pygame.quit() is called so there is no errors
        self.thread.join()

    def IsRunning(self):
        return self.m_bRunning

    def Run(self):
        while self.m_bKeepGoing:
            #I rewrote this to only draw when the position changes
            # e = pygame.event.poll()
            # if e.type == pygame.MOUSEBUTTONDOWN:
            #     self.color = (255,0,128)
            #     self.rect = (e.pos[0], e.pos[1], 100, 100)
            #     print (e.pos)
            #     self.screen.fill((0,0,0))
            #     self.screen.fill(self.color,self.rect)
            # if self.init:
            #     self.screen.fill((0,0,0))
            #     self.screen.fill(self.color,self.rect)
            # pygame.display.flip()
            self.designer.main()
        self.m_bRunning = False
        print ("pygame draw loop exited")
 
class SDLPanel(wx.Panel):
    def __init__(self,parent,ID,tplSize,*args):
        global pygame
        global pygame_init_flag
        wx.Panel.__init__(self, parent, ID, size=tplSize)
        self.Fit()
        os.environ['SDL_WINDOWID'] = str(self.GetHandle())
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        #here is where things change if pygame has already been initialized 
        #we need to do so again
        n = args[0]
        if pygame_init_flag:
            #call pygame.init() on subsaquent windows
            #pygame.init()
            n.initPygame()
        else:
            #import if this is the first time
            import pygame
        
        n.initPygame()
        pygame_init_flag = True #make sure we know that pygame has been imported
        #pygame.display.init()
        #window = pygame.display.set_mode(tplSize)
        self.thread = SDLThread(n)
        self.thread.Start()

    def __del__(self):
        self.thread.Stop()
        print( "thread stoped")
        #very important line, this makes sure that pygame exits before we 
        #reinitialize it other wise we get errors
        pygame.quit()

    

if __name__ == '__main__':
    app = wx.App()
    NodeEditor(None, 'Node Editor')
    app.MainLoop()
