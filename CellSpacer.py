import CellSpacerVisualizer as cellVisual
from Grid import Grid
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

xLength = 101
yLength = 101

defaultOmega = 5

iterations = 50

gridHistory = np.zeros((xLength, yLength, iterations))

grid = Grid(xLength, yLength, [
    [(50, 50), 0, 18, 1]
])

for t in range(iterations):
    color_matrix = cellVisual.computeMatrixFromGrid(grid)
    gridHistory[:, :, t] = color_matrix

    grid.tick()

fig, ax = plt.subplots()

displayMatrix = ax.matshow(gridHistory[:, :, 0])

def animate(t):
    displayMatrix = ax.matshow(gridHistory[:, :, t])
    return displayMatrix

anim = animation.FuncAnimation(fig, func = animate, frames = iterations, interval = 125)
plt.show()