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
        self.COLOR = '#1B2A41'
        self.selected = False
        # store the id of the nodes
        self.pins = []
        
        self.entities = []

        self.shift = 25
        
        self.radius = 7
        self.setInputPin()
        self.setInputPin()
        self.setOutputPin()
        self.setInputPin()
        
        
    def countInputPins(self):
        cnt = 0
        for p in self.pins:
            if p._type_ == 'input':
                cnt+=1
        return cnt
    
    def countOutputPins(self):
        cnt = 0
        for p in self.pins:
            if p._type_ == 'output':
                cnt+=1
        return cnt
    
    def setInputPin(self):
        c = self.countInputPins()
        x = 0
        y = self.shift + self.shift*c
        p = Pin(c+1,'input',x,y)
        self.pins.append(p)
        
    def setOutputPin(self):
        c = self.countOutputPins()
        x = 0 +self.width
        y = self.shift + self.shift*c
        p = Pin(c+1,'output',x,y)
        self.pins.append(p)

    def setX(self,x):
        self.x =x
    
    def setY(self,y):
        self.y =y
    
    def setSelectedTrue(self):
        self.selected = True
    
    def setSelectedFalse(self):
        self.selected = False
    
    def isInsidePin(self,x,y):
        for pin in self.pins:
            print(pin.x+self.x,pin.y+self.y,"|",self.dist(x,y,pin.x,pin.y+self.y),'[',pin.selected,']')
            if self.dist(x,y,pin.x+self.x,pin.y+self.y) <= self.radius:
                pin.selected = True
                return True
        return False    

    def isInside(self,x,y):
        if x >self.x and x < (self.x+self.width):
            if y >self.y and y <(self.y+self.height):
                print ("yes")
                if self.isInsidePin(x,y):
                    return False
                return True
            else: 
                return False
        else:
            return False
    
    def isInsidePinOnly(self,x,y):
        for pin in self.pins:
            print(pin.x+self.x,pin.y+self.y,"|",self.dist(x,y,pin.x,pin.y+self.y),'[',pin.selected,']')
            if self.dist(x,y,pin.x+self.x,pin.y+self.y) <= self.radius:
                pin.selected = True
                return pin
        return False 
    
    def createConnection(self,x,y,nid,pid,spid,sptp):

        e = Edge()
        e.setConnection(nid,pid)
        for p in self.pins:
            if p._type_ == sptp:
                if p.id == spid:
                    p.connections.append(e)
                    print(">>Connection [ N",self.id,": P ",spid,"]=>[ N",nid,": P ",pid,"]")
        
    def isInsideOnly(self,x,y):
        if x >self.x and x < (self.x+self.width):
            if y >self.y and y <(self.y+self.height):
                return True
            else: 
                return False
        else: 
            return False
    def translate(self,dx,dy):
        self.x += dx
        self.y += dy
    def dist(self,x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2 +(y2-y1)**2)


class Pin(object):
    def __init__(self,_id_,_type_,x,y):
        self.x,self.y = x,y
        self.id = _id_
        # id of the node it connected to
        self.connections = []
        # connected or not
        self.state = -1 
        # input or output
        self._type_ = _type_
        self.selected = False

class Edge(object):
    def __init__(self):
        self.nodeId = -1
        self.pins = []
    def setConnection(self,nid,pid):
        self.nodeId = nid
        self.pins.append(pid)

'''
{
    "graph" : { 
        
        "a" : ["c"],
        "b" : ["c", "e"],
        "c" : ["a", "b", "d", "e"],
        "d" : ["c"],
        "e" : ["c", "b"],
        "f" : []
    },
    
    "nodes" : {
        "a" : {
            "id":456462,
            "title": "Palyer",
            "type": "player",
            "width":100,
            "height": 150,
            "x":200,
            "y":200,
            "color":"#454555",
            "pins":[
                {
                    "id":45,
                    "x":20,
                    "y":30,
                    "type":"input",
                    "connection":[]
                },
                {
                    "id":45,
                    "x":120,
                    "y":30,
                    "type":"output",
                    "connection":[
                        "a":[0,5],
                        "b":[3]
                    ]
                    
                }
            ],

        },
        "b" : {},
        "c" : {}

    }, 
    
}
'''

class Graph(object):
    def __init__(self):
        pass


class Entity():
    def __init__(self):
        self.Name = ""
        self.inputs = []
        self.outputs = []

    def entityFunction(self):
        pass


if __name__ == "__main__":
    n = Node(6)
    n.main()
