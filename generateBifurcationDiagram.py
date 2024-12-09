from differenceEquationApproximation import runApproximation
from CellSpacer import runABM
import numpy as np
import matplotlib.pyplot as plt

yellowEndpoints = np.zeros(81)
greenEndpoints = np.zeros(81)

environmentUsed = "periodic"

for k in range(81):
    print(f"On iteration {k}")
    yellowEndpoints[k], greenEndpoints[k] = runABM(15000, environmentUsed, [0.2, 0.2 + 0.01 * k], toPlot = True)

with open(f"yellowEndpoints{environmentUsed}.txt", 'w') as f:
    for k in range(81):
        f.write(f"{yellowEndpoints[k]}\n")

with open(f"greenEndpoints{environmentUsed}.txt", 'w') as f:
    for k in range(81):
        f.write(f"{greenEndpoints[k]}\n")

plt.plot(np.array([0.02 + 0.01 * k for k in range(81)]), yellowEndpoints, label = "Yellow Cells")
plt.plot(np.array([0.02 + 0.01 * k for k in range(81)]), yellowEndpoints, label = "Green Cells")
plt.xlabel("Difference in S-Value")
plt.ylabel("Long-Term Population Value")
plt.title(f"Long-Term Population Behavior ({environmentUsed}) vs Difference in S-Value")
plt.legend()
plt.savefig(f"OutputGIFs/LongTermBehaviorStudies/yellowAndGreenEndpoints{environmentUsed}.png")