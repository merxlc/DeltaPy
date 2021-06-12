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
