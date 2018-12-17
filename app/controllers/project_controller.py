
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
import os,time,random,math

import importlib

class Project():
        
        def __init__(self,*args,**kwargs):
                pass
                self.paths =  importlib.import_module('paths','.')
        
        def createNewProject(self,name,oriantation):
                os.chdir(self.paths.projects_path)
                # Create target Directory if don't exist
                if not os.path.exists(name):
                        os.mkdir(name)
                        print("Directory " , name ,  " Created ")
                else:    
                        print("Directory " , name ,  " already exists")
        
        def openProject(self,name):
                pass
        
        def removeProject(self,name):
                pass
        
        def claseProject(self,name):
                pass
        
        def saveProject(self,name):
                pass
        
        def recentProjects(self):
                pass
