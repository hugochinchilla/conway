from collections import defaultdict


class World(dict):
    def insert(self, cell):
        datadict = {cell: None}
        self.update(datadict)

    @property
    def cells(self):
        return len(self)

    def tick(self):
        counter = defaultdict(lambda: [])
        for cell in self.keys():
            counter[cell].extend(self.alive_neighbors(cell))
            counter[cell] = set(counter[cell])

        new_world = {}
        for cell in self.keys():
            count = len(counter[cell])
            if count >= 2:
                new_world[cell] = None

        for cell,nbrs in counter.items():
            if len(nbrs) >= 3:
                new_world[cell] = None

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


