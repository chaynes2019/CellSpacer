class Space():
    def __init__(self, containingGrid, x, y, initialOccupant):
        self.grid = containingGrid
        self.x = x
        self.y = y
        self.occupant = initialOccupant

    def setOccupant(self, cell):
        self.occupant = cell

    def getOccupant(self):
        return self.occupant

    def getNeighbors(self):
        #Von Neumann neighborhood setup
        return self.grid.getVonNeumannNeighbors(self.x, self.y)

        #Moore neighborhood setup
        return self.grid.getMooreNeighbors(self.x, self.y)

    def getOpenNeighbors(self):
        openNeighbors = []
        
        for neighbor in self.getNeighbors():
            if neighbor.getOccupant() == None:
                openNeighbors.append(neighbor)
        
        return set(openNeighbors)