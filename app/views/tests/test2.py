import wx
import wx.aui
import os
import threading
global pygame # when we import it, let's keep its proper name!
global pygame_init_flag
pygame_init_flag = False
from pygame.locals import *

import sys; sys.path.insert(0, "..")

class ParentFrame(wx.aui.AuiMDIParentFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIParentFrame.__init__(self, parent, -1,
                                          title="AuiMDIParentFrame",
                                          size=(640,480),
                                          style=wx.DEFAULT_FRAME_STYLE)
        self.count = 0
        mb = self.MakeMenuBar()
        self.SetMenuBar(mb)
        self.CreateStatusBar()

    def MakeMenuBar(self):
        mb = wx.MenuBar()
        menu = wx.Menu()
        item = menu.Append(-1, "New SDL child window\tCtrl-N")
        self.Bind(wx.EVT_MENU, self.OnNewChild, item)
        item = menu.Append(-1, "Close parent")
        self.Bind(wx.EVT_MENU, self.OnDoClose, item)
        mb.Append(menu, "&File")
        return mb
        
    def OnNewChild(self, evt):
        self.count += 1
        child = ChildFrameSDL(self, self.count)
        child.Show()

    def OnDoClose(self, evt):
        self.Close()

class ChildFrameSDL(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent, count):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1,
                                         title="Child: %d" % count)
        mb = parent.MakeMenuBar()
        menu = wx.Menu()
        item = menu.Append(-1, "This is child %d's menu" % count)
        mb.Append(menu, "&Child")
        self.SetMenuBar(mb)
        
        p = SDLPanel(self, -1, (640,480))

        sizer = wx.BoxSizer()
        sizer.Add(p, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
        wx.CallAfter(self.Layout)

class SDLThread:
    def __init__(self,screen):
        self.m_bKeepGoing = self.m_bRunning = False
        self.screen = screen
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
            e = pygame.event.poll()
            if e.type == pygame.MOUSEBUTTONDOWN:
                self.color = (255,0,128)
                self.rect = (e.pos[0], e.pos[1], 100, 100)
                print (e.pos)
                self.screen.fill((0,0,0))
                self.screen.fill(self.color,self.rect)
            if self.init:
                self.screen.fill((0,0,0))
                self.screen.fill(self.color,self.rect)
            pygame.display.flip()
        self.m_bRunning = False;
        print ("pygame draw loop exited")
 
class SDLPanel(wx.Panel):
    def __init__(self,parent,ID,tplSize):
        global pygame
        global pygame_init_flag
        wx.Panel.__init__(self, parent, ID, size=tplSize)
        self.Fit()
        os.environ['SDL_WINDOWID'] = str(self.GetHandle())
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        #here is where things change if pygame has already been initialized 
        #we need to do so again
        if pygame_init_flag:
            #call pygame.init() on subsaquent windows
            pygame.init()
        else:
            #import if this is the first time
            import pygame
        pygame_init_flag = True #make sure we know that pygame has been imported
        pygame.display.init()
        window = pygame.display.set_mode(tplSize)
        self.thread = SDLThread(window)
        self.thread.Start()

    def __del__(self):
        self.thread.Stop()
        print( "thread stoped")
        #very important line, this makes sure that pygame exits before we 
        #reinitialize it other wise we get errors
        pygame.quit()

app = wx.PySimpleApp()
frame = ParentFrame(None)
frame.Show()
app.MainLoop()