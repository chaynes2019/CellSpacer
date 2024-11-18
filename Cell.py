import random
import math
from ComplementaryProbabilityFunctions import p_a, p_n, p_q, p_r, probDoNothing

class Cell():
    def __init__(self, container, colorValue, t_mVal, quiescent_, sVal):
        self.containingSpace = container
        self.color = colorValue
        self.t_mFrac = t_mVal
        self.quiescent = quiescent_
        self.s = sVal

        if abs(self.color) > 1 or abs(self.t_mFrac) > 1:
            raise(ValueError(f"The passed cell parameters are too large: color = {self.color}; t_mFrac = {self.t_mFrac}"))
    
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
        newlyFilledPlot.setOccupant(Cell(newlyFilledPlot, self.color, self.t_mFrac, self.quiescent))

    def quiesce(self):
        self.quiescent = True

    def anagenesis(self):
        self.quiescent = False

    def apoptote(self):
        self.containingSpace.setOccupant(None)
        del self

    def doNothing(self):
        pass

    def getFitness(self, phi):
        return 0.5 * math.cos(phi - self.t_mFrac * 2 * math.pi) + 0.5

    def getAction(self, phi):
        fitness = self.getFitness(phi)

        if self.quiescent == False:
            return random.choices(
                [self.proliferate,
                 self.quiesce,
                 self.apoptote,
                 self.doNothing],
                 [p_r(fitness),
                  p_q(fitness, self.s),
                  p_a(fitness),
                  probDoNothing]
            )
        
        else:
            return random.choices(
                [self.anagenesis,
                 self.doNothing],
                 [p_n(fitness),
                  1 - p_n(fitness)]
            )