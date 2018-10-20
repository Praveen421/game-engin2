# -*- coding: utf-8 -*- 

import os
import wx
import wx.xrc

from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

#from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"计算机插值 v0.1", pos = wx.DefaultPosition, size = wx.Size( 428,235 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_SHAPED|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        
        self.Creat_menu()
        self.Creat_sizer()
        self.Bind_event()
        
        self.ButtonPlt.Disable()
        
        #Necessary varible
        self.x = np.array([1.2,1.3,1.4,1.5,1.6,1.8,1.9,2.0])
        self.y = np.array([0.15,0.34,0.57,0.72,0.95,1.29,1.58,1.94])
        
    def __del__( self ):
        pass
    
    def Creat_menu( self ):
        self.MainMenu = wx.MenuBar( 0 )
        self.File = wx.Menu()
        self.Load = wx.MenuItem( self.File, wx.ID_ANY, u"载入数据...", wx.EmptyString, wx.ITEM_NORMAL )
        self.File.AppendItem( self.Load )
        
        self.Save = wx.MenuItem( self.File, wx.ID_ANY, u"另存数据...", wx.EmptyString, wx.ITEM_NORMAL )
        self.File.AppendItem( self.Save )        
        
        self.Exit = wx.MenuItem( self.File, wx.ID_ANY, u"退出...", wx.EmptyString, wx.ITEM_NORMAL )
        self.File.AppendItem( self.Exit )
        
        self.MainMenu.Append( self.File, u"文件" ) 
        
        self.About_M = wx.Menu()
        self.About = wx.MenuItem( self.About_M, wx.ID_ANY, u"关于", wx.EmptyString, wx.ITEM_NORMAL )
        self.About_M.AppendItem( self.About )
        
        self.MainMenu.Append( self.About_M, u"关于" ) 
        
        self.SetMenuBar( self.MainMenu )
        
    def Creat_sizer( self ):
        MainSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.MainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        UserSizer = wx.BoxSizer( wx.VERTICAL )
        
        upperSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.TextExplanation = wx.StaticText( self.MainPanel, wx.ID_ANY, u"请在下面输入框内输入要插值的数，以空格间隔。\n默认输入范围在[1.2, 2.0],依载入数据改变。\n提示：必须在计算后绘图。", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.TextExplanation.Wrap( -1 )
        upperSizer.Add( self.TextExplanation, 0, wx.ALL, 20 )
        
        
        #upperSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        RadioBoxInterpolationChoices = [ u"线性插值", u"抛物线插值" ]
        self.RadioBoxInterpolation = wx.RadioBox( self.MainPanel, wx.ID_ANY, u"插值种类", wx.DefaultPosition, wx.DefaultSize, RadioBoxInterpolationChoices, 1, wx.RA_SPECIFY_COLS )
        self.RadioBoxInterpolation.SetSelection( 0 )
        upperSizer.Add( self.RadioBoxInterpolation, 0, wx.ALL, 5 )
        
        
        UserSizer.Add( upperSizer, 1, wx.ALL|wx.EXPAND, 5 )
        
        lowerSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        
        #lowerSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.TextCtrVal = wx.TextCtrl( self.MainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        lowerSizer.Add( self.TextCtrVal, 0, wx.ALL, 5 )
        
        
        #lowerSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.ButtonCal = wx.Button( self.MainPanel, wx.ID_ANY, u"计算", wx.DefaultPosition, wx.DefaultSize, 0 )
        lowerSizer.Add( self.ButtonCal, 0, wx.ALL, 5 )
        
        self.ButtonPlt = wx.Button( self.MainPanel, wx.ID_ANY, u"绘图", wx.DefaultPosition, wx.DefaultSize, 0 )
        lowerSizer.Add( self.ButtonPlt, 0, wx.ALL, 5 )
        
        self.ButtonCls = wx.Button( self.MainPanel, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0 )
        lowerSizer.Add( self.ButtonCls, 0, wx.ALL, 5 )
        
        
        UserSizer.Add( lowerSizer, 1, wx.EXPAND, 5 )
        
        
        self.MainPanel.SetSizer( UserSizer )
        self.MainPanel.Layout()
        UserSizer.Fit( self.MainPanel )
        MainSizer.Add( self.MainPanel, 1, wx.EXPAND |wx.ALL, 1 )
        
        
        self.SetSizer( MainSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
    
    # Connect Events
    def Bind_event( self ):        
        self.Bind( wx.EVT_MENU, self.LoadFile, id = self.Load.GetId() )
        self.Bind( wx.EVT_MENU, self.SaveFile, id = self.Save.GetId() )
        self.Bind( wx.EVT_MENU, self.ExitIt, id = self.Exit.GetId() )
        self.Bind( wx.EVT_MENU, self.Dialog, id = self.About.GetId() )
        self.TextCtrVal.Bind( wx.EVT_TEXT_ENTER, self.Calculate )
        self.ButtonCal.Bind( wx.EVT_BUTTON, self.Calculate )
        self.ButtonPlt.Bind( wx.EVT_BUTTON, self.Plot )
        self.ButtonCls.Bind( wx.EVT_BUTTON, self.Clear )
    
    # Virtual event handlers, overide them in your derived class
    def LoadFile( self, event ):
        file_choices = "TXT (*.txt)|*.txt"
        
        dlg = wx.FileDialog(
            self, 
            message=u"载入数据文件...",
            defaultDir=os.getcwd(),
            defaultFile="data.txt",
            wildcard=file_choices,
            style=wx.OPEN | wx.CHANGE_DIR)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            try:            
                self.load = np.loadtxt(path)
                self.x = self.load[0,:]
                self.y = self.load[1,:]
                print (self.x)
                dlg2 = wx.MessageDialog( self, u"载入数据成功\nX=" + str(self.x) + "\nY=" + str(self.y), u"载入信息", wx.OK)
                dlg2.ShowModal()
                dlg2.Destroy()
            except Exception:
                dlg2 = wx.MessageDialog( self, u"载入数据失败" , u"载入信息", wx.OK)
                dlg2.ShowModal()
                dlg2.Destroy()
    
    def SaveFile( self, event ):
        file_choices = "TXT (*.txt)|*.txt"
        
        dlg = wx.FileDialog(
            self, 
            message=u"存储数据到...",
            defaultDir=os.getcwd(),
            defaultFile="result.txt",
            wildcard=file_choices,
            style=wx.SAVE)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            try:
                np.savetxt(path,self.result)
                dlg2 = wx.MessageDialog( self, u"成功存储运算结果到\n%s" %path, u"存储信息", wx.OK)
                dlg2.ShowModal()
                dlg2.Destroy()
            except Exception:
                dlg2 = wx.MessageDialog( self, u"存储运算结果失败" , u"存储信息", wx.OK)
                dlg2.ShowModal()
                dlg2.Destroy()
                
    def ExitIt( self, event ):
        self.Close(True)
    
    def Dialog( self, event ):
        dlg = wx.MessageDialog( self, u"A program of interpolation", u"About", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    
    def Calculate( self, event ):
        self.f1 = interpolate.interp1d(self.x, self.y, kind='linear')
        self.f2 = interpolate.interp1d(self.x, self.y, kind='quadratic')
        self.iMethod = self.RadioBoxInterpolation.GetSelection()
        if self.iMethod == 0:
            f = self.f1
        elif self.iMethod == 1:
            f = self.f2
        
        MyArray = map(float, self.TextCtrVal.GetValue().split())
        self.xnew = np.array(MyArray)
        title = u"计算结果"
        self.ButtonPlt.Enable()
        try:
            self.result = f(self.xnew)
        except ValueError:
            self.result = u"输入错误，数值越界"
            title = u"警告！"
            self.ButtonPlt.Disable()
        except:
            self.result = u"未知错误"
            title = u"警告！"
            self.ButtonPlt.Disable()
        dlg = wx.MessageDialog( self, u"%s" %self.result, u"%s" %title, wx.OK)
        dlg.ShowModal() 
        dlg.Destroy() 
    
    
    def Plot( self, event ):
        if self.iMethod == 0:
            method = 'Linear'
        elif self.iMethod == 1:
            method = 'Quadratic'
        plt.figure(u"图示")
        plt.plot(self.x,self.y,'o',self.xnew,self.result,'g^')
        plt.legend(["Data", "Result"], loc='best')
        plt.suptitle("%s Interpolation" %method,fontsize=18)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.show()
        
    def Clear( self, event ):
        self.TextCtrVal.Clear()    

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        
if __name__ == '__main__': 
    app = wx.PySimpleApp()
    app.frame = MainFrame(None)
    app.frame.Show()
    app.MainLoop()
