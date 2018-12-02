
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
import sys
from pygame.locals import *
import wx
import wx.xrc
import wx.aui
import wx.dataview
import wx.propgrid as pg
import os
import threading
global pygame  # when we import it, let's keep its proper name!
global pygame_init_flag
pygame_init_flag = False

sys.path.insert(0, "..")


class MainWindow(wx.aui.AuiMDIParentFrame):
    def __init__(self, parent, title, *args):
        # super(NodeEditor, self).__init__(parent, title=title,size=(550, 550))

        wx.aui.AuiMDIParentFrame.__init__(self, parent, -1,
                                          title=" PyTrack v 1.0.1 ",
                                          size=(640, 480),
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

        self.bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_auinotebook1 = wx.aui.AuiNotebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.aui.AUI_NB_DEFAULT_STYLE)

        self.bSizer1.Add(self.m_auinotebook1, 1, wx.EXPAND | wx.ALL, 5)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_dataViewCtrl1 = wx.dataview.DataViewCtrl(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(170, 300), 0)
        bSizer2.Add(self.m_dataViewCtrl1, 0, wx.ALL, 5)

        self.m_propertyGridManager1 = pg.PropertyGridManager(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(170, 300), wx.propgrid.PGMAN_DEFAULT_STYLE)
        self.m_propertyGridManager1.SetExtraStyle(
            wx.propgrid.PG_EX_MODE_BUTTONS)

        self.m_propertyGridPage1 = self.m_propertyGridManager1.AddPage(
            u"Page", wx.NullBitmap)
        self.m_propertyGridItem1 = self.m_propertyGridPage1.Append(
            pg.StringProperty(u"Name", u"Name"))
        self.m_propertyGridItem6 = self.m_propertyGridPage1.Append(
            pg.StringProperty(u"Name1", u"Name1"))
        self.m_propertyGridItem7 = self.m_propertyGridPage1.Append(
            pg.StringProperty(u"Name2", u"Name2"))
        self.m_propertyGridItem8 = self.m_propertyGridPage1.Append(
            pg.StringProperty(u"Name3", u"Name3"))
        self.m_propertyGridItem9 = self.m_propertyGridPage1.Append(
            pg.StringProperty(u"Name4", u"Name4"))
        self.m_propertyGridItem2 = self.m_propertyGridPage1.Append(
            pg.StringProperty(u"Name5", u"Name5"))
        self.m_propertyGridItem3 = self.m_propertyGridPage1.Append(
            pg.StringProperty(u"Name6", u"Name6"))
        self.m_propertyGridItem4 = self.m_propertyGridPage1.Append(
            pg.StringProperty(u"Name7", u"Name7"))
        self.m_propertyGridItem5 = self.m_propertyGridPage1.Append(
            pg.StringProperty(u"Name8", u"Name8"))
        bSizer2.Add(self.m_propertyGridManager1, 0, wx.ALL, 5)

        self.bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        self.SetSizer(self.bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

	# def __del__( self ):
	# 	pass

    def sizerMain(self):
        return self.bSizer1

    def onNewChild(self, evt):
        self.count += 1
        try:
            child = ChildFrameSDL(self, self.count, "sdl", self.designer)
            # child = ChildFrameSDL(self.m_auinotebook1, self.count, "sdl", self.designer)
        except Exception as data:
            print (data)

        child.Show()

    def onDoClose(self, evt):
        self.Close()

    def onNewNode(self, evt):
        self.count += 1
        child = ChildFrameSDL(self, self.count, "node", self.node_module)
        child.Show()

    def onNewProject(self, evt):
        child = MyDialog(self, "New Project").ShowModal()
        # print a

    def MakeMenuBar(self):
        m_menubar1 = wx.MenuBar(0)
        m_menubar1.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        m_menubar1.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTIONTEXT))

        m_File = wx.Menu()
        item = m_File.Append(-1, u"New Project\tCtrl-N")
        self.Bind(wx.EVT_MENU, self.onNewProject, item)
        item = m_File.Append(-1, u"Open Project\tCtrl-O")
        self.Bind(wx.EVT_MENU, self.onNewProject, item)
        item = m_File.Append(-1, u"Close Project")
        item = m_File.Append(-1, u"Save ..")
        item = m_File.Append(-1, u"Save As ..")
        item = m_File.Append(-1, u"Import")
        item = m_File.Append(-1, u"Export")
        item = m_File.Append(-1, u"Close All")
        self.Bind(wx.EVT_MENU, self.onDoClose, item)
        
        
        m_menubar1.Append(m_File, u"File")

        m_Edit = wx.Menu()
        m_menubar1.Append(m_Edit, u"Edit")

        m_View = wx.Menu()
        item = m_View.Append(-1, u"Designer\tCtrl-D")
        self.Bind(wx.EVT_MENU, self.onNewChild, item)
        item = m_View.Append(-1, u"Node Editor\tCtrl-E")
        self.Bind(wx.EVT_MENU, self.onNewNode, item)

        m_menubar1.Append(m_View, u"View")

        # mb = wx.MenuBar()
        # menu = wx.Menu()
        # item = menu.Append(-1, "New SDL child window\tCtrl-N")
        # self.Bind(wx.EVT_MENU, self.onNewChild, item)
        # item = menu.Append(-1, "New node window\tCtrl-N")
        # self.Bind(wx.EVT_MENU, self.onNewNode, item)
        # item = menu.Append(-1, "Close parent")
        # self.Bind(wx.EVT_MENU, self.onDoClose, item)
        # mb.Append(menu, "&View")

        self.SetMenuBar(m_menubar1)
        # return mb

        return m_menubar1


class PageOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageOne object", (20, 20))


class PageTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageTwo object", (40, 40))


class PageThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageThree object", (60, 60))


class MyDialog(wx.Dialog):
  	 def __init__(self, parent, title):
            super(MyDialog, self).__init__(parent, title=title, size=(550, 250))
            self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
            self.SetBackgroundColour(wx.Colour(12, 24, 33))

            bSizer1 = wx.BoxSizer(wx.VERTICAL)

            self.m_panel2 = wx.Panel(
                self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
            self.m_panel2.SetBackgroundColour(wx.Colour(12, 24, 33))

            bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

            self.m_staticText1 = wx.StaticText(
                self.m_panel2, wx.ID_ANY, u"Project Name", wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText1.Wrap(-1)
            self.m_staticText1.SetForegroundColour(wx.Colour(14, 124, 123))

            bSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

            self.m_textCtrl1 = wx.TextCtrl(
                self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(340, -1), 0)
            self.m_textCtrl1.SetBackgroundColour(wx.Colour(27, 42, 65))

            bSizer2.Add(self.m_textCtrl1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

            self.m_button1 = wx.Button(self.m_panel2, wx.ID_ANY, u"Create",
                                       wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
            self.m_button1.SetForegroundColour(
                wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
            self.m_button1.SetBackgroundColour(wx.Colour(50, 74, 95))

            bSizer2.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

            bSizer6 = wx.BoxSizer(wx.VERTICAL)

            bSizer2.Add(bSizer6, 1, wx.EXPAND, 5)

            self.m_panel2.SetSizer(bSizer2)
            self.m_panel2.Layout()
            bSizer2.Fit(self.m_panel2)
            bSizer1.Add(self.m_panel2, 0, wx.EXPAND | wx.ALL, 5)

            self.m_panel4 = wx.Panel(
                self, wx.ID_ANY, wx.DefaultPosition, wx.Size(100, 100), wx.TAB_TRAVERSAL)
            self.m_panel4.SetBackgroundColour(wx.Colour(12, 24, 33))

            fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
            fgSizer1.SetFlexibleDirection(wx.BOTH)
            fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

            self.m_checkBox1 = wx.CheckBox(
                self.m_panel4, wx.ID_ANY, u"Landscape", wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_checkBox1.SetForegroundColour(wx.Colour(14, 124, 123))

            fgSizer1.Add(self.m_checkBox1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

            self.m_checkBox2 = wx.CheckBox(
                self.m_panel4, wx.ID_ANY, u"Portrait", wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_checkBox2.SetForegroundColour(wx.Colour(14, 124, 123))

            fgSizer1.Add(self.m_checkBox2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

            self.m_bpButton1 = wx.BitmapButton(self.m_panel4, wx.ID_ANY, wx.Bitmap(
                u"G:\\landscape.bmp", wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_bpButton1.SetForegroundColour(
                wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

            fgSizer1.Add(self.m_bpButton1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

            self.m_bpButton2 = wx.BitmapButton(self.m_panel4, wx.ID_ANY, wx.Bitmap(
                u"G:\\portrate.bmp", wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
            fgSizer1.Add(self.m_bpButton2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

            self.m_panel4.SetSizer(fgSizer1)
            self.m_panel4.Layout()
            bSizer1.Add(self.m_panel4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

            self.SetSizer(bSizer1)
            self.Layout()

            self.Centre(wx.BOTH)

	
		
class NodeEditor(wx.Panel):
    def __init__(self, parent, ID, tplSize, *args):
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

    def drawTestRects(self, dc):
        dc.SetBrush(wx.Brush("#000000", style=wx.SOLID))
        dc.DrawRectangle(50, 50, 50, 50)
        dc.DrawRectangle(100, 100, 100, 100)

    def onPaint(self, event):
        event.Skip()

        dc = wx.PaintDC(self)
        dc.BeginDrawing()
        dc.EndDrawing()

    def onPaint(self, e):
        self.dc = wx.PaintDC(self)

        #dc.Clear()
        #dc.DrawBitmap(wx.Bitmap("python.jpg"),10,10,True)
        self.createNode("Palyer", 200, 200, 100, 100)
        self.createNode("Key Down", 400, 300, 100, 100)
        self.displayNodes()
        self.gc = wx.GraphicsContext.Create(self.dc)
        self.gc.PushState()
        self.drawBezier(300, 200, 400, 300)
        self.gc.PopState()
        #self.dc.EndDrawing()

    def drawBezier(self, toX, toY, fromX, fromY):
        self.gc.SetPen(wx.Pen("#0E7C7B", 2))
        path = self.gc.CreatePath()
        path.MoveToPoint(wx.Point2D(toX, toY))  # where to move
        # Adds a cubic Bezier curve from the current point, using two control points and an end point.
        path.AddCurveToPoint(wx.Point2D(toX+50, toY+10),
                             wx.Point2D(fromX-70, fromY-10),
                             wx.Point2D(fromX, fromY))
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
                    n.translate(dx, dy)
            for n in self.Nodes:
                for p in n.pins:
                    if p.selected == True:
                        if p._type_ == 'output':
                            self.drawBezier(p.x+n.x, p.y+n.y, evtPos[0], evtPos[1])
                        else :
                            self.drawBezier(evtPos[0], evtPos[1],p.x+n.x , p.y+n.y)
            self.displayNodes()

            try:
                rect = wx.Rect(topLeft=(0, 0), bottomRight=evtPos)
            except TypeError as exc:  # topLeft = NoneType. Attempting to double click image or something
                return
            except Exception as exc:
                raise exc

    def onLeftDown(self, event):
        x = event.GetX()
        y = event.GetY()
        self.start = [x, y]
        self.current = self.start
        print("left down", self.start)
        noneSelected = 1
        for n in self.Nodes:
                if n.isInside(self.start[0], self.start[1]):
                    n.setSelectedTrue()
                    noneSelected = 0
                    wx.SetCursor(wx.StockCursor(wx.CURSOR_HAND))

        if noneSelected == 1:
            for n in self.Nodes:
                    n.setSelectedFalse()
                    wx.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))

        self.displayNodes()

    def onLeftUp(self, event):
        x = event.GetX()
        y = event.GetY()
        self.end = [x, y]
        self.start = None
        print("left Up", self.start)

        flag, spid, sptp = 0, -1, ''
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
                    if node.isInsideOnly(x, y):
                        p = node.isInsidePinOnly(x, y)
                        if p:
                            n.createConnection(x, y, node.id, p.id, spid, sptp)

        for n in self.Nodes:
                for p in n.pins:
                    p.selected = False

    def onRightDown(self, event):
        x = event.GetX()
        y = event.GetY()
        print("Right down", x, y)
        self.createNode("New Node", x, y, 100, 100)
        #brush = wx.Brush(wx.Colour(192,192,192,0x80))
        self.displayNodes()

    def createMenu(self):
        self.dc.DrawRectangleList()

    def onRightUp(self, event):
        print("Right up")

    def createNode(self, title, x, y, width, height):
        n = self.node_module.Node(title, x, y, width, height)
        self.Nodes.append(n)

    def addPin(self, _type_):
        pass

    def createNodeConnector(self):
        pass

    def displayConnector(self):
        pass

    def displayNodes(self):
        self.dc = wx.ClientDC(self)
        for n in self.Nodes:
            if n.selected:
                #brush = wx.Brush(wx.Colour(192,192,192,0x80))
                self.dc.SetBrush(wx.Brush('#324A5F'))
                self.dc.DrawRectangle(n.x, n.y, n.width, n.height)
                self.dc.DrawRectangle(n.x, n.y-25, n.width, 25)
                for p in n.pins:
                    if p._type_ == 'input':
                        # input pins
                        self.dc.SetBrush(wx.Brush('#324A5F'))
                        self.dc.DrawCircle(n.x, n.y+p.y, n.radius)
                        self.dc.SetBrush(wx.Brush('#CCC9DC'))
                        self.dc.DrawCircle(n.x, n.y+p.y, n.radius-2)
                    else:
                        # output pins
                        self.dc.SetBrush(wx.Brush('#324A5F'))
                        self.dc.DrawCircle(n.x+n.width, n.y+p.y, n.radius)
                        self.dc.SetBrush(wx.Brush('#CCC9DC'))
                        self.dc.DrawCircle(n.x+n.width, n.y+p.y, n.radius-2)

                font = wx.Font(14, wx.ROMAN, wx.ITALIC, wx.NORMAL)
                self.dc.SetFont(font)
                self.dc.DrawText(n.title, n.x+10, n.y-20)
            else:
                self.dc.SetBrush(wx.Brush(n.COLOR))
                self.dc.DrawRectangle(n.x, n.y, n.width, n.height)
                self.dc.DrawRectangle(n.x, n.y-25, n.width, 25)

                for p in n.pins:
                    if p._type_ == 'input':
                        # input pins
                        self.dc.SetBrush(wx.Brush('#324A5F'))
                        self.dc.DrawCircle(n.x, n.y+p.y, n.radius)
                        self.dc.SetBrush(wx.Brush('#CCC9DC'))
                        self.dc.DrawCircle(n.x, n.y+p.y, n.radius-2)
                    else:
                        # output pins
                        self.dc.SetBrush(wx.Brush('#324A5F'))
                        self.dc.DrawCircle(n.x+n.width, n.y+p.y, n.radius)
                        self.dc.SetBrush(wx.Brush('#CCC9DC'))
                        self.dc.DrawCircle(n.x+n.width, n.y+p.y, n.radius-2)

                font = wx.Font(14, wx.ROMAN, wx.ITALIC, wx.NORMAL)
                self.dc.SetFont(font)
                self.dc.DrawText(n.title, n.x+10, n.y-20)
                #n.conection()


class ChildFrameSDL(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent, count, _type, *args):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1,
                                         title="Child: %d" % count,size=(400,400))
        # mb = parent.MakeMenuBar()
        # menu = wx.Menu()
        # item = menu.Append(-1, "This is child %d's menu" % count)
        # mb.Append(menu, "&Child")
        # self.SetMenuBar(mb)
        if _type == "sdl":
            p = SDLPanel(self, -1, (640, 480), args[0])
        else:
            p = NodeEditor(self, -1, (640, 480), args[0])

        s = parent.sizerMain()

        s.Add(p, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(s)

        # wx.CallAfter(self.Layout)


class SDLThread:
    def __init__(self, designer):
        self.m_bKeepGoing = self.m_bRunning = False
        self.designer = designer
        self.color = (255, 0, 0)
        self.rect = (10, 10, 100, 100)
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
    def __init__(self, parent, ID, tplSize, *args):
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
        pygame_init_flag = True  # make sure we know that pygame has been imported
        #pygame.display.init()
        #window = pygame.display.set_mode(tplSize)
        self.thread = SDLThread(n)
        self.thread.Start()

    def __del__(self):
        self.thread.Stop()
        print("thread stoped")
        #very important line, this makes sure that pygame exits before we
        #reinitialize it other wise we get errors
        pygame.quit()


if __name__ == '__main__':
    app = wx.App()
    NodeEditor(None, 'Node Editor')
    app.MainLoop()
