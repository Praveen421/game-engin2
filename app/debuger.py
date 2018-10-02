import os


class debuger(object):
    def __init__(self):
        # enable or disable the debuger 
        self.debug = True
    def log(self,tag,args):
        if self.debug == True:
            print(tag,":",args)


