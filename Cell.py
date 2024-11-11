import random
from ComplementaryProbabilityFunctions import p_a, p_n, p_q, p_r, probDoNothing

class Cell():
    def __init__(self, container, eta_, numDivisions, omega_, colorValue, phi_m, quiescent_):
        self.containingSpace = container
        self.numberDivisionsPerformed = numDivisions
        self.eta = eta_
        self.omega = omega_
        self.color = colorValue
        self.phiM = phi_m
        self.quiescent = quiescent_
    
    def getColor(self):
        return self.color

    def tick(self, phi):
        proliferativePossibilities = self.containingSpace.getOpenNeighbors()
        neighboringSpaces = self.containingSpace.getNeighbors()

        action = self.getAction(phi)[0]

        if action == self.proliferate:
            action(neighboringSpaces)
        else:
            action()
            

    def proliferate(self, neighboringPlots):
        newlyFilledPlot = random.choice(list(neighboringPlots))
        newlyFilledPlot.setOccupant(Cell(newlyFilledPlot, self.eta, self.numberDivisionsPerformed, self.omega, self.color))

    def quiesce(self):
        self.quiescent = True

    def anagenesis(self):
        self.quiescent = False

    def apoptote(self):
        self.containingSpace.setOccupant(None)
        del self

    def doNothing(self):
        pass

    def getAction(self, phi):
        phiDiff = abs(phi - self.phiM)

        if self.quiescent == False:
            return random.choices(
                [self.proliferate,
                 self.quiesce,
                 self.apoptote,
                 self.doNothing],
                 [p_r(phiDiff),
                  p_q(phiDiff),
                  p_a(phiDiff),
                  probDoNothing]
            )
        
        else:
            return random.choices(
                [self.anagenesis,
                 self.doNothing],
                 [p_n(phiDiff),
                  1 - p_n(phiDiff)]
            )