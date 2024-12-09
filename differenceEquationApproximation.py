from ComplementaryProbabilityFunctions import p_a, p_n, p_q, p_r
import math
import random
import numpy as np
import matplotlib.pyplot as plt

mutationProb = 0.001

def dNp(populations, fitness):
    yellowNp = populations[0]
    yellowNq = populations[1]
    greenNp = populations[2]
    greenNq = populations[3]

    popSum = yellowNp + yellowNq + greenNp + greenNq
    fracOccupied = popSum / 10201

    yellowSVal = 0.2
    greenSVal = 0.4

    yellowProliferatingMultiplier = (1 -(fracOccupied ** 1.5)) * (1 - mutationProb) * p_r(fitness, yellowSVal) - p_a(fitness) - p_q(fitness, yellowSVal)
    greenProliferatingMultiplier = (1 - (fracOccupied ** 1.5)) * (1 - mutationProb) * p_r(fitness, greenSVal) - p_a(fitness) - p_q(fitness, greenSVal)

    return np.array([
        yellowProliferatingMultiplier * yellowNp + p_n(fitness, yellowSVal) * yellowNq + (1 - (fracOccupied ** 1.5)) * mutationProb * p_r(fitness, greenSVal) * greenNp,
        p_q(fitness, yellowSVal) * yellowNp - p_n(fitness, yellowSVal) * yellowNq,
        greenProliferatingMultiplier * greenNp + p_n(fitness, greenSVal) * greenNq + (1 - (fracOccupied ** 1.5)) * mutationProb * p_r(fitness, yellowSVal) * yellowNp,
        p_q(fitness, greenSVal) * greenNp - p_n(fitness, greenSVal) * greenNq
    ])

def getFitness(phi):
        return 0.5 * math.cos(phi) + 0.5

def phi(t, phiPrev, environment, randomNumGen):
    if environment == "fluctuating":
        T = 100

        return 2 * math.pi * t / T
    
    #Random environment
    elif environment == "random":
        return random.uniform(0, 2 * math.pi)
    

    #QuasiBrownian Environment
    elif environment == "quasibrownian":
        return phiPrev + randomNumGen.normal(0, 0.25)
    

def runApproximation(initialPopulations, numIterations, environment, randomSeed = 1, plot = False):
    random.seed(randomSeed)
    rng = np.random.default_rng(randomSeed)

    yellowProliferatorPop = initialPopulations[0]
    yellowQuiescentPop = initialPopulations[1]
    greenProliferatorPop = initialPopulations[2]
    greenQuiescentPop = initialPopulations[3]

    cellPopulations = np.array([yellowProliferatorPop,
                                yellowQuiescentPop,
                                greenProliferatorPop,
                                greenQuiescentPop])

    timeLength = numIterations

    cellPopulationsOverTime = np.zeros((4, timeLength))
    environmentOverTime = np.zeros(timeLength)

    for t in range(timeLength):
        cellPopulationsOverTime[:, t] = cellPopulations

        phiPrevious = 0 if t == 0 else environmentOverTime[t - 1]

        phiVal = phi(t, phiPrevious, environment, rng)
        environmentOverTime[t] = phiVal

        fitnessVal = getFitness(phiVal)

        cellPopulations = cellPopulations + dNp(cellPopulations, fitnessVal)

    #plt.plot(range(timeLength), cellPopulationsOverTime[0, :] + cellPopulationsOverTime[1, :] +  cellPopulationsOverTime[2, :] + cellPopulationsOverTime[3, :], label = "Total Population")

    if plot == True:
        plt.plot(range(timeLength), cellPopulationsOverTime[0, :], label = "Yellow Proliferators")
        plt.plot(range(timeLength), cellPopulationsOverTime[1, :], label = "Yellow Quiescent")
        plt.plot(range(timeLength), cellPopulationsOverTime[2, :], label = "Green Proliferators")
        plt.plot(range(timeLength), cellPopulationsOverTime[3, :], label = "Green Quiescent")


        plt.legend()
        plt.title("Populations versus Time")
        plt.xlabel("Time (cell cycles)")
        plt.ylabel("Cells")
        plt.xlim([0, timeLength])
        plt.ylim([0, 10500])

        plt.savefig("OutputGIFs/differenceEquationFidelityTests/differenceEquationQuasiBrownianEnvironmentSeed1.png")

        fig, ax = plt.subplots()
        ax.plot(range(timeLength), environmentOverTime, label = "Environment")
        ax.set_title("Environment over Time")
        ax.set_xlabel("Time")
        ax.set_ylabel("Environment Value")
        ax.legend()

        fig.savefig("OutputGIFs/differenceEquationFidelityTests/differenceEquationQuasiBrownianEnvironmentSeed1EnvironmentValues.png")

    return (cellPopulationsOverTime[0, -1] + cellPopulationsOverTime[1, -1],
            cellPopulationsOverTime[2, -1] + cellPopulationsOverTime[3, -1])