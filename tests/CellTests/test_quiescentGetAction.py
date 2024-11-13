from Grid import Grid

def test_quiescentBadConditions():
    phi = 0

    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 1, True]
    ])

    cell = unitaryGrid.spaces[(0, 0)].getOccupant()

    assert cell.getAction(phi)[0] in [cell.doNothing]

def test_quiescentGoodConditions():
    phi = 1

    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 1, True]
    ])

    cell = unitaryGrid.spaces[(0, 0)].getOccupant()

    assert cell.getAction(phi)[0] in [cell.anagenesis]

def test_quiescentIntermediateConditions():
    phi = 0.5

    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 1, True]
    ])

    cell = unitaryGrid.spaces[(0, 0)].getOccupant()

    assert cell.getAction(phi)[0] in [cell.anagenesis,
                                      cell.doNothing]