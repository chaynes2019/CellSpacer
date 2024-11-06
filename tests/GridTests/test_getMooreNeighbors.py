from Grid import Grid

def test_getMooreNeighborsInUnitaryGrid():
    unitaryGrid = Grid(1, 1, [])

    assert unitaryGrid.getMooreNeighbors(0, 0) == set([unitaryGrid.spaces[(0, 0)]])

def test_getMooreNeighborsInLinearGrid():
    linearGrid = Grid(10, 1, [])

    assert linearGrid.getMooreNeighbors(4, 0) == set([linearGrid.spaces[3, 0],
                                                      linearGrid.spaces[4, 0],
                                                      linearGrid.spaces[5, 0]])

def test_getMooreNeighborsInSquareGrid():
    squareGrid = Grid(3, 3, [])

    assert squareGrid.getMooreNeighbors(1, 1) == set([squareGrid.spaces[0, 1],
                                                      squareGrid.spaces[0, 0],
                                                      squareGrid.spaces[2, 0],
                                                      squareGrid.spaces[1, 2],
                                                      squareGrid.spaces[2, 1],
                                                      squareGrid.spaces[0, 2],
                                                      squareGrid.spaces[2, 2],
                                                      squareGrid.spaces[1, 0]])