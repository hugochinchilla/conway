from collections import defaultdict


class World():
    def __init__(self):
        self._cells = set()

    def __iter__(self):
        yield from self._cells

    def __repr__(self):
        return repr(self._cells)

    def __has__(self, cell):
        return cell in self._cells

    def insert(self, cell):
        self._cells.add(cell)

    @property
    def size(self):
        return len(self._cells)

    def tick(self):
        counter = defaultdict(lambda: [])
        for cell in self._cells:
            for nbr in self.neighbors_of(cell):
                if nbr not in counter:
                    counter[nbr].extend(self.alive_neighbors(nbr))
                    counter[nbr] = set(counter[nbr])

        new_world = set()
        for cell, nbrs in counter.items():
            if cell in self and  1 < len(nbrs) < 4:
                new_world.add(cell)

        for cell, nbrs in counter.items():
            if cell not in self._cells and len(nbrs) == 3:
                new_world.add(cell)

        self._cells = new_world

    def alive_neighbors(self, cell):
        alive = set()
        for cell in self.neighbors_of(cell):
            if cell in self:
                alive.add(cell)

        return alive

    def neighbors_of(self, cell):
        rows = set()
        for x in range(-1,2):
            for y in range(-1,2):
                if (x,y) != (0,0):
                    i,j = cell
                    rows.add((i+x, j+y))
        return rows
