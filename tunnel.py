import time

link = {}

def init(vardict):
    global link
    link = vardict

class Node:
    def __init__(self, name):
        self.name = name
        self.set_scripts()
        self.children = []
    def set_scripts(self):
        self.scripts = {}
    def add_node(self, nodetype, *params):
        newnode = nodetype(*params)
        self.children.append(newnode)
        self.__dict__[params[0]] = newnode
    def add_script(self, script):
        newscript = script()
        self.scripts[script.__name__] = newscript
    def __getitem__(self, key):
        return self.scripts[key]

class Link:
    def __init__(self, source):
        self.source = source
    def evaluate(self):
        return self.source

class Script:
    def __init__(self):
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

root = Node('root')

def start():
    global root
    running = root.children

    for node in running:
        for script in node.scripts.values():
            script.setup()

    while True:
        time.sleep(0.1)
        for node in running:
            for script in node.scripts.values():
                script.varupdate()
                script.update()
