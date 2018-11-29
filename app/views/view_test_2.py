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
import wx.dataview
import wx.propgrid as pg

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

        def __init__( self, parent ):
                wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 736,490 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

                #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
                self.SetBackgroundColour( wx.Colour( 12, 24, 33 ) )

                self.m_statusBar1 = self.CreateStatusBar( 1, 0, wx.ID_ANY )
                self.m_statusBar1.SetBackgroundColour( wx.Colour( 12, 24, 33 ) )

                self.m_menubar1 = wx.MenuBar( 0 )
                self.m_menubar1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
                self.m_menubar1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )

                self.m_menu1 = wx.Menu()
                self.m_menubar1.Append( self.m_menu1, u"File" ) 

                self.m_menu2 = wx.Menu()
                self.m_menubar1.Append( self.m_menu2, u"view" ) 

                self.SetMenuBar( self.m_menubar1 )

                bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

                bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

                self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 10,-1 ), wx.HSCROLL|wx.VSCROLL )
                self.m_scrolledWindow1.SetScrollRate( 5, 5 )
                self.m_scrolledWindow1.SetMaxSize( wx.Size( 100,-1 ) )

                bSizer3.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )

                self.m_auinotebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 450,-1 ), wx.aui.AUI_NB_DEFAULT_STYLE )
                self.m_auinotebook1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
                self.m_auinotebook1.SetBackgroundColour( wx.Colour( 27, 42, 65 ) )
                self.m_auinotebook1.SetMaxSize( wx.Size( 400,-1 ) )


                bSizer3.Add( self.m_auinotebook1, 1, wx.EXPAND |wx.ALL, 5 )

                bSizer2 = wx.BoxSizer( wx.VERTICAL )

                self.m_dataViewCtrl1 = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 130,200 ), 0 )
                bSizer2.Add( self.m_dataViewCtrl1, 0, wx.ALL, 5 )

                self.m_propertyGridManager1 = pg.PropertyGridManager(self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 130,200 ), wx.propgrid.PGMAN_DEFAULT_STYLE)
                self.m_propertyGridManager1.SetExtraStyle( wx.propgrid.PG_EX_MODE_BUTTONS ) 

                self.m_propertyGridPage1 = self.m_propertyGridManager1.AddPage( u"Page", wx.NullBitmap );
                self.m_propertyGridItem1 = self.m_propertyGridPage1.Append( pg.StringProperty( u"Name", u"Name" ) ) 
                self.m_propertyGridItem6 = self.m_propertyGridPage1.Append( pg.StringProperty( u"Name", u"Name" ) ) 
                self.m_propertyGridItem7 = self.m_propertyGridPage1.Append( pg.StringProperty( u"Name", u"Name" ) ) 
                self.m_propertyGridItem8 = self.m_propertyGridPage1.Append( pg.StringProperty( u"Name", u"Name" ) ) 
                self.m_propertyGridItem9 = self.m_propertyGridPage1.Append( pg.StringProperty( u"Name", u"Name" ) ) 
                self.m_propertyGridItem2 = self.m_propertyGridPage1.Append( pg.StringProperty( u"Name", u"Name" ) ) 
                self.m_propertyGridItem3 = self.m_propertyGridPage1.Append( pg.StringProperty( u"Name", u"Name" ) ) 
                self.m_propertyGridItem4 = self.m_propertyGridPage1.Append( pg.StringProperty( u"Name", u"Name" ) ) 
                self.m_propertyGridItem5 = self.m_propertyGridPage1.Append( pg.StringProperty( u"Name", u"Name" ) ) 


                bSizer2.Add()
                ##bSizer2.Add( self.m_propertyGridManager1, 0, wx.ALL, 5 )

                        
                bSizer3.Add( bSizer2, 1, wx.EXPAND, 5 )
                        
                        
                bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
                self.SetSizer(bSizer1)
                #self.SetSizer( bSizer1 )
                        
                self.Layout()


                #self.Centre( wx.BOTH )

        def __del__( self ):
                pass

if __name__ == "__main__":
        app = wx.App(False)
        frame = MyFrame1(None)
        frame.Show()
        app.MainLoop()


