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


import os,time
import tkinter as tk
from tkinter import ttk

class UI():
    def __init__(self,*args):
        # libs
        self.node_module = args[0]
        
        
        self.Nodes = []

        # main window
        self.win = tk.Tk()
        self.win.title("PyTrack")
        self.center_window(900,650)

        # left Frame
        self.win_left = tk.Frame(self.win,width=200,height=600)
        self.win_left.columnconfigure(0, weight=1)
        self.win_left.rowconfigure(0, weight=1)
        s = ttk.Separator(self.win_left, orient=tk.HORIZONTAL)
        lf = ttk.Labelframe(self.win_left, text='Label')
        self.win_left.pack(side = tk.LEFT)
        # center embed window
        self.tab_control = ttk.Notebook(self.win, width = 650 ,height = 630)
        
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1,text="Designer")
        self.tab_control.pack(expand=1,fill="both")
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2,text="Node Editor")
        self.tab_control.pack(expand=1,fill="both")
        
    def InitEvents(self):
        self.canvas.bind('<ButtonPress-1>', self.GraphLeftMousePressed)
        self.canvas.bind('<ButtonRelease-1>', self.GraphLeftMouseReleased)
        self.canvas.bind('<ButtonPress-2>', self.GraphScrollPressed)
        self.canvas.bind('<ButtonRelease-2>', self.GraphScrollReleased)
        self.canvas.bind('<ButtonPress-3>', self.GraphRightMousePressed)
        self.canvas.bind('<ButtonRelease-3>', self.GraphRightMouseReleased)
        self.win.bind('<Delete>', self.DeleteBtnPressed)
    
    def displayNodes(self):
        for n in self.Nodes:
            self.canvas.create_rectangle([n.x,n.y,n.x+n.width,n.y+n.height], fill = '#1b2a41')
            self.canvas.create_rectangle([n.x,n.y-25,n.x+n.width,n.y], fill = '#324a5f')
            self.canvas.create_text((n.x+10,n.y-20),anchor=tk.NW,fill="#0e7c7b",text=n.title)
    
    def CreateNodesMenu(self, Pos):
        self.NodesMenu = GraphNodesMenu.GraphNodesMenu(self, Pos)
       
    def create_node(self,name,x,y,width,height):
        n = self.node_module.Node(name,x,y,width,height)
        self.Nodes.append(n)

    def create_node_editor(self):
        # canvas
        self.canvas = tk.Canvas(self.tab2,width= 800,height=600,bg='#0c1821')
        self.canvas.pack(fill = tk.BOTH, expand = 1)
        self.canvas.update()

    def create_popup_menu(self,x,y,height,width):
        self.popupMenu = tk.Frame(self.canvas, bg='#1b2a41')
        self.popupMenu.pack()
        self.popupMenu.configure(width=width,height=height)
        self.popupMenu.place_configure(x=x,y=y)

        # listbox 
        self.listBox = tk.Listbox(self.popupMenu)
        self.listBox.pack(side=tk.LEFT)
        self.Scrollbar = tk.Scrollbar(self.popupMenu)
        self.Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listBox.insert(1,"Player")
        self.listBox.insert(2,"Object")
        self.listBox.insert(3,"Background")
        self.listBox.insert(4,"Camera")
        self.listBox.insert(5,"Sounds")
        self.listBox.insert(6,"Music")

        # remove scroll
        self.listBox.config(yscrollcommand=self.Scrollbar.set)
        self.Scrollbar.config(command=self.listBox.yview)

        self.listBox.bind('<<ListboxSelect>>', lambda event: self.NodesMenuSelected(self.listBox.selection_get()))
    
    def delete_popup_menu(self):
        self.popupMenu.destroy()
    
    def NodesMenuSelected(self, selection):
        print("Menu-selected-: "+selection)
        self.delete_popup_menu()
        x,y = self.GetMousePos()
        self.create_node(selection,x,y,80,80)
        self.win.update()

    def center_window(self,width=300, height=200):
        # get screen width and height
        screen_width = self.win.winfo_screenwidth()
        screen_height = self.win.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.win.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    def GetMousePos(self):
        x = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        y = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
        return x,y

    def DeleteBtnPressed(self, event):
        self.Controller.DeleteBtnPressed()

    def NodeLeftMousePressed(self, node):
        self.Controller.NodeLeftMousePressed(node)

    def NodeLeftMouseReleased(self, node):
        self.Controller.NodeLeftMouseReleased(node)

    def NodeInputLeftMousePressed(self, node):
        self.Controller.NodeInputLeftMousePressed(node)

    def NodeInputLeftMouseReleased(self, node):
        self.Controller.NodeInputLeftMouseReleased(node)

    def NodeOutputLeftMousePressed(self, node):
        self.Controller.NodeOutputLeftMousePressed(node)

    def NodeOutputLeftMouseReleased(self, node):
        self.Controller.NodeOutputLeftMouseReleased(node)

    def NodePinLeftMousePressed(self, node, pin):
        self.Controller.NodePinLeftMousePressed(node, pin)

    def NodePinLeftMouseReleased(self, node, pin):
        self.Controller.NodePinLeftMouseReleased(node, pin)

    def GraphLeftMousePressed(self,event):
        print('Graph-LeftMousePressed')
        self.delete_popup_menu()

    def GraphLeftMouseReleased(self,event):
        print('Graph-LeftMouseReleased')

    def GraphScrollPressed(self,event):
        self.Controller.GraphScrollPressed()

    def GraphScrollReleased(self,event):
        self.Controller.GraphScrollReleased()

    def GraphRightMousePressed(self,event):
        print('Graph-RightMousePressed')
        x,y = self.GetMousePos()
        self.create_popup_menu(x,y,100,200)

    def GraphRightMouseReleased(self,event):
        print('Graph-RightMouseReleased')

    def NodeSettingsBtnClicked(self,event):
        print('NodeSettingsBtnClicked')

    def GlobalSettingsBtnClicked(self,event):
        print('GlobalSettingsBtnClicked')

    
    def top_menu(self):
                
        # creating the menu for GUI
        menu = tk.Menu(self.win,bg='#212121')
        self.win.config(menu=menu)
        # file menu option
        filemenu = tk.Menu(menu)
        menu.add_cascade(label="File",menu=filemenu)
        filemenu.add_command(label = "New" , command=self.about)
        filemenu.add_command(label = "Open" , command=self.about)
        filemenu.add_command(label = "Create" , command=self.about)
        filemenu.add_separator()
        filemenu.add_command(label = "Import" , command=self.about)
        filemenu.add_command(label = "Export" , command=self.about)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit" , command=self.win.quit)
        # create menu
        createmenu = tk.Menu(menu)
        menu.add_cascade(label="Create", menu=createmenu)
        createmenu.add_command(label="Cube", command=self.about)
        createmenu.add_command(label="Cone", command=self.about)
        createmenu.add_command(label="Cylinder", command=self.about)
        createmenu.add_command(label="Sphere", command=self.about)
        createmenu.add_command(label="Plane", command=self.about)
        createmenu.add_command(label="Circle", command=self.about)
        createmenu.add_command(label="Human", command=self.about)
        createmenu.add_separator()
        createmenu.add_command(label="Light", command=self.about)
        createmenu.add_command(label="Spot light", command=self.about)
        createmenu.add_command(label="Area light", command=self.about)
        createmenu.add_separator()
        createmenu.add_command(label="Camera", command=self.about)
        # physics menu
        physicsmenu = tk.Menu(menu)
        menu.add_cascade(label="Physics" ,menu = physicsmenu)
        physicsmenu.add_command(label="Force", command=self.about)
        physicsmenu.add_command(label="Torque", command=self.about)
        # Genatic algorithms
        GAmenu = tk.Menu(menu)
        menu.add_cascade(label="GA" ,menu = GAmenu)
        GAmenu.add_command(label="Init Sequence", command=self.about)
        GAmenu.add_command(label="Live", command=self.about)
        # help menu option
        helpmenu = tk.Menu(menu)
        menu.add_cascade(label="Help" ,menu = helpmenu)
        helpmenu.add_command(label="About", command=self.about)
        helpmenu.add_command(label="Version", command=self.about)
        helpmenu.add_command(label="Update", command=self.about)
    
    def DeleteNodesMenu(self):
        if self.NodesMenu:
            self.NodesMenu.Delete()
            del self.NodesMenu
            self.NodesMenu = None
    
    def run(self):
        #self.win.after(16,self.customLoop)
        self.win.mainloop()
   
    def about(self):
        print ('about the game engine')
        
    def customLoop(self):
        self.create_node("New node",100,100,80,80)
        self.create_node("New 1",320,200,80,80)
        self.displayNodes()
        self.InitEvents()

        #self.win.after(16,self.customLoop)


