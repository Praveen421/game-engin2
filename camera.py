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
    
    