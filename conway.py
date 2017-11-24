from collections import defaultdict


class World(dict):
    def insert(self, cell):
        self.update({cell: None})

    @property
    def cells(self):
        return len(self)

    def __iter__(self):
        yield from self.keys()

    def __repr__(self):
        return repr(self.keys())

    def tick(self):
        counter = defaultdict(lambda: [])
        for cell in self.keys():
            for nbr in self.neighbors_of(cell):
                if nbr not in counter:
                    counter[nbr].extend(self.alive_neighbors(nbr))
                    counter[nbr] = set(counter[nbr])

        new_world = {}
        for cell in self.keys():
            count = len(counter[cell])
            if count >= 2:
                new_world[cell] = None

        for cell,nbrs in counter.items():
            if len(nbrs) >= 3:
                new_world[cell] = None

        print(self)
        print(new_world.keys())
        self.clear()
        self.update(new_world)


    def alive_neighbors(self, cell):
        alive = []
        for cell in self.neighbors_of(cell):
            if cell in self:
                alive.append(cell)

        return alive

    def neighbors_of(self, cell):
        rows = []
        for x in range(-1,2):
            for y in range(-1,2):
                if (x,y) != (0,0):
                    i,j = cell
                    rows.append((i+x, j+y))
        return rows


