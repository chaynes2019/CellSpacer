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

iterations = 1000

gridHistory = np.zeros((xLength, yLength, iterations))

initialYellowCells = [[(x, y), 1, yellowt_m, False, yellowSVal] for x, y in itertools.product(range(xLength), range(yLength)) if (x, y) != (0, 0) and ((x + y) % 2 == 0)]

initialGreenCells = [[(x, y), 0.5, greent_m, False, greenSVal] for x, y in itertools.product(range(xLength), range(yLength)) if (x, y) != (0, 0) and ((x + y) % 2 == 1)]

yellowProliferatorsOverTime = np.zeros(iterations)
yellowQuiescentOverTime = np.zeros(iterations)
greenProliferatorsOverTime = np.zeros(iterations)
greenQuiescentOverTime = np.zeros(iterations)
environmentValuesOverTime = np.zeros(iterations)

grid = Grid(xLength, yLength, initialYellowCells + initialGreenCells)

for t in range(iterations):
    color_matrix = cellVisual.computeMatrixFromGrid(grid)
    gridHistory[:, :, t] = color_matrix

    yellowProliferatorsOverTime[t], yellowQuiescentOverTime[t], greenProliferatorsOverTime[t], greenQuiescentOverTime[t] = grid.getYellowGreenPopSizes()

    environmentValuesOverTime[t] = grid.phiVal
    grid.tick(t)

plt.plot(range(iterations), yellowProliferatorsOverTime, label = "Yellow Proliferators")
plt.plot(range(iterations), yellowQuiescentOverTime, label = "Yellow Quiescent")
plt.plot(range(iterations), greenProliferatorsOverTime, label = "Green Proliferators")
plt.plot(range(iterations), greenQuiescentOverTime, label = "Green Quiescent")
plt.title("Populations versus Time")
plt.ylim([0, 10500])
plt.xlim([0, iterations])
plt.xlabel("Time (cell cycles)")
plt.ylabel("Cells")
plt.legend()

plt.savefig("OutputGIFs/differenceEquationFidelityTests/quasiBrownianEnvironmentSeed1HomogeneousStartPopPlot.png")

'''
fig, ax = plt.subplots()

displayMatrix = ax.matshow(gridHistory[:, :, 0])
ax.set_title(f"(Time = 0, Environment = 0")

def animate(t):
    environmentVal = environmentValuesOverTime[t]
    environmentVal = round(environmentVal, 2)

    displayMatrix.set_array(gridHistory[:, :, t])
    ax.set_title(f"(Time = {t}, Environment = {environmentVal}")
    return [displayMatrix]

anim = animation.FuncAnimation(fig, func = animate, frames = iterations, interval = 30)

gifWriter = animation.PillowWriter(fps = 30)
anim.save("OutputGIFs/differenceEquationFidelityTests/quasiBrownianEnvironmentSeed1HomogeneousStart.gif", writer = gifWriter)
'''

fig2, ax2 = plt.subplots()
ax2.plot(range(iterations), environmentValuesOverTime, label = "Environment")
ax2.set_title("Environment over Time")
ax2.set_xlabel("Time")
ax2.set_ylabel("Environment Value")
ax2.legend()

fig2.savefig("OutputGIFs/differenceEquationFidelityTests/quasiBrownianEnvironmentSeed1EnvironmentValuesExtremelyLong.png")

exit()