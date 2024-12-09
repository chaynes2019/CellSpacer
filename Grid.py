import itertools as iterT
from Space import Space
from Cell import Cell
import math
import random
import numpy as np

homeostaticRateFactor = 0.1
stochasticDecreaseRate = 0.1

randomSeed = 1

random.seed(randomSeed)
rng = np.random.default_rng(randomSeed)

class Grid():
    def __init__(self, xLength, yLength, initiallyOccupiedSpaces, environment_, yellowSValue, greenSValue):
        self.dimensions = (xLength, yLength)

        if (xLength < 1 or yLength < 1):
            raise ValueError("The dimensions of the grid must be positive")

        self.spaces = dict()

        self.initializeEmptyGrid()

        self.initializeOccupiedSpaces(initiallyOccupiedSpaces)

        self.cells = set()

        self.getYellowGreenPopSizes()

        self.phiVal = 0

        self.yellowSVal = yellowSValue

        self.greenSVal = greenSValue

        self.environment = environment_

    def phi(self, t):
        if self.environment == "periodic":
            T = 100

            return 2 * math.pi * t / T
        #return 0
        
        elif self.environment == "random":
            #Random Environment
            
            return random.uniform(0, 2 * math.pi)
        
        
        elif self.environment == "quasibrownian":
            #QuasiBrownian Environment
            return self.phiVal + rng.normal(0, 0.25)

        '''if t >= 250:
            return 0.5 * 2 * math.pi
        else:
            return 0'''

    def dPhidt(self, phi):
        return homeostaticRateFactor * (2 * math.pi - phi)

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
    
    '''
    def refreshCellPopulation(self):
        self.cells = set()

        xLength = self.dimensions[0]
        yLength = self.dimensions[1]

        for x, y in iterT.product(range(xLength), range(yLength)):
            cell = self.spaces[(x, y)].getOccupant()
            if cell != None:
                self.cells.add(cell)
    '''
    
    def getYellowGreenPopSizes(self):
        self.cells = set()

        yellowProliferators = set()
        yellowQuiescent = set()
        greenProliferators = set()
        greenQuiescent = set()

        xLength = self.dimensions[0]
        yLength = self.dimensions[1]

        for x, y in iterT.product(range(xLength), range(yLength)):
            cell = self.spaces[(x, y)].getOccupant()
            if cell != None:
                self.cells.add(cell)
                if cell.color == 1:
                    if cell.quiescent:
                        yellowQuiescent.add(cell)
                    else:
                        yellowProliferators.add(cell)
                elif cell.color == 0.5:
                    if cell.quiescent:
                        greenQuiescent.add(cell)
                    else:
                        greenProliferators.add(cell)
                else:
                    raise(ValueError("There is a non-empty cell with illegal color"))
                
        return (len(yellowProliferators),
                len(yellowQuiescent),
                len(greenProliferators),
                len(greenQuiescent))

    def tick(self, t):
        #By running the below method, self.cells is refreshed
        self.getYellowGreenPopSizes()

        #print(len(self.cells))

        self.phiVal = self.phi(t)

        for cell in self.cells:
            cell.tick(self.phiVal, [self.yellowSVal, self.greenSVal])