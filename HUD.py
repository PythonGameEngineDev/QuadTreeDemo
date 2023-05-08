import PyGine
class HUD1(PyGine.Overlay) :
    def start(self):
        self.addComponent(PyGine.TextComponent(self,"P = play/pause",(0, 0, 0), 20))
        self.transform.position.y = 10

class HUD2(PyGine.Overlay) :
    def start(self):
        self.addComponent(PyGine.TextComponent(self,"E = erase",(0, 0, 0), 20))
        self.transform.position.y = 50

class HUD3(PyGine.Overlay) :
    def start(self):
        self.addComponent(PyGine.TextComponent(self,"mouseClicks = erase/draw tile",(0, 0, 0), 20))
        self.transform.position.y = 90

