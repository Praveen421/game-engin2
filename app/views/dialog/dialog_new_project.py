# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Project
###########################################################################

class MyDialog ( wx.Dialog ):
	
	def __init__( self, parent):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"New Project", pos = wx.DefaultPosition, size = wx.Size( 563,253 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 12, 24, 33 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.Colour( 12, 24, 33 ) )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Project Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetForegroundColour( wx.Colour( 14, 124, 123 ) )
		
		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 340,-1 ), 0 )
		self.m_textCtrl1.SetBackgroundColour( wx.Colour( 27, 42, 65 ) )
		
		bSizer2.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button1 = wx.Button( self.m_panel2, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.m_button1.SetBackgroundColour( wx.Colour( 50, 74, 95 ) )
		
		bSizer2.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,100 ), wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.Colour( 12, 24, 33 ) )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_checkBox1 = wx.CheckBox( self.m_panel4, wx.ID_ANY, u"Landscape", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetForegroundColour( wx.Colour( 14, 124, 123 ) )
		
		fgSizer1.Add( self.m_checkBox1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self.m_panel4, wx.ID_ANY, u"Portrait", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetForegroundColour( wx.Colour( 14, 124, 123 ) )
		
		fgSizer1.Add( self.m_checkBox2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_bpButton1 = wx.BitmapButton( self.m_panel4, wx.ID_ANY, wx.Bitmap( u"G:\\landscape.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bpButton1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		fgSizer1.Add( self.m_bpButton1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_bpButton2 = wx.BitmapButton( self.m_panel4, wx.ID_ANY, wx.Bitmap( u"G:\\portrate.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer1.Add( self.m_bpButton2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel4.SetSizer( fgSizer1 )
		self.m_panel4.Layout()
		bSizer1.Add( self.m_panel4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
	
if __name__ == "__main__":
	app = wx.App(False)
	frame = Project(None)
	frame.Show()
	app.MainLoop()
        
       
