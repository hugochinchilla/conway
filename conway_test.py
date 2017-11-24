from conway import World
import pytest


def test_neigbors_calculation():
    world = World()
    assert world.neighbors_of((1,1)) == [
        (0,0), (0,1), (0,2),
        (1,0),        (1,2),
        (2,0), (2,1), (2,2)]

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
    """
    in:  [XX]
    out: [  ]
    """
    world = World()
    world.insert((0,0))
    world.insert((0,1))
    world.tick()
    assert world.cells == 0

def test_empty_cell_with_3_neighbors_becomes_populated():
    """
    in:  [XX]
         [X·]

    out: [XX]
         [XX]
    """
    world = World()
    world.insert((0,0))
    world.insert((0,1))
    world.insert((1,0))
    world.tick()
    assert world.cells == 4


def test_3_inline_cells():
    """
    tree cells meke one survive:

    in:  [···]
         [XXX]
         [···]

    out: [·X·]
         [·X·]
         [·X·]
    """
    world = World()
    world.insert((1,0))
    world.insert((1,1))
    world.insert((1,2))
    world.tick()
    assert world.cells == 3
    assert (0,1) in world
    assert (1,1) in world
    assert (2,1) in world

def test_3_inline_horzontal_cells_become_3_vertical_cells():
    """
    in:  [···]
         [XXX]
         [···]

    out: [·X·]
         [·X·]
         [·X·]
    """
    world = World()
    world.insert((1,0))
    world.insert((1,1))
    world.insert((1,2))
    world.tick()
    assert world.cells == 3
    assert (0,1) in world
    assert (1,1) in world
    assert (2,1) in world

def est_cell_dies_from_overpopulation():
    """
    in:  [·X·]
         [XXX]
         [·X·]

    out: [XXX]
         [X·X]
         [XXX]
    """
    world = World()
    world.insert((0,1))
    world.insert((1,0))
    world.insert((1,1))
    world.insert((1,2))
    world.insert((2,1))
    world.tick()
    for cell in world.keys():
        print(cell)
    assert world.cells == 8
