# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:18:16 2020

@author: umut.kapucu
"""

import matplotlib.pyplot as plt
# %matplotlib inline  



class Circle(object):
    
    def __init__(self, radius, color):
        self.radius=radius
        self.color=color
        
    def add_r(self,r):
        self.radius=self.radius+r
        return(self.radius)
    
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  
    

class Rectangle(object):
    
    def __init__(self, width, height, color):
        self.width=width
        self.height=height
        self.color=color
        
    def add_h(self,h):
        self.height=self.height+h
        return(self.height)
    
    def add_w(self,w):
        self.width=self.width+w
        return(self.width)   

    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()


myCircle=Circle(5, 'red')

print('My circle has a radius:',myCircle.radius,'and it is', myCircle.color)
print('Here is my circle:')
myCircle.drawCircle()

myCircle.add_r(3)

print('My circle has a radius:',myCircle.radius,'and it is', myCircle.color)
print('Here is my circle:')
myCircle.drawCircle()


myRectangle=Rectangle(5, 6, 'blue')

print('My rectangle has a width:',myRectangle.width,'\n and a height:', myRectangle.height,'\n and it is', myRectangle.color)
print('Here is my rectangle:')
myRectangle.drawRectangle()

myRectangle.add_w(3)

print('My rectangle has a width:',myRectangle.width,'\n and a height:', myRectangle.height,'\n and it is', myRectangle.color)
print('Here is my rectangle:')
myRectangle.drawRectangle()
