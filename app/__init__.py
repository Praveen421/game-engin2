
from paths import *
import os
from debuger import *
from plugins.level_designer import main
d = debuger()

plugins = []



def load_plugins():
    global plugins
    plugins_dir_names = os.listdir(plugins_path)
    plugins = plugins_dir_names
    
    d.log("msg",plugins)
# def execute_plugins():
#     global plugins
#     cmd = ' python main.py'
#     for p in plugins:
#         plugin_main = os.listdir(plugins_path+p)
#         os.system('cd '+plugins_path+p)
#         os.system(cmd)
#         os.system(cmd)
#         d.log("cmd",'cd '+plugins_path+p)

def main():
    load_plugins()
    execute_plugins()
    

if __name__ == "__main__":
    main()