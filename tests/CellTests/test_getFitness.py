from Grid import Grid
import math

def test_getFitnessGoodConditions():
    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 0, False, 0.5]
        ])
    
    cellInQuestion = unitaryGrid.spaces[(0, 0)].getOccupant()

    periodFrac = 0

    assert cellInQuestion.getFitness(2 * math.pi * periodFrac) == 1

def test_getFitnessGoodConditionsSecondPeriod():
    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 0, False, 0.5]
        ])
    
    cellInQuestion = unitaryGrid.spaces[(0, 0)].getOccupant()
    
    periodFrac = 1

    assert cellInQuestion.getFitness(2 * math.pi * periodFrac) == 1

def test_getFitnessBadConditions():
    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 0, False, 0.5]
        ])
    
    cellInQuestion = unitaryGrid.spaces[(0, 0)].getOccupant()
    
    periodFrac = 0.5

    assert cellInQuestion.getFitness(2 * math.pi * periodFrac) == 0

def test_getFitnessIntermediateConditions():
    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 0, False, 0.5]
        ])
    
    cellInQuestion = unitaryGrid.spaces[(0, 0)].getOccupant()

    periodFrac = 0.25

    assert 0 < cellInQuestion.getFitness(2 * math.pi * periodFrac) < 1