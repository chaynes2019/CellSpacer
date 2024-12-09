import random
import math
from ComplementaryProbabilityFunctions import p_a, p_n, p_q, p_r, probDoNothing

mutationProbability = 0.001

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

    def tick(self, phi, sVals):
        proliferativePossibilities = self.containingSpace.getOpenNeighbors()
        neighboringSpaces = self.containingSpace.getNeighbors()

        action = self.getAction(phi)[0]

        yellowSVal = sVals[0]
        greenSVal = sVals[1]

        if action == self.proliferate:
            action(proliferativePossibilities, yellowSVal, greenSVal)
        else:
            action()

        #print(f"Action chosen is {action}")
            

    def proliferate(self, openNeighboringPlots, yellowSVal, greenSVal):
        if len(openNeighboringPlots) > 0:
            newlyFilledPlot = random.choice(list(openNeighboringPlots))
            
            mutant = random.choices([True, False], [mutationProbability, 1 - mutationProbability])[0]
            #print("Mutant Boolean returned: {} with mutation probability: {}".format(mutant, mutationProbability))

            if mutant:
                if abs(self.color - 0.5) < 0.01:
                    newColor = 1.0
                    newSVal = yellowSVal
                else:
                    newColor = 0.5
                    newSVal = greenSVal

                newlyFilledPlot.setOccupant(Cell(newlyFilledPlot, newColor, self.t_mFrac, self.quiescent, newSVal))
            else:
                newlyFilledPlot.setOccupant(Cell(newlyFilledPlot, self.color, self.t_mFrac, self.quiescent, self.s))

        else:
            pass

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
                 [p_r(fitness, self.s),
                  p_q(fitness, self.s),
                  p_a(fitness),
                  probDoNothing]
            )
        
        else:
            return random.choices(
                [self.anagenesis,
                 self.doNothing],
                 [p_n(fitness, self.s),
                  1 - p_n(fitness, self.s)]
            )