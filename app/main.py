from paths import *
import os
import importlib
from debuger import *
#import tkinter as tk
#from tkinter import ttk
##import views.view_node_editor as view
#from views.test2 import *
import wx

try:
    import views.view_main as view
except ImportError as error:
	# Output expected ImportErrors.
	print(error.__class__.__name__ + ": " + error.message)
	view = importlib.import_module('views.view_main', '.')
except Exception as exception:
	# Output unexpected Exceptions.
	print(exception, False)
	print(exception.__class__.__name__ + ": " + exception.message)
	view = importlib.import_module('views.view_main', '.')


def part(str, side):
    # split the tring by '.'
    name, ext = str.split('.')

    if side == 1:
        return name
    else:
        return ext


def load_lib():
    global libs, lib_names
    names = os.listdir(libs_path)
    for l in names:
        if l != '__pycache__':
            if part(l, 0) == 'py':
                LIB_NAME = 'lib.'+part(l, 1)
                # d.log('LIBS',LIB_NAME)
                lib_names.append(part(l, 1))
                # loading the libs
                libs.append(importlib.import_module(LIB_NAME, '.'))

    # debug message
    d.log("Loader", lib_names)


def find_module(str):
    global lib_names, libs

    k = [i for i in range(len(lib_names)) if lib_names[i] == str]
    return libs[k[0]]


def create_new_project():
    # start the new project window
    newDialog = importlib.import_module('dialog_new_project', '.')
    newDialogObject = newDialog.Project()
    newDialogObject.startWindow()


#######################################################
### globals
#######################################################
d = debuger()
lib_names = list()
libs = list()


def main():
    load_lib()

    designer = libs[1].Designer(find_module('layer'),
<<<<<<< HEAD
            find_module('camera'),
            find_module('pointer'),
            find_module('rect'),
            find_module('tile'),path=path)
    designer.main()
    #create_new_project()
=======
                                find_module('camera'),
                                find_module('pointer'),
                                find_module('rect'),
                                find_module('tile'), path=path)
>>>>>>> test

    # designer.main()
    # create_new_project()

    app = wx.App()
    view.MainWindow(None, "Node Editor", find_module('node'), designer)
    app.MainLoop()


if __name__ == "__main__":
<<<<<<< HEAD
        main()
=======
	main()
>>>>>>> test
