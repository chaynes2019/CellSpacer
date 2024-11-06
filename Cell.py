import random

class Cell():
    def __init__(self, container, numDivisions, omega, colorValue):
        self.containingSpace = container
        self.neighbors = self.containingSpace.getNeighbors()
        self.numberDivisionsPerformed = numDivisions
        self.omega = omega
        self.color = colorValue
    
    def getColor(self):
        return self.color

    def tick(self):
        proliferativePossibilities = self.containingSpace.getOpenNeighbors()

        if len(proliferativePossibilities) > 0 and self.numberDivisionsPerformed < self.omega:
            #Telomere shortening affects both daughter cells
            self.numberDivisionsPerformed += 1
            self.proliferate(proliferativePossibilities)

    def proliferate(self, openPlots):
        newlyFilledPlot = random.choice(list(openPlots))
        newlyFilledPlot.setOccupant(Cell(newlyFilledPlot, self.numberDivisionsPerformed, self.omega, self.color))