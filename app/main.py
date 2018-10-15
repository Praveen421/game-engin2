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
import views.view_main as view


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

    app = view.UI(find_module('node'))
    app.top_menu()
    app.create_node_editor()
    app.customLoop()
    app.run()

if __name__ == "__main__":
        main()