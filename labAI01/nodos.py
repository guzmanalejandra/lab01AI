class nodos:

    def __init__(self, position=None, visited=False, parent=None):
        self.position = position

        self.g = 1000000
        self.h = 1000000
        self.f = 1000000
        self.visited = visited
        self.parent = parent

    def setG(self, g):
        self.g = g

    def setH(self, h):
        self.h = h
    
    def setF(self):
        self.f = self.g + self.h

    def setVisited(self):
        self.visited = True

