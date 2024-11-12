import random

class Cell():
    def __init__(self, container, mu_, numDivisions, omega_, telomeraseParam, colorValue):
        self.containingSpace = container
        self.numberDivisionsPerformed = numDivisions
        self.mu = mu_
        self.omega = omega_
        self.telomeraseVal = telomeraseParam
        self.color = colorValue
    
    def getColor(self):
        return self.color

    def tick(self, debug):
        proliferativePossibilities = self.containingSpace.getOpenNeighbors()
        neighboringSpaces = self.containingSpace.getNeighbors()

        if debug:
            print(f"Number of Divisions = {self.numberDivisionsPerformed}")
            print(f"Number of Open Neighbors = {len(proliferativePossibilities)}")
            print(f"Mu = {self.mu}")
            print(f"Omega = {self.omega}")

        if len(proliferativePossibilities) > self.mu and self.numberDivisionsPerformed < self.omega:
            #Telomere shortening affects both daughter cells
            self.numberDivisionsPerformed += 1 - self.telomeraseVal
            self.proliferate(neighboringSpaces)
        '''
        else:
            print(f"We're overflowing our proliferative prerogatives! NumDivisions = {self.numberDivisionsPerformed}")
        '''

    def proliferate(self, neighboringPlots):
        newlyFilledPlot = random.choice(list(neighboringPlots))
        newlyFilledPlot.setOccupant(Cell(newlyFilledPlot, self.mu, self.numberDivisionsPerformed, self.omega, self.telomeraseVal, self.color))

    def apoptote(self):
        self.containingSpace.setOccupant(None)
        del self