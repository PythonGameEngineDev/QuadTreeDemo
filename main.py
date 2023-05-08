import PyGine
from Scene1 import Scene1 
class game(PyGine.Game) :

    def __init__(self):
        super().__init__(1000,600,self)
        self.addScene(Scene1())
        self.setScene(1)
        self.fps= 60
        self.setBgColor((0,20,0))
    
    def update(self) :
        #convert delta time between frame to frame per seconds
        self.s = 1000 / self.dt
        self.setCaption("FPS: " + str(self.s) )

g =  game()
g.game.run()