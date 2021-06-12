from tunnel import *
from scripts import *

class Empty(Node):
    pass

class World(Node):
    def set_scripts(self):
        self.scripts = {}
        self.add_script(Map)

class Camera(Node):
    def set_scripts(self):
        self.scripts = {}
        self.add_script(CameraView)
        self.add_script(Transform)
    def setup(self):
        self.world = ""
