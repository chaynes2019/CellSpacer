import CellSpacerVisualizer as cellVisual
from Grid import Grid
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

xLength = 101
yLength = 101

yellowPhiM = 1
greenPhiM = 0.8

iterations = 1000

gridHistory = np.zeros((xLength, yLength, iterations))

grid = Grid(xLength, yLength, [
    [(40, 50), 1, yellowPhiM, False],
    [(60, 50), 0.5, greenPhiM, False]
])

for t in range(iterations):
    color_matrix = cellVisual.computeMatrixFromGrid(grid)
    gridHistory[:, :, t] = color_matrix

    grid.tick(t)

fig, ax = plt.subplots()

displayMatrix = ax.matshow(gridHistory[:, :, 0])
ax.set_title("Populations (yellow phi_m = {yellowPhiM}, green phi_m = {greenPhiM}) at Time = 0, phi = 1")

def animate(t):
    phiVal = grid.phi(t)
    phiVal = round(phiVal, 2)

    displayMatrix.set_array(gridHistory[:, :, t])
    ax.set_title(f"Populations (yellow phi_m = {yellowPhiM}, green phi_m = {greenPhiM}) at Time = {t}, phi = {phiVal}")
    return [displayMatrix]

anim = animation.FuncAnimation(fig, func = animate, frames = iterations, interval = 30)

gifWriter = animation.PillowWriter(fps = 30)
anim.save("OutputGIFs/y1g08PeriodicDrasticEnvironmentalSwitch_2.gif", writer = gifWriter)

exit()