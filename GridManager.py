import random
import PyGine
from Cell import Cell
from quadtree import quadtree
class GridManager(PyGine.GameObject) :
    
    def __init__(self) :
        super().__init__()
        self.quadtree = quadtree(0,0,1000,600,"root ")
        self.cells = []
        self.updateCount = 0

    def start(self) :
        for i in range(100) :
            self.cells.append(PyGine.Game.game.instanciate(Cell( random.randint(0,940)  ,random.randint(0,540) ,100,100,self)))


    def update(self,dt) :
        self.updateCount += 1
        if PyGine.MouseListener.getClicked(0) :
            x : int = PyGine.MouseListener.getPos().x
            y : int = PyGine.MouseListener.getPos().y
            self.cells.append(PyGine.Game.game.instanciate(Cell( x ,y ,100,100,self)))
        
        if self.updateCount % 10 == 0 :
            self.quadtree = quadtree(0,0,1000,600," root" +str( self.updateCount))

            for cell in self.cells :
                self.quadtree.addElement(cell)

        self.quadtree.draw()


