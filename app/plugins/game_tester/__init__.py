


### meta data

author      = "siddhartha"
name        = 'game Tester'
version     = '1.0.1'
main        = 'main.py'

load_sequence =[]

class Plugin:
    def __init__(self,*args,**kwargs):
        print('Game Tester :',args,kwargs)
    def run(self):
        print("run")
    def meta(self):
        return load_sequence
