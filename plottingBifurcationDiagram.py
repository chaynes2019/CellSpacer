import matplotlib.pyplot as plt
import numpy as np

yellowEndpoints = np.zeros(81)
greenEndpoints = np.zeros(81)

environmentUsed = "periodic"

with open(f"yellowEndpoints{environmentUsed}.txt", 'r') as f:
    cellNumbersOverTime = f.readlines()

    for k, cellNum in enumerate(cellNumbersOverTime):
        yellowEndpoints[k] = float(cellNum)

with open(f"greenEndpoints{environmentUsed}.txt", 'r') as f:
    cellNumbersOverTime = f.readlines()

    for k, cellNum in enumerate(cellNumbersOverTime):
        greenEndpoints[k] = float(cellNum)

plt.plot(np.array([0.02 + 0.01 * k for k in range(81)]), yellowEndpoints, 'y', label = "Yellow Cell Endpoints")
plt.plot(np.array([0.02 + 0.01 * k for k in range(81)]), greenEndpoints, 'g', label = "Green Cell Endpoints")
plt.plot(np.array([0.455 for k in range(10201)]), np.array([x for x in range(10201)]), 'k--', label = "Stable Coexistence")
plt.xlabel("Difference in S-Value")
plt.ylabel("Population Endpoints")
plt.legend()
plt.title("Population Endpoints vs. Diff in S-Value")
plt.savefig(f"populationBifurcationDiagramFor{environmentUsed}Environment.png")
plt.show()
    