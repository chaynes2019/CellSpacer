import itertools as iterT
from Space import Space
from Cell import Cell

class Grid():
    def __init__(self, xLength, yLength, initiallyOccupiedSpaces):
        self.dimensions = (xLength, yLength)

        if (xLength < 1 or yLength < 1):
            raise ValueError("The dimensions of the grid must be positive")

        self.spaces = dict()

        self.initializeEmptyGrid()

        self.initializeOccupiedSpaces(initiallyOccupiedSpaces)

        self.cells = []

        self.refreshCellPopulation()


    def initializeEmptyGrid(self):
        for x, y in iterT.product(range(self.dimensions[0]),
                                  range(self.dimensions[1])):
            self.spaces[(x, y)] = Space(self, x, y, None)


    def initializeOccupiedSpaces(self, initFilledSpaces):
        for spaceInfo in initFilledSpaces:
            x = spaceInfo[0][0]
            y = spaceInfo[0][1]

            num_divisions = spaceInfo[1]
            etaVal = spaceInfo[2]
            omegaVal = spaceInfo[3]

            colorVal = spaceInfo[4]

            phiMVal = spaceInfo[5]

            quiescenceVal = spaceInfo[6]

            fillingSpace = self.spaces[(x, y)]
            fillingSpace.setOccupant(Cell(fillingSpace,
                                          num_divisions,
                                          etaVal,
                                          omegaVal,
                                          colorVal,
                                          phiMVal,
                                          quiescenceVal))

    def getVonNeumannNeighbors(self, x, y):
        xLength = self.dimensions[0]
        yLength = self.dimensions[1]

        #Use of remainder creates periodic boundary conditions

        upperNeighbor = self.spaces[(x % xLength,
                                     (y + 1) % yLength)]
        lowerNeighbor = self.spaces[(x % xLength,
                                    (y - 1) % yLength)]
        leftNeighbor = self.spaces[((x - 1) % xLength,
                                     y % yLength)]
        rightNeighbor = self.spaces[((x + 1) % xLength,
                                     y % yLength)]

        neighbors = set([upperNeighbor,
                         lowerNeighbor,
                         leftNeighbor,
                         rightNeighbor])
        
        return neighbors

    def getMooreNeighbors(self, x, y):
        xLength = self.dimensions[0]
        yLength = self.dimensions[1]

        #Use of remainder creates periodic boundary conditions

        upperNeighbor = self.spaces[(x % xLength,
                                     (y + 1) % yLength)]
        lowerNeighbor = self.spaces[(x % xLength,
                                    (y - 1) % yLength)]
        leftNeighbor = self.spaces[((x - 1) % xLength,
                                     y % yLength)]
        rightNeighbor = self.spaces[((x + 1) % xLength,
                                     y % yLength)]
        
        upperLeftNeighbor = self.spaces[((x - 1) % xLength,
                                         (y + 1) % yLength)]
        
        upperRightNeighbor = self.spaces[((x + 1) % xLength,
                                         (y + 1) % yLength)]
        
        lowerRightNeighbor = self.spaces[((x + 1) % xLength,
                                         (y - 1) % yLength)]
        
        lowerLeftNeighbor = self.spaces[((x - 1) % xLength,
                                         (y - 1) % yLength)]

        neighbors = set([upperNeighbor,
                         lowerNeighbor,
                         leftNeighbor,
                         rightNeighbor,
                         upperLeftNeighbor,
                         upperRightNeighbor,
                         lowerRightNeighbor,
                         lowerLeftNeighbor])
        
        return neighbors
    
    def refreshCellPopulation(self):
        self.cells = []

        xLength = self.dimensions[0]
        yLength = self.dimensions[1]

        for x, y in iterT.product(range(xLength), range(yLength)):
            cell = self.spaces[(x, y)].getOccupant()
            if cell != None:
                self.cells.append(cell)

    def tick(self):
        self.refreshCellPopulation()

        print(len(self.cells))

        for cell in self.cells:
            cell.tick()