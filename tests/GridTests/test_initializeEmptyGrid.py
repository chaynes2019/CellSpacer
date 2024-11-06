from Grid import Grid
import itertools

def test_emptyUnitaryGrid():
    unitaryGrid = Grid(1, 1, [])

    assert len(unitaryGrid.spaces) == 1
    assert unitaryGrid.spaces[(0, 0)].getOccupant() == None

def test_emptyLinearGrid():
    linearGrid = Grid(10, 1, [])

    for x, y in itertools.product(range(10), range(1)):
        assert linearGrid.spaces[(x, y)].getOccupant() == None

def test_emptySquareGrid():
    squareGrid = Grid(10, 10, [])

    for x, y in itertools.product(range(10), range(10)):
        assert squareGrid.spaces[(x, y)].getOccupant() == None