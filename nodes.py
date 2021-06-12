from tunnel import *
from scripts import *

class Empty(Node):
    pass

class World(Node):
    def set_scripts(self):
        self.scripts = {}
        self.add_script(Counter)
        self.add_script(Printme)
        self['Printme'].set_var('counter', self['Counter'])
