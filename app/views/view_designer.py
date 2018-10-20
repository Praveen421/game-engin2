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
#from tkFileDilog import askopenfilename

# alexa voice service




################################################################
def key(event):
    print ("key",repr(event.char))

def newObject():
    print ('objects list ')
def newFile():
    print ('new file')

def fileOpen():
    print ('open file')
def about():
    
    print ('about the game engine')
################################################################
#initilise the GUI of tkinter
root = tk.Tk()
root.title("Game engine 3d")
buttonwin = tk.Frame(root,width = 200, height = 600)
buttonwin.columnconfigure(0, weight=1)
buttonwin.rowconfigure(0, weight=1)
#buttonwin.grid(column=0, row=0, sticky=(N, W, E, S))
buttonwin.pack(side = LEFT)
embed = tk.Frame(root, width = 800, height = 600) #creates embed frame for pygame window
embed.grid(columnspan = 600, rowspan = 400, row=0,column=4) # Adds grid

buttonwin.bind_all("<Key>",key)
embed.pack(side = LEFT,fill=Y) #packs window to the left
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'



###############################################################

if __name__ == '__main__':
   pass

 


# creating the menu for GUI
menu = Menu(root)
root.config(menu=menu)
# file menu option
filemenu = Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label = "New" , command=newFile)
filemenu.add_command(label = "Open" , command=fileOpen)
filemenu.add_command(label = "Create" , command=newObject)
filemenu.add_separator()
filemenu.add_command(label = "Import" , command=newObject)
filemenu.add_command(label = "Export" , command=newObject)
filemenu.add_separator()
filemenu.add_command(label = "Exit" , command=root.quit)
# create menu
createmenu = Menu(menu)
menu.add_cascade(label="Create", menu=createmenu)
createmenu.add_command(label="Cube", command=createCube)
createmenu.add_command(label="Cone", command=about)
createmenu.add_command(label="Cylinder", command=about)
createmenu.add_command(label="Sphere", command=about)
createmenu.add_command(label="Plane", command=createPlane)
createmenu.add_command(label="Circle", command=createCircle)
createmenu.add_command(label="Human", command=about)
createmenu.add_separator()
createmenu.add_command(label="Light", command=about)
createmenu.add_command(label="Spot light", command=about)
createmenu.add_command(label="Area light", command=about)
createmenu.add_separator()
createmenu.add_command(label="Camera", command=about)
# physics menu
physicsmenu = Menu(menu)
menu.add_cascade(label="Physics" ,menu = physicsmenu)
physicsmenu.add_command(label="Force", command=about)
physicsmenu.add_command(label="Torque", command=about)
# Genatic algorithms
GAmenu = Menu(menu)
menu.add_cascade(label="GA" ,menu = GAmenu)
GAmenu.add_command(label="Init Sequence", command=initGA)
GAmenu.add_command(label="Live", command=livePopulation)
# help menu option
helpmenu = Menu(menu)
menu.add_cascade(label="Help" ,menu = helpmenu)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Version", command=about)
helpmenu.add_command(label="Update", command=about)



def buttons():
    button_createCube = Button(buttonwin,text="Cube",relief=RIDGE,width=8,command=createCube)
    button_createCube.grid(row=0,column=0)
    button_createCube = Button(buttonwin,text="Sphere",relief=RIDGE,width=8,command=createCube)
    button_createCube.grid(row=0,column=1)
    button_createCube = Button(buttonwin,text="Cone",relief=RIDGE,width=8,command=createCube)
    button_createCube.grid(row=1,column=0)
    button_createCube = Button(buttonwin,text="Plane",relief=RIDGE,width=8,command=createPlane)
    button_createCube.grid(row=1,column=1)
    button_createCube = Button(buttonwin,text="Cylinder",relief=RIDGE,width=8,command=createCube)
    button_createCube.grid(row=2,column=0)
    button_createCube = Button(buttonwin,text="Circle",relief=RIDGE,width=8,command=createCircle)
    button_createCube.grid(row=2,column=1)
    button_createCube = Button(buttonwin,text="Human",relief=RIDGE,width=8,command=createCube)
    button_createCube.grid(row=3,column=0)
    button_createCube = Button(buttonwin,text="Ak47",relief=RIDGE,width=8,command=createCube)
    button_createCube.grid(row=3,column=1)
    # camera controlls
    button_createCube = Button(buttonwin,text="x",relief=SUNKEN,width=8,command=createCube)
    button_createCube.grid(row=5,column=0)
    button_createCube = Button(buttonwin,text="-x",relief=SUNKEN,width=8,command=createCube)
    button_createCube.grid(row=5,column=1)
    button_createCube = Button(buttonwin,text="y",relief=SUNKEN,width=8,command=createCube)
    button_createCube.grid(row=6,column=0)
    button_createCube = Button(buttonwin,text="-y",relief=SUNKEN,width=8,command=createCube)
    button_createCube.grid(row=6,column=1)
    button_createCube = Button(buttonwin,text="z",relief=SUNKEN,width=8,command=createCube)
    button_createCube.grid(row=7,column=0)
    button_createCube = Button(buttonwin,text="-z",relief=SUNKEN,width=8,command=createCube)
    button_createCube.grid(row=7,column=1)
    # physics controll

buttons()
if __name__ == '__main__':

   while True:
       main()
       root.update()
    #root.mainloop()
