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


'''
==========================================
    camera class
==========================================
'''          
class camera:
    def __init__(self,pos=(0,0,0),rot=(0,0),center=(0,0,0)):
        self.pos = [pos[0],pos[1],pos[2]]  #The sphere's center
        self.rot = list(rot)   #The spherical coordinates' angles (degrees).
        self.radius = 3.0      #The sphere's radius
        self.center = list(center)
    def update(self,dt,key):
        s = dt*10
        if key == 'down': self.pos[2] -= s
        if key == 'up': self.pos[2] += s

        if key == 'front': self.pos[1] += s
        if key == 'back': self.pos[1] -= s

        if key == 'left': self.pos[0] -= s
        if key == 'right': self.pos[0] += s 
    def drag(self,dx,dy,dz):
        
        self.pos[2] += dz
        self.pos[1] += dy
        self.pos[0] += dx

    def rotateCam(self,dt,key,dtheta): 
         
        c1,s1 = math.cos(dtheta),math.sin(dtheta)
        c2,s2 = math.cos(-dtheta),math.sin(-dtheta)
        d = math.sqrt((self.pos.x**2)+(self.pos.y**2)+(self.pos.z**2))
        if key == 'x+': # horiontal x,z
                temp = self.pos[1]

                self.pos[1] =  d*c1 - d*s1
                self.pos[2] =  temp*s1 + d*c1
        if key == 'x-': # horizontal x,z
                temp = self.pos[1]
                self.pos[1] =  d*c2 - d*s2
                self.pos[2] =  temp*s2 + d*c2
        if key == 'y+': # virtical y,z
                temp = self.pos[0]
                self.pos[0] =  self.pos[0]*c1 - self.pos[2]*s1
                self.pos[2] =  temp*s1 + self.pos[2]*c1
        if key == 'y-': # virtical y,z
                temp = self.pos[0]
                self.pos[0] =  self.pos[0]*c2 - self.pos[2]*s2
                self.pos[2] =  temp*s2 + self.pos[2]*c2
    
    