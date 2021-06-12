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
