from nodes import *
from scripts import *
from tunnel import *

class Counter(Script):
    def start(self):
        self.i = 0
    def update(self):
        self.i += 1

class Printme(Script):
    def update(self):
        print(self.counter.i)

root.add_node(Empty, 'base')

root.base.add_script(Printme)
root.base.add_script(Counter)

root.base['Printme'].set_var('counter', root.base['Counter'])

start()
