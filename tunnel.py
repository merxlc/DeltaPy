import time

link = {}

def init(vardict):
    global link
    link = vardict

class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.set_scripts()
        self.children = []
    def set_scripts(self):
        self.scripts = {}
    def add_node(self, nodetype, name):
        newnode = nodetype(name, self)
        self.children.append(newnode)
        self.__dict__[name] = newnode
    def add_script(self, script):
        newscript = script(self)
        self.scripts[script.__name__] = newscript
    def __getitem__(self, key):
        return self.scripts[key]
    def setup_all_sub(self):
        for node in self.children:
            node.setup_all_sub()
            for script in node.scripts.values():
                script.setup()
    def update_all_sub(self):
        for node in self.children:
            node.update_all_sub()
            for script in node.scripts.values():
                script.varupdate()
                script.update()

class Link:
    def __init__(self, source):
        self.source = source
    def evaluate(self):
        return self.source

class Script:
    def __init__(self, parent):
        self.parent = parent
        self.varlinks = {}
        self.start()
    def start(self):
        pass
    def setup(self):
        pass
    def varupdate(self):
        for key in self.varlinks:
            #print(self.varlinks[key].source)
            self.__dict__[key] = self.varlinks[key].evaluate()
        #print(self.varlinks)
    def update(self):
        pass
    def set_var(self, key, val):
        self.varlinks[key] = Link(val)
    def append_var(self, key, val):
        self.varlinks[key] = Link(self.__dict__[key] + [val])

root = Node('root', '')

def start():
    global root
    root.setup_all_sub()

    while True:
        root.update_all_sub()
