

<<<<<<< HEAD


=======
import importlib,os
>>>>>>> e55b006a9d516228913e7a1dd3603a2f04366ea2


class Plugin:
    def __init__(self,*args,**kwargs):
        print('Game Tester :',args,kwargs)
    def run(self):
        print("run")

# importing the Layer module
try:
    Layer_module = importlib.import_module('.layer','main')
except ImportError:
    print("\n[ok]: I don't know how to - ")
