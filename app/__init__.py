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



def load_plugins():
    global plugins_names
    plugins_dir_names = os.listdir(plugins_path)
    plugins_names = plugins_dir_names
    # debug message
    d.log("msg",plugins_names)

# def execute_plugins():
#     global plugins
#     cmd = ' python main.py'
#     for p in plugins:
#         plugin_main = os.listdir(plugins_path+p)
#         os.system('cd '+plugins_path+p)
#         os.system(cmd)
#         os.system(cmd)          # showConfig   addConfig
#         d.log("cmd",'cd '+plugins_path+p)

def execute_plugins():
    global plugins_names,plugins
        
    for p in plugins_names:
        PLUGIN_NAME = 'plugins.'+p+'.__init__'
        d.log("msg",PLUGIN_NAME)
        plugins.append(importlib.import_module(PLUGIN_NAME,'.'))
        temp = importlib.import_module(PLUGIN_NAME,'.')
        k = temp.Plugin("ju",key=67)
        modules = k.meta()
        for m in modules:
            print(importlib.import_module('plugins.'+p+'.'+m,'.'))


def main():
    global plugins
    load_plugins()
    execute_plugins()
    m = plugins[0].Plugin("hj",key=123)
    
### globals
d = debuger()
plugins_names = []
plugins = []

if __name__ == "__main__":
    main()