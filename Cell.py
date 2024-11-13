import random
from ComplementaryProbabilityFunctions import p_a, p_n, p_q, p_r, probDoNothing

class Cell():
    def __init__(self, container, colorValue, phi_m, quiescent_):
        self.containingSpace = container
        self.color = colorValue
        self.phiM = phi_m
        self.quiescent = quiescent_

        if abs(self.color) > 1 or abs(self.phiM) > 1:
            raise(ValueError(f"The passed cell parameters are too large: color = {self.color}; phiM = {self.phiM}"))
    
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

        #print(f"Action chosen is {action}")
            

    def proliferate(self, neighboringPlots):
        newlyFilledPlot = random.choice(list(neighboringPlots))
        newlyFilledPlot.setOccupant(Cell(newlyFilledPlot, self.color, self.phiM, self.quiescent))

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