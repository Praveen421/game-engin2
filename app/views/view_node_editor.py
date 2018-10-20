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

class NodeEditor(wx.Frame):
    def __init__(self, parent, title,*args):
        super(NodeEditor, self).__init__(parent, title=title, 
            size=(250, 550))

        self.node_module = args[0]
        self.Nodes = []

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Centre()
        self.Show()

    def initEditor(self):
        # bind mouse ,key
        pass

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        dc.DrawLine(50, 60, 190, 60)

        dc.SetBrush(wx.Brush('#c50024'))
        dc.DrawRectangle(130, 105, 90, 60)
    def displayNodes(self):
        for n in self.Nodes:
            dc.DrawRectangle([n.x,n.y,n.x+n.width,n.y+n.height])
            dc.DrawRectangle([n.x,n.y-25,n.x+n.width,n.y])
            
            font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL) 
            dc.SetFont(font) 
            dc.DrawText(n.title,n.x+10,n.y-20) 
            
    

if __name__ == '__main__':
    app = wx.App()
    NodeEditor(None, 'Node Editor')
    app.MainLoop()
