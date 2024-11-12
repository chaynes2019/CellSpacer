import random

class Cell():
    def __init__(self, container, mu_, numDivisions, omega_, colorValue):
        self.containingSpace = container
        self.numberDivisionsPerformed = numDivisions
        self.mu = mu_
        self.omega = omega_
        self.color = colorValue
    
    def getColor(self):
        return self.color

    def tick(self):
        proliferativePossibilities = self.containingSpace.getOpenNeighbors()
        neighboringSpaces = self.containingSpace.getNeighbors()

        if len(proliferativePossibilities) > self.mu and self.numberDivisionsPerformed < self.omega:
            #Telomere shortening affects both daughter cells
            self.numberDivisionsPerformed += 1
            self.proliferate(neighboringSpaces)
        '''
        else:
            print(f"We're overflowing our proliferative prerogatives! NumDivisions = {self.numberDivisionsPerformed}")
        '''
        
    def proliferate(self, neighboringPlots):
        newlyFilledPlot = random.choice(list(neighboringPlots))
        newlyFilledPlot.setOccupant(Cell(newlyFilledPlot, self.mu, self.numberDivisionsPerformed, self.omega, self.color))

    def apoptote(self):
        self.containingSpace.setOccupant(None)
        del self