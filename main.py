from nodes import *
from scripts import *
from tunnel import *

#init(globals())

#root.add_node(Empty, 'base')

#root.base.add_script(Printme)
#root.base.add_script(Counter)

#root.base['Printme'].set_var('counter', root.base['Counter'])

root.add_node(World, 'world')
root.add_node(Square, 'player')

root.world['Map'].set_var('objects', root.world['Map'].objects + [])

root.world.add_node(Camera, 'main_camera')

start()
