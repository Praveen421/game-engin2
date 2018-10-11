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





import tkinter as tk
from tkinter import *
import os


class MainView():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Game engine 3d")
        self.buttonwin = tk.Frame(root,width = 600, height = 600)
        self.buttonwin.columnconfigure(0, weight=1)
        self.buttonwin.rowconfigure(0, weight=1)
    def menu(self):
        # creating the menu for GUI
        self.menu = Menu(root)
        self.root.config(menu=menu)
        # file menu option
        self.filemenu = Menu(menu)
        self.menu.add_cascade(label="File",menu=filemenu)
        self.filemenu.add_command(label = "New" , command=newFile)
        self.filemenu.add_command(label = "Open" , command=fileOpen)
        self.filemenu.add_command(label = "Create" , command=newObject)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "Import" , command=newObject)
        self.filemenu.add_command(label = "Export" , command=newObject)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "Exit" , command=root.quit)
        # create menu
        self.createmenu = Menu(menu)
        self.menu.add_cascade(label="Create", menu=createmenu)
        self.createmenu.add_command(label="Cube", command=createCube)
        self.createmenu.add_command(label="Cone", command=about)
        self.createmenu.add_command(label="Cylinder", command=about)
        self.createmenu.add_command(label="Sphere", command=about)
        self.createmenu.add_command(label="Plane", command=createPlane)
        self.createmenu.add_command(label="Circle", command=createCircle)
        self.createmenu.add_command(label="Human", command=about)
        self.createmenu.add_separator()
        self.createmenu.add_command(label="Light", command=about)
        self.createmenu.add_command(label="Spot light", command=about)
        self.createmenu.add_command(label="Area light", command=about)
        self.createmenu.add_separator()
        self.createmenu.add_command(label="Camera", command=about)
        # physics menu
        self.physicsmenu = Menu(menu)
        self.menu.add_cascade(label="Physics" ,menu = physicsmenu)
        self.physicsmenu.add_command(label="Force", command=about)
        self.physicsmenu.add_command(label="Torque", command=about)
        # Genatic algorithms
        self.GAmenu = Menu(menu)
        self.menu.add_cascade(label="GA" ,menu = GAmenu)
        self.GAmenu.add_command(label="Init Sequence", command=initGA)
        self.GAmenu.add_command(label="Live", command=livePopulation)
        # help menu option
        self.helpmenu = Menu(menu)
        self.menu.add_cascade(label="Help" ,menu = helpmenu)
        self.helpmenu.add_command(label="About", command=about)
        self.helpmenu.add_command(label="Version", command=about)
        self.helpmenu.add_command(label="Update", command=about)

