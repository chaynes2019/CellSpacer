import CellSpacerVisualizer as cellVisual
from Grid import Grid
import numpy as np
import itertools

import matplotlib.pyplot as plt
import matplotlib.animation as animation

xLength = 101
yLength = 101

defaultMu = 0
defaultOmega = 85

iterations = 210

gridHistory = np.zeros((xLength, yLength, iterations))

initialCondition = [[(x, y), defaultMu, 0, defaultOmega, 1] for x, y in itertools.product(range(xLength), range(yLength)) if (x, y) != (50, 50)]
initialCondition.append([(50, 50), defaultMu, 0, defaultOmega, 0.5])

grid = Grid(xLength, yLength, initialCondition)

for t in range(iterations):
    color_matrix = cellVisual.computeMatrixFromGrid(grid)
    gridHistory[:, :, t] = color_matrix

    grid.tick()

fig, ax = plt.subplots()

displayMatrix = ax.matshow(gridHistory[:, :, 0])
ax.set_title(f"Labeled Single Cell: mu = {defaultMu}, omega = {defaultOmega}")
ax.set_xlabel("x")
ax.set_ylabel("y")

def animate(t):
    displayMatrix.set_array(gridHistory[:, :, t])
    return [displayMatrix]

anim = animation.FuncAnimation(fig, func = animate, frames = iterations, interval = 30)
#plt.show()


mpegWriter = animation.FFMpegWriter(fps = 30)

anim.save("labeledSingleCellHomeostaticTissueGrowth.mp4", writer = mpegWriter)

gifWriter = animation.PillowWriter(fps = 30)
anim.save("labeledSingleCellHomeostaticTissueGrowth.gif", writer = gifWriter)

exit()