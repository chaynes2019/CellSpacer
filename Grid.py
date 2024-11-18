import itertools as iterT
from Space import Space
from Cell import Cell
import math

class Grid():
    def __init__(self, xLength, yLength, initiallyOccupiedSpaces):
        self.dimensions = (xLength, yLength)

        if (xLength < 1 or yLength < 1):
            raise ValueError("The dimensions of the grid must be positive")

        self.spaces = dict()

        self.initializeEmptyGrid()

        self.initializeOccupiedSpaces(initiallyOccupiedSpaces)

        self.cells = set()

        self.refreshCellPopulation()

    def phi(self, t):
        T = 100

        return 2 * math.pi * t / T
        '''if t >= 250:
            return 0.5 * 2 * math.pi
        else:
            return 0'''

    def initializeEmptyGrid(self):
        for x, y in iterT.product(range(self.dimensions[0]),
                                  range(self.dimensions[1])):
            self.spaces[(x, y)] = Space(self, x, y, None)


    def initializeOccupiedSpaces(self, initFilledSpaces):
        for spaceInfo in initFilledSpaces:
            x = spaceInfo[0][0]
            y = spaceInfo[0][1]

            colorVal = spaceInfo[1]

            tMFracVal = spaceInfo[2]

            quiescenceVal = spaceInfo[3]

            sVal = spaceInfo[4]

            fillingSpace = self.spaces[(x, y)]
            fillingSpace.setOccupant(Cell(fillingSpace,
                                          colorVal,
                                          tMFracVal,
                                          quiescenceVal,
                                          sVal))

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
        self.cells = set()

        xLength = self.dimensions[0]
        yLength = self.dimensions[1]

        for x, y in iterT.product(range(xLength), range(yLength)):
            cell = self.spaces[(x, y)].getOccupant()
            if cell != None:
                self.cells.add(cell)

    def tick(self, t):
        self.refreshCellPopulation()

        print(len(self.cells))

        phiVal = self.phi(t)

        for cell in self.cells:
            cell.tick(phiVal)