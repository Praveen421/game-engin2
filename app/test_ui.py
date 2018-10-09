# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep 22 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx,sys
import wx.xrc
import wx.aui

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame(wx.Frame):

	def __init__(self,parent, title):
			super(MyFrame, self).__init__(parent, title=title, 
            								size=(250, 550))
			self.fuck()
	def fuck(self):

			import sys,os
			##Note we call the GetHandle() method of a control in the window/frame, not the wxFrame itself
			self.hwnd = self.GetChildren()
			if sys.platform == "win32":
				os.environ['SDL_VIDEODRIVER'] = 'windib'
			os.environ['SDL_WINDOWID'] = str(self.hwnd) #must be before init

			## NOTE WE DON'T IMPORT PYGAME UNTIL NOW.  Don't put "import pygame" at the top of the file.
			import pygame
			pygame.display.init()

			self.display = pygame.display.set_mode((400,400)) #size no matter

			pygame.display.set_caption("PyTrack | v1.0.1")
			# initilise the clock
			self.clock = pygame.time.Clock()
		
			self.screen.fill(pygame.Color(255,255,255))
			pygame.display.init()
			pygame.display.update()
    


if __name__ == '__main__':
   
        app = wx.App(False)
        frame = MyFrame(None,"hj")
        frame.Show()
        app.MainLoop()