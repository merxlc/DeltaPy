# DeltaPy

Python game engine

Quick start:

import necessary modules:

```
from nodes import *
from scripts import *
from tunnel import *
```

(Optional) pass `globals()` into `init`. This will allow the engine to interface with your variables directly.

```
init(globals())
```

After adding all your nodes and scripts, run `start()`. This will start execution.

```
start()
```

# Nodes and scripts

Between your `init` and `start`, you can initialise nodes and scripts. The engine provides a base node, `root`, which all your nodes should be children of. To do this, you can use the `add_node` function:

```
root.add_node([node class], [node name])
```

Once you've added your node, you can access it with `root.[node name]`. You can also add scripts to it with:

```
root.[node name].add_script([script class])
```

This will add the script to the node and run it every frame.

You can also make nodes children of other nodes:

```
root.[base node name].add_node([node class], [child node name])
```

This node can then also be accessed with:

```
root.[base node name].[child node name]
```

# Sharing variables

you can share variables between scripts/nodes by linking them. this can be done with the `set_var` function:

```
root.{node 1 name}[{script name}].set_var({variable name}, {variable source})
```

# Example program

The above techniques are used in this example program, which will keep track of a counter called i, increment it every frame, and print it every frame:

```
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
```
