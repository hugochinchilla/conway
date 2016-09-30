
class World(object):

    def __init__(self, width, height):
        self.world = [[False]]
        #self.width = width
        #self.height = height
        #self.rows = []
        #for row in height:
        #    self.rows.append([False for x in range(0, width)])

    def pos(self, x, y):
        return self.world[x][y]
