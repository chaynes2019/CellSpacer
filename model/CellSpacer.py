import CellSpacerVisualizer as cellVisual
from Grid import Grid
from Cell import Cell
import numpy as np
import itertools

import matplotlib.pyplot as plt
import matplotlib.animation as animation

xLength = 101
yLength = 101

defaultMu = 0
defaultOmega = 85

iterations = 420

gridHistory = np.zeros((xLength, yLength, iterations))

initialCondition = [[(x, y), defaultMu, 0, defaultOmega, 0, 1] for x, y in itertools.product(range(xLength), range(yLength)) if (x, y) != (50, 50) and (x, y) != (0, 0)]
initialCondition.append([(50, 50), -1, 0, defaultOmega, 1, 0.5])

grid = Grid(xLength, yLength, initialCondition)

for t in range(iterations):
    color_matrix = cellVisual.computeMatrixFromGrid(grid)
    gridHistory[:, :, t] = color_matrix

    if t == 30:
        grid.treatWithTelomeraseInhibitor()

    if t == 210:
        cell_to_mutate = Cell(grid.spaces[(50, 50)],
                              -1,
                              0,
                              defaultOmega,
                              1,
                              0.75)
        
        grid.spaces[(50, 50)].setOccupant(cell_to_mutate)

    grid.tick()

fig, ax = plt.subplots()

displayMatrix = ax.matshow(gridHistory[:, :, 0])
ax.set_title(f"Cancer treated at t = 30 out of 420: mu = {-1}, omega = {defaultOmega}, t = 0")
ax.set_xlabel("x")
ax.set_ylabel("y")

def animate(t):
    displayMatrix.set_array(gridHistory[:, :, t])
    ax.set_title(f"Cancer treated at t = 30 out of 420: mu = {-1}, omega = {defaultOmega}, t = {t}")
    return [displayMatrix]

anim = animation.FuncAnimation(fig, func = animate, frames = iterations, interval = 30)
#plt.show()


mpegWriter = animation.FFMpegWriter(fps = 30)

anim.save("resistantEscapeCancerousTissueGrowth.mp4", writer = mpegWriter)

gifWriter = animation.PillowWriter(fps = 30)
anim.save("resistantEscapeCancerousTissueGrowth.gif", writer = gifWriter)

exit()