from Grid import Grid
import math

def test_proliferateRetrieval():
    phi = 0

    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 0, False, 0.5]
    ])

    cell = unitaryGrid.spaces[(0, 0)].getOccupant()

    assert cell.getAction(phi)[0] in [cell.proliferate,
                                      cell.doNothing]
    
def test_proliferateAlternatePhiRetrieval():
    phi = 2 * math.pi * 1

    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 0, False, 0.5]
    ])

    cell = unitaryGrid.spaces[(0, 0)].getOccupant()

    assert cell.getAction(phi)[0] in [cell.proliferate,
                                      cell.doNothing]

def test_apoptosisAndQuiesceRetrieval():
    phi = 2 * math.pi * 0.5

    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 0, False, 0.5]
    ])

    cell = unitaryGrid.spaces[(0, 0)].getOccupant()

    assert cell.getAction(phi)[0] in [cell.apoptote,
                                      cell.quiesce, 
                                      cell.doNothing]

def test_retrievalInIntermediateConditions():
    phi = 2 * math.pi * 0.25

    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 0, False, 0.5]
    ])

    cell = unitaryGrid.spaces[(0, 0)].getOccupant()

    assert cell.getAction(phi)[0] in [cell.proliferate,
                                      cell.apoptote,
                                      cell.quiesce, 
                                      cell.doNothing]