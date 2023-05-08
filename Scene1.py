import PyGine
from GridManager import GridManager
from HUD import HUD1,HUD2,HUD3
class Scene1(PyGine.Scene) :
    def start(self) :
        print("Starting Game Scene")
        self.addGameObject(GridManager())
        self.addGameObject(HUD1())
        self.addGameObject(HUD2())
        self.addGameObject(HUD3())
