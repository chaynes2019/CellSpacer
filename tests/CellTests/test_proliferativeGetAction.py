from Grid import Grid

def test_proliferateRetrieval():
    phi = 1

    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 1, False]
    ])

    cell = unitaryGrid.spaces[(0, 0)].getOccupant()

    assert cell.getAction(phi)[0] in [cell.proliferate,
                                      cell.doNothing]

def test_apoptosisAndQuiesceRetrieval():
    phi = 0

    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 1, False]
    ])

    cell = unitaryGrid.spaces[(0, 0)].getOccupant()

    assert cell.getAction(phi)[0] in [cell.apoptote,
                                      cell.quiesce, 
                                      cell.doNothing]

def test_retrievalInIntermediateConditions():
    phi = 0.5

    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 1, False]
    ])

    cell = unitaryGrid.spaces[(0, 0)].getOccupant()

    assert cell.getAction(phi)[0] in [cell.proliferate,
                                      cell.apoptote,
                                      cell.quiesce, 
                                      cell.doNothing]