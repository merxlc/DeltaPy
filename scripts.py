from tunnel import *

class Counter(Script):
    def start(self):
        self.i = 0
    def update(self):
        self.i += 1

class Printme(Script):
    def update(self):
        print(self.counter.i)
