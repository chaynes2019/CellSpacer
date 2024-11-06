from Grid import Grid

def test_getNeighborsInUnitaryGrid():
    unitaryGrid = Grid(1, 1, [])

    assert unitaryGrid.getVonNeumannNeighbors(0, 0) == set([unitaryGrid.spaces[(0, 0)]])

def test_getNeighborsInLinearGrid():
    linearGrid = Grid(10, 1, [])

    assert linearGrid.getVonNeumannNeighbors(4, 0) == set([linearGrid.spaces[3, 0],
                                                           linearGrid.spaces[4, 0],
                                                           linearGrid.spaces[5, 0]])

def test_getNeighborsInSquareGrid():
    squareGrid = Grid(3, 3, [])

    assert squareGrid.getVonNeumannNeighbors(1, 1) == set([squareGrid.spaces[0, 1],
                                                           squareGrid.spaces[1, 2],
                                                           squareGrid.spaces[2, 1],
                                                           squareGrid.spaces[1, 0]])