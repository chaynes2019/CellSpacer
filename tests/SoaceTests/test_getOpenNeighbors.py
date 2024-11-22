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
        [(0, 0), 1, 1, False, 0.5]
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
        [(4, 0), 1, 1, False, 0.5]
    ])

    centerSpace = centerFilledLinearGrid.spaces[(4, 0)]
    
    assert centerSpace.getOpenNeighbors() == set([centerFilledLinearGrid.spaces[3, 0],
                                                  centerFilledLinearGrid.spaces[5, 0]])
    
def test_leftFilledLinearGrid():
    leftFilledLinearGrid = Grid(9, 1, [
        [(3, 0), 1, 1, False, 0.5]
    ])

    centerSpace = leftFilledLinearGrid.spaces[(4, 0)]
    
    assert centerSpace.getOpenNeighbors() == set([
        leftFilledLinearGrid.spaces[4, 0],
        leftFilledLinearGrid.spaces[5, 0]
        ])

def test_surroundedLinearGrid():
    surroundedLinearGrid = Grid(9, 1, [
        [(3, 0), 1, 1, False, 0.5],
        [(4, 0), 1, 1, False, 0.5],
        [(5, 0), 1, 1, False, 0.5]
    ])

    centerSpace = surroundedLinearGrid.spaces[(4, 0)]
    
    assert centerSpace.getOpenNeighbors() == set([])

def test_checkeredSquareGrid():
    squareGrid = Grid(3, 3, [
        [(1, 0), 1, 1, False, 0.5],
        [(0, 1), 1, 1, False, 0.5],
        [(2, 1), 1, 1, False, 0.5],
        [(1, 2), 1, 1, False, 0.5]
    ])

    centerSpace = squareGrid.spaces[(1, 1)]

    assert centerSpace.getOpenNeighbors() == set([])