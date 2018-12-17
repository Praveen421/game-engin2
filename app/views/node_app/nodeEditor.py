import wx

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
                            self.drawBezier(p.x+n.x, p.y+n.y,
                                            evtPos[0], evtPos[1])
                        else:
                            self.drawBezier(
                                evtPos[0], evtPos[1], p.x+n.x, p.y+n.y)
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

