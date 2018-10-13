'''
MIT License

Copyright (c) 2018 sidd5sci

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''
from paths import *
import os,importlib
from debuger import *
import tkinter as tk
from tkinter import ttk


class UI():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("PyTrack")
        self.center_window(900,600)

        # left Frame
        self.win_left = tk.Frame(self.win,width=200,height=600)
        self.win_left.columnconfigure(0, weight=1)
        self.win_left.rowconfigure(0, weight=1)
        s = ttk.Separator(self.win_left, orient=tk.HORIZONTAL)
        lf = ttk.Labelframe(self.win_left, text='Label')
        self.win_left.pack(side = tk.LEFT)
        # main embed window
        self.tab_control = ttk.Notebook(self.win, width = 650 ,height = 630)
        
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1,text="Designer")
        self.tab_control.pack(expand=1,fill="both")
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2,text="Node Editor")
        self.tab_control.pack(expand=1,fill="both")
        
        
   
    def create_node_editor(self):
        # canvas
        self.canvas = tk.Canvas(self.tab2,width= 800,height=600)
        self.canvas.create_rectangle([10,10, 650,630], fill = 'blue')
        self.canvas.pack(fill = tk.BOTH, expand = 1)
        self.canvas.update()

    def center_window(self,width=300, height=200):
        # get screen width and height
        screen_width = self.win.winfo_screenwidth()
        screen_height = self.win.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.win.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
    def top_menu(self):
                
        # creating the menu for GUI
        menu = tk.Menu(self.win)
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
    
    def run(self):
        self.win.mainloop()
   
    def about(self):
        print ('about the game engine')



def part(str):
    # split the tring by '.'
    name,ext = str.split('.')
    return name

def load_lib():
    global libs,lib_names
    names = os.listdir(libs_path)
    for l in names:
        
        if l != '__pycache__':
            # lib name
            LIB_NAME = 'lib.'+part(l)
            # storing libs names loaded
            lib_names.append(part(l))
            # loading the libs
            libs.append(importlib.import_module(LIB_NAME,'.'))

    # debug message
    d.log("Loader",lib_names)

def find_module(str):
    global lib_names,libs

    k= [i for i in range(len(lib_names)) if lib_names[i]==str]
    return libs[k[0]]

def create_new_project():
    # start the new project window     
    newDialog = importlib.import_module('dialog_new_project','.')
    newDialogObject =  newDialog.Project()
    newDialogObject.startWindow()
    
        
    

#######################################################
### globals
#######################################################
d = debuger()
lib_names  = list()
libs  = list()


def main():
    load_lib()
    '''
    designer = libs[1].Designer(find_module('layer'),
            find_module('camera'),
            find_module('pointer'),
            find_module('rect'),
            find_module('tile'),path=path)'''
    #designer.main()
    #create_new_project()
    app = UI()
    app.top_menu()
    app.create_node_editor()
    app.run()

if __name__ == "__main__":
        main()