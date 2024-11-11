from Grid import Grid

def test_emptyUnitaryGrid():
    emptyUnitaryGrid = Grid(1, 1, [])

    centerSpace = emptyUnitaryGrid.spaces[(0, 0)]

    #The getOpenNeighbors function returns a list, not a set,
    #because the function iterates over the set, checking each
    #to see if they are open. And if not, then 
    assert centerSpace.getOpenNeighbors() == set([centerSpace])

def test_filledUnitaryGrid():
    filledUnitaryGrid = Grid(1, 1, [
        [(0, 0), 0, 1, 1, 1, 1, False]
    ])

    centerSpace = filledUnitaryGrid.spaces[(0, 0)]

    #The getOpenNeighbors function returns a list, not a set,
    #because the function iterates over the set, checking each
    #to see if they are open. And if not, then 
    assert centerSpace.getOpenNeighbors() == set([])

def test_emptyLinearGrid():
    emptyLinearGrid = Grid(9, 1, [])

    centerSpace = emptyLinearGrid.spaces[(4, 0)]
    
    assert centerSpace.getOpenNeighbors() == set([emptyLinearGrid.spaces[3, 0],
                                                  emptyLinearGrid.spaces[4, 0],
                                                  emptyLinearGrid.spaces[5, 0]])
    
def test_centerFilledLinearGrid():
    centerFilledLinearGrid = Grid(9, 1, [
        [(4, 0), 0, 5, 5, 1, 1, False]
    ])

    centerSpace = centerFilledLinearGrid.spaces[(4, 0)]
    
    assert centerSpace.getOpenNeighbors() == set([centerFilledLinearGrid.spaces[3, 0],
                                                  centerFilledLinearGrid.spaces[5, 0]])
    
def test_leftFilledLinearGrid():
    leftFilledLinearGrid = Grid(9, 1, [
        [(3, 0), 0, 2, 3, 1, 1, False]
    ])

    centerSpace = leftFilledLinearGrid.spaces[(4, 0)]
    
    assert centerSpace.getOpenNeighbors() == set([
        leftFilledLinearGrid.spaces[4, 0],
        leftFilledLinearGrid.spaces[5, 0]
        ])

def test_surroundedLinearGrid():
    surroundedLinearGrid = Grid(9, 1, [
        [(3, 0), 0, 2, 3, 1, 1, False],
        [(4, 0), 0, 5, 6, 1, 1, False],
        [(5, 0), 0, 3, 4, 1, 1, False]
    ])

    centerSpace = surroundedLinearGrid.spaces[(4, 0)]
    
    assert centerSpace.getOpenNeighbors() == set([])

def test_checkeredSquareGrid():
    squareGrid = Grid(3, 3, [
        [(1, 0), 0, 5, 7, 1, 1, False],
        [(0, 1), 0, 6, 8, 1, 1, False],
        [(2, 1), 0, 4, 7, 1, 1, False],
        [(1, 2), 0, 3, 3, 1, 1, False]
    ])

    centerSpace = squareGrid.spaces[(1, 1)]

    assert centerSpace.getOpenNeighbors() == set([])