from conway import World

#Each cell with one or no neighbors dies, as if by solitude.
#Each cell with four or more neighbors dies, as if by overpopulation.
#Each cell with two or three neighbors survives.

def test_create_world_given_1_1():
  world = World(1,1)
  assert world.pos(0,0) == False

# single cell starves
#[X] [ ]
#def test_single_cell_starves():
#  world = World(1,1)
#  world.populate(1,1)
#  world.tick()
#  assert world[0][0] = False


# two cells starve to death
#[XX] []

# tree cells meke one survive
#[XXX] [ X ]

# empty cells with 3 neighbors becomes populated
#[X  ] [   ]
#[   ] [ X ]
#[X X] [   ]

# a cell with 4 or more neightbors dies from overpopulation
#[X X] [   ]
#[ X ] [   ]
#[X X] [   ]
