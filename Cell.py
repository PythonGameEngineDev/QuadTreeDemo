import random
import PyGine
class Cell(PyGine.GameObject) :

    def __init__(self, x, y,dx,dy,gm) :
        super().__init__()
        self.name = "cell" + str(x) +" " +str(y)
        self.gridManager = gm
        self.transform.position.x = x
        self.transform.position.y = y
        self.transform.scale.x = dx
        self.transform.scale.y = dy
        self.addComponent(PyGine.DrawRectComponent(self,(255,255,255)))
        
        self.points = [[x,y],[x+dx,y],[x,y+dy],[x+dx,y+dy]]

    def update(self,dt) :
        
        if self.transform.position.x < 0 :
            self.transform.position.x = 0
        if self.transform.position.x + self.transform.scale.x > 1000 :
            self.transform.position.x = 1000 - self.transform.scale.x
        if self.transform.position.y < 0 :
            self.transform.position.y = 0
        if self.transform.position.y + self.transform.scale.y > 600 :
            self.transform.position.y = 600 - self.transform.scale.y

        self.points = [[self.transform.position.x,self.transform.position.y],[self.transform.position.x+self.transform.scale.x,self.transform.position.y],[self.transform.position.x,self.transform.position.y+self.transform.scale.y],[self.transform.position.x+self.transform.scale.x,self.transform.position.y+self.transform.scale.y]]
        self.getComponent(PyGine.DrawRectComponent).color = (255,255,255)
        if PyGine.MouseListener.getPressed(2) :
            if self.transform.position.x < PyGine.MouseListener.getPos().x < self.transform.position.x + self.transform.scale.x and self.transform.position.y < PyGine.MouseListener.getPos().y < self.transform.position.y + self.transform.scale.y :
                self.destroy()
                if self in self.gridManager.cells :
                    self.gridManager.cells.remove(self)

        self.gridManager.quadtree.getCollisionInfosOf(self)

        #mouvement aléatoire
        self.transform.position.x += random.randint(-1,1)
        self.transform.position.y += random.randint(-1,1)
        
    def isInCollisionWith(self,cell) :
        #with the transform of both cell, we can check if they are in collision
        return self.transform.position.x < cell.transform.position.x + cell.transform.scale.x and self.transform.position.x + self.transform.scale.x > cell.transform.position.x and self.transform.position.y < cell.transform.position.y + cell.transform.scale.y and self.transform.position.y + self.transform.scale.y > cell.transform.position.y


    def isIn(self,tree) :
        for p in self.points : 
            if p[1] > tree.transform.position.y and p[1] < tree.transform.position.y + tree.transform.scale.y and p[0] > tree.transform.position.x and p[0] < tree.transform.position.x + tree.transform.scale.x :
                return True
        return False

    def onCollision(self, o):

        self.getComponent(PyGine.DrawRectComponent).color = (255,0,0)

    def hasAPointIn(self,tree ) :
        res = ""
        for p in self.points : 
            if p[1] > tree.center.y :
                res+= "S"
                if p[0] < tree.center.x :
                    res += "W"
                elif p[0] > tree.center.x :
                    res+= "E"
            elif p[1] < tree.center.y :
                res+= "N"
                if p[0] < tree.center.x :
                    res += "W"
                elif p[0] > tree.center.x :
                    res+= "E"
            res += " "
        
        return res
    
    def __str__(self) :
        return self.name