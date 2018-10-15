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
from PIL import Image
import math,time,os
import importlib



class Node():
    def __init__(self,*args,**kwargs):
        
        self.id = 0
        self.title =args[0]
        self.x = args[1]
        self.y = args[2]
        self.width = args[3]
        self.height = args[4]

        self.AUTO_ADGUST = True
        self.COLOR = (100,100,100)

        # store the id of the nodes
        self.input_pins = []
        self.output_pins = []

        self.entities = []
    
    def set_input_pin(self,id):
        self.input_pins.append(id)
    
    def set_output_pin(self,id):
        self.output_pins.append(id)
    
    def main(self):
        pass


class Entity():
    def __init__(self):
        self.Name = ""
        self.inputs = []
        self.outputs = []

    def entity_function(self):
        pass


if __name__ == "__main__":
    n = Node(6)
    n.main()
