
### meta data

author      = "siddhartha"
<<<<<<< HEAD
name        = 'game Tester'
=======
name        = 'level designer'
>>>>>>> e55b006a9d516228913e7a1dd3603a2f04366ea2
version     = '1.0.1'
main        = 'main.py'

load_sequence =[]

class Plugin:
    def __init__(self,*args,**kwargs):
        print('Level designer :',args,kwargs)
    def run(self):
        print("run")
    def meta(self):
        return load_sequence
<<<<<<< HEAD
=======

>>>>>>> e55b006a9d516228913e7a1dd3603a2f04366ea2
