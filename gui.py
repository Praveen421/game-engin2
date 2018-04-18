# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

###########################################################################
## Class Polar
###########################################################################

class Polar ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 737,441 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.new = wx.MenuItem( self.file, wx.ID_ANY, u"New Project", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.new )
		
		self.open = wx.MenuItem( self.file, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.open )
		
		self.save = wx.MenuItem( self.file, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.save )
		
		self.saveAs = wx.MenuItem( self.file, wx.ID_ANY, u"Save As ...", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.saveAs )
		
		self.file.AppendSeparator()
		
		self._import = wx.MenuItem( self.file, wx.ID_ANY, u"Import", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self._import )
		
		self.export = wx.MenuItem( self.file, wx.ID_ANY, u"Export", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.export )
		
		self.file.AppendSeparator()
		
		self.exit = wx.MenuItem( self.file, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.exit )
		
		self.m_menubar1.Append( self.file, u"File" ) 
		
		self.edit = wx.Menu()
		self.undo = wx.MenuItem( self.edit, wx.ID_ANY, u"Undo", wx.EmptyString, wx.ITEM_NORMAL )
		self.edit.AppendItem( self.undo )
		
		self.redo = wx.MenuItem( self.edit, wx.ID_ANY, u"Redo", wx.EmptyString, wx.ITEM_NORMAL )
		self.edit.AppendItem( self.redo )
		
		self.m_menubar1.Append( self.edit, u"Edit" ) 
		
		self.window = wx.Menu()
		self.m_menubar1.Append( self.window, u"Window" ) 
		
		self.view = wx.Menu()
		self.m_menubar1.Append( self.view, u"View" ) 
		
		self.help = wx.Menu()
		self.m_menubar1.Append( self.help, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_auinotebook2 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.aui.AUI_NB_DEFAULT_STYLE )
		
		bSizer5.Add( self.m_auinotebook2, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		bSizer5.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_auinotebook3 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.aui.AUI_NB_DEFAULT_STYLE )
		
		bSizer5.Add( self.m_auinotebook3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_auiToolBar5 = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_tool4 = self.m_auiToolBar5.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool5 = self.m_auiToolBar5.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool7 = self.m_auiToolBar5.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_auiToolBar5.AddSeparator()
		
		self.m_tool13 = self.m_auiToolBar5.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool14 = self.m_auiToolBar5.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_auiToolBar5.AddSeparator()
		
		self.m_auiToolBar5.Realize() 
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

if __name__ == '__main__':
   
        app = wx.App(False)
        frame = Polar(None)
        frame.Show()
        app.MainLoop()