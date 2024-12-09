import CellSpacerVisualizer as cellVisual
from Grid import Grid
import numpy as np
import math
import itertools

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def runABM(numIters, environment, sVals, xLength = 101, yLength = 101, toPlot = False, toAnimate = False, environmentalAnimation = False):
    xLength = 101
    yLength = 101

    yellowt_m = 0
    greent_m = 0

    yellowSVal = sVals[0]
    greenSVal = sVals[1]

    iterations = numIters

    gridHistory = np.zeros((xLength, yLength, iterations))

    #initialYellowCells = [[(x, y), 1, yellowt_m, False, yellowSVal] for x, y in itertools.product(range(xLength), range(yLength)) if (x, y) != (0, 0) and ((x + y) % 2 == 0)]
    initialYellowCells = [[(x, y), 1, yellowt_m, False, yellowSVal] for x, y in itertools.product(range(xLength), range(yLength))]

    #initialGreenCells = [[(x, y), 0.5, greent_m, False, greenSVal] for x, y in itertools.product(range(xLength), range(yLength)) if (x, y) != (0, 0) and ((x + y) % 2 == 1)]
    initialGreenCells = []

    yellowProliferatorsOverTime = np.zeros(iterations)
    yellowQuiescentOverTime = np.zeros(iterations)
    greenProliferatorsOverTime = np.zeros(iterations)
    greenQuiescentOverTime = np.zeros(iterations)
    environmentValuesOverTime = np.zeros(iterations)

    grid = Grid(xLength, yLength, initialYellowCells + initialGreenCells, environment, yellowSVal, greenSVal)

    for t in range(iterations):
        color_matrix = cellVisual.computeMatrixFromGrid(grid)
        gridHistory[:, :, t] = color_matrix

        yellowProliferatorsOverTime[t], yellowQuiescentOverTime[t], greenProliferatorsOverTime[t], greenQuiescentOverTime[t] = grid.getYellowGreenPopSizes()

        environmentValuesOverTime[t] = grid.phiVal
        grid.tick(t)

    if toPlot == True:
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

        plt.savefig(f"OutputGIFs/differenceEquationFidelityTests/{environment}EnvironmentSeed1AllYellowStartPopPlotIters{numIters}.png")

        fig2, ax2 = plt.subplots()
        ax2.plot(range(iterations), environmentValuesOverTime, label = "Environment")
        ax2.set_title("Environment over Time")
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Environment Value")
        ax2.legend()

        fig2.savefig(f"OutputGIFs/differenceEquationFidelityTests/{environment}EnvironmentSeed1EnvironmentValuesAllYellowIters{numIters}.png")
    
    if environmentalAnimation == True:
        fig3, ax3 = plt.subplots()

        ax3.set_title("Environment over Time")

        ax3.plot(np.array([math.cos(2 * math.pi * 0.001 * k) for k in range(1000)]),
                 np.array([math.sin(2 * math.pi * 0.001 * k) for k in range(1000)]),
                 'k')

    if toAnimate == True:
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
        anim.save(f"OutputGIFs/differenceEquationFidelityTests/{environment}EnvironmentSeed1AllYellowStart.gif", writer = gifWriter)
    
    return (yellowProliferatorsOverTime[-1] + yellowQuiescentOverTime[-1],
            greenProliferatorsOverTime[-1] + greenQuiescentOverTime[-1])