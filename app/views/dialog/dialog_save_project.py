# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os

###########################################################################
## Class Project
###########################################################################

class MyDialog ( wx.Dialog ):
	
	def __init__( self, parent):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Save As", pos = wx.DefaultPosition, size = wx.Size( 563,253 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		
		self.SetBackgroundColour( wx.Colour( 12, 24, 33 ) )
		wildcard = "Text Files (*.txt)|*.txt" 
                # wildcard = "BMP and GIF files (*.bmp;*.gif)|*.bmp;*.gif|PNG files (*.png)|*.png"
                # self.text = wx.TextCtrl(self, size = (-1,200),style = wx.TE_MULTILINE) 
                
                #  ask the user what new file to open
                with wx.FileDialog(self, "Save Project", wildcard="XYZ files (*.xyz)|*.xyz",
                       style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as dlg:

                        if dlg.ShowModal() == wx.ID_CANCEL:
                                return     # the user changed their mind

                        # save the current contents in the file
                        self.pathname = dlg.GetPath()
                        # try:
                        #         with open(pathname, 'w') as file:
                        #                 self.doSaveData(file)
                        # except IOError:
                        #         wx.LogError("Cannot save current data in file '%s'." % pathname)
                                
                dlg.Destroy() 
		
	
	def __del__( self ):
		pass
	
	
if __name__ == "__main__":
	app = wx.App(False)
	frame = Project(None)
	frame.Show()
	app.MainLoop()
        
       
