import CellSpacerVisualizer as cellVisual
from Grid import Grid
import numpy as np
import math

import matplotlib.pyplot as plt
import matplotlib.animation as animation

xLength = 101
yLength = 101

yellowt_m = 0
greent_m = 0

yellowSVal = 0.2
greenSVal = 0.4

iterations = 5000

gridHistory = np.zeros((xLength, yLength, iterations))

initialYellowCells = [[(x + 45, 25), 1, yellowt_m, False, yellowSVal] for x in range(10)]

initialGreenCells = [[(x + 45, 75), 0.5, greent_m, False, greenSVal] for x in range(10)]

grid = Grid(xLength, yLength, initialYellowCells + initialGreenCells)

for t in range(iterations):
    color_matrix = cellVisual.computeMatrixFromGrid(grid)
    gridHistory[:, :, t] = color_matrix

    grid.tick(t)

fig, ax = plt.subplots()

displayMatrix = ax.matshow(gridHistory[:, :, 0])
ax.set_title(f"(Yellow S = {yellowSVal}, Green S = {greenSVal}) at Time = 0, Environment = 0")

def animate(t):
    environmentVal = grid.phi(t) % (2 * math.pi)
    environmentVal = round(environmentVal, 2)

    displayMatrix.set_array(gridHistory[:, :, t])
    ax.set_title(f"(Yellow S = {yellowSVal}, Green S = {greenSVal}) at Time = {t}, Environment = {environmentVal}")
    return [displayMatrix]

anim = animation.FuncAnimation(fig, func = animate, frames = iterations, interval = 30)

gifWriter = animation.PillowWriter(fps = 30)
anim.save("OutputGIFs/PeriodicEnvironmentalFluctuationsDotProductv1/ySVal02gSVal04ExtremelyLongVersion.gif", writer = gifWriter)

exit()