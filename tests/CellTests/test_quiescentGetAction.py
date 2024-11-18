from Grid import Grid
import math

def test_quiescentBadConditions():
    phi = 2 * math.pi * 0.5

    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 0, True]
    ])

    cell = unitaryGrid.spaces[(0, 0)].getOccupant()

    assert cell.getAction(phi)[0] in [cell.doNothing]

def test_quiescentGoodConditions():
    phi = 2 * math.pi * 0

    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 0, True]
    ])

    cell = unitaryGrid.spaces[(0, 0)].getOccupant()

    assert cell.getAction(phi)[0] in [cell.anagenesis]

def test_quiescentIntermediateConditions():
    phi = 2 * math.pi * 0.25

    unitaryGrid = Grid(1, 1, [
        [(0, 0), 1, 0, True]
    ])

    cell = unitaryGrid.spaces[(0, 0)].getOccupant()

    assert cell.getAction(phi)[0] in [cell.anagenesis,
                                      cell.doNothing]