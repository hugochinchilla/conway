from conway import World
import pytest


def test_cells_match():
    assert (1,1) == (1,1)

def test_a_world_with_1_cell_at_3_5():
    world = World()
    world.insert((3,5))
    assert (3,5) in world
    assert (1,1) not in world
    assert world.cells == 1

def test_a_world_with_2_cells():
    world = World()
    world.insert((1,5))
    world.insert((900,52))

    assert (1,5) in world
    assert (900,52) in world
    assert (1,1) not in world
    assert world.cells == 2


def test_single_cell_starves():
    world = World()
    world.insert((1,1))
    world.tick()
    assert (1,1) not in world


def test_two_neighbor_cells_starve():
    world = World()
    world.insert((1,1))
    world.insert((1,2))
    world.tick()
    assert (1,1) not in world
    assert (1,2) not in world

def est_3_neighbor_cells_one_survive():
    world = World()
    world.insert((1,1))
    world.insert((1,2))
    world.insert((1,3))
    world.tick()
    assert (1,1) not in world
    assert (1,2) in world
    assert (1,3) not in world


def test_neigbors_calculation():
    world = World()
    assert world.neighbors_of((1,1)) == [
        (0,0), (0,1), (0,2),
        (1,0),        (1,2),
        (2,0), (2,1), (2,2)]


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
