import CellSpacerVisualizer as cellVisual
from Grid import Grid
import numpy as np
import math
import itertools

import matplotlib.pyplot as plt
import matplotlib.animation as animation

xLength = 101
yLength = 101

yellowt_m = 0
greent_m = 0

yellowSVal = 0.2
greenSVal = 0.4

iterations = 500

gridHistory = np.zeros((xLength, yLength, iterations))

initialYellowCells = [[(x, y), 1, yellowt_m, False, yellowSVal] for x, y in itertools.product(range(xLength), range(yLength)) if (x, y) != (0, 0) and x >= 50]

initialGreenCells = [[(x, y), 0.5, greent_m, False, greenSVal] for x, y in itertools.product(range(xLength), range(yLength)) if (x, y) != (0, 0) and x < 50]


grid = Grid(xLength, yLength, initialYellowCells + initialGreenCells)

for t in range(iterations):
    color_matrix = cellVisual.computeMatrixFromGrid(grid)
    gridHistory[:, :, t] = color_matrix

    grid.tick(t)

fig, ax = plt.subplots()

displayMatrix = ax.matshow(gridHistory[:, :, 0])
ax.set_title(f"(Time = 0, Environment = 0")

def animate(t):
    environmentVal = grid.phi(t) % (2 * math.pi)
    environmentVal = round(environmentVal, 2)

    displayMatrix.set_array(gridHistory[:, :, t])
    ax.set_title(f"(Time = {t}, Environment = {environmentVal}")
    return [displayMatrix]

anim = animation.FuncAnimation(fig, func = animate, frames = iterations, interval = 30)

gifWriter = animation.PillowWriter(fps = 60)
anim.save("OutputGIFs/homogeneousTissueUnderStochasticFluctuation/twoEvenPops.gif", writer = gifWriter)

exit()