import pygame
import PyGine
from Cell import Cell
class quadtree :

    def __init__(self,x,y,dx,dy,tag = "") :
        self.tag = tag
        self.Region_NE = None
        self.Region_NO = None
        self.Region_SE = None
        self.Region_SO = None
        self.elements = []
        self.transform = PyGine.Transform()
        self.transform.position.x = x
        self.transform.position.y = y
        self.transform.scale.x = dx
        self.transform.scale.y = dy
        self.center = PyGine.Vector3(x + dx/2,y + dy/2)
        self.capacity = 5
        self.numElements = 0 
        self.divided = False
        self.maxDepth = 20
        self.DEBUG = False#True

    def clear(self) :
        self.elements = []
        if self.divided :
            self.Region_NE.clear()
            self.Region_NO.clear()
            self.Region_SE.clear()
            self.Region_SO.clear()
            self.Region_NE = None
            self.Region_NO = None
            self.Region_SE = None
            self.Region_SO = None
        self.numElements = 0
        self.divided = False



    def draw(self) :
        if self.divided and self.DEBUG :
            pygame.draw.line(PyGine.Game.game.surface,(255,255,255),(self.center.x,self.center.y),(self.center.x,self.center.y + self.transform.scale.y/2))
            pygame.draw.line(PyGine.Game.game.surface,(255,255,255),(self.center.x,self.center.y),(self.center.x + self.transform.scale.x/2,self.center.y))
            pygame.draw.line(PyGine.Game.game.surface,(255,255,255),(self.center.x,self.center.y),(self.center.x - self.transform.scale.x/2,self.center.y))
            pygame.draw.line(PyGine.Game.game.surface,(255,255,255),(self.center.x,self.center.y),(self.center.x ,self.center.y- self.transform.scale.y/2))
            
            self.Region_NE.draw()
            self.Region_NO.draw()
            self.Region_SE.draw()
            self.Region_SO.draw()
    
    def build(self) :

        self.divided = True
        self.Region_NE = quadtree(self.transform.position.x + self.transform.scale.x/2,self.transform.position.y,self.transform.scale.x/2,self.transform.scale.y/2,self.tag + " NE")
        self.Region_NO = quadtree(self.transform.position.x ,self.transform.position.y,self.transform.scale.x/2,self.transform.scale.y/2,self.tag + " NO")
        self.Region_SE = quadtree(self.transform.position.x + self.transform.scale.x/2,self.transform.position.y + self.transform.scale.y/2,self.transform.scale.x/2,self.transform.scale.y/2,self.tag + " SE") 
        self.Region_SO = quadtree(self.transform.position.x ,self.transform.position.y + self.transform.scale.y/2,self.transform.scale.x/2,self.transform.scale.y/2,self.tag + " SO")

    def getCollisionInfosOf(self,object : PyGine.GameObject) :

        collisionInfos = []

        if  not object.isIn(self) :
            return

        if self.divided:
            # Recursively check the object against each of the quadtree's sub-regions
            self.Region_NE.getCollisionInfosOf(object)
            self.Region_NO.getCollisionInfosOf(object)
            self.Region_SE.getCollisionInfosOf(object)
            self.Region_SO.getCollisionInfosOf(object)
        else:
            # Check the object against all of the elements in the quadtree
            for element in self.elements:
                if object != element and object.isInCollisionWith(element):
                    collisionInfos.append((object, element))
                    object.onCollision(element)       



    def addElement(self,object : PyGine.GameObject,depth=0) :
        res2 = object.isIn(self)
        if res2 :
            if self.numElements >= self.capacity and depth < self.maxDepth:

                if not self.divided : 
                    self.build()
                    
                    for element in self.elements :
                        self.Region_NE.addElement(element,depth+1)
                        self.Region_NO.addElement(element,depth+1)
                        self.Region_SE.addElement(element,depth+1)
                        self.Region_SO.addElement(element,depth+1)
                    
                    self.elements = []

                self.Region_NE.addElement(object,depth+1)
                self.Region_NO.addElement(object,depth+1)
                self.Region_SE.addElement(object,depth+1)
                self.Region_SO.addElement(object,depth+1)

            else :
                self.numElements += 1
                self.elements.append(object)

