import itertools as iter
import numpy as np
import matplotlib.pyplot as plt

from Grid import Grid

def computeMatrixFromGrid(grid):
    xLength = grid.dimensions[0]
    yLength = grid.dimensions[1]

    colorMatrix = np.zeros((xLength, yLength))

    for x, y in iter.product(range(xLength), range(yLength)):
        space = grid.spaces[(x, y)]

        if space.getOccupant() != None:
            colorMatrix[x, y] = space.getOccupant().getColor()

    return colorMatrix

def visualizeMatrix(colorMatrix):
    plt.matshow(colorMatrix)

    plt.show()


grid = Grid(7, 7, [
    [(3, 3), 1, 0, False, 0.4]
])

'''
color_matrix = computeMatrixFromGrid(grid)
visualizeMatrix(color_matrix)

grid.tick(0)

color_matrix = computeMatrixFromGrid(grid)
visualizeMatrix(color_matrix)


grid.spaces[(3, 3)].getOccupant().apoptote()
print(grid.spaces[(3, 3)].getOccupant())

color_matrix = computeMatrixFromGrid(grid)
visualizeMatrix(color_matrix)


grid.tick(1)

color_matrix = computeMatrixFromGrid(grid)
visualizeMatrix(color_matrix)
'''