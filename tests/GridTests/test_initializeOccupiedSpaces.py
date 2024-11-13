from Grid import Grid
import itertools

def test_filledUnitaryGrid():
    unitaryGrid = Grid(1, 1, [[(0, 0), 1, 1, False]])

    assert len(unitaryGrid.spaces) == 1
    assert unitaryGrid.spaces[(0, 0)].getOccupant() != None

    occupant = unitaryGrid.spaces[(0, 0)].getOccupant()
    assert occupant.phiM == 1


def test_bookendLinearGrid():
    linearGrid = Grid(10, 1, [
        [(0, 0), 1, 0.25, False],
        [(9, 0), 1, 0.6, False]
    ])

    occupant1 = linearGrid.spaces[(0, 0)].getOccupant()
    assert occupant1.phiM == 0.25

    occupant2 = linearGrid.spaces[(9, 0)].getOccupant()
    assert occupant2.phiM == 0.6

def test_checkeredSquareGrid():
    squareGrid = Grid(3, 3, [
        [(0, 0), 1, 1, False],
        [(2, 0), 1, 0, False],
        [(1, 1), 1, 0.5, False],
        [(0, 2), 1, 0.75, False],
        [(2, 2), 1, 0.3, False]
    ])

    occupant1 = squareGrid.spaces[(0, 0)].getOccupant()
    assert occupant1.phiM == 1

    occupant2 = squareGrid.spaces[(2, 0)].getOccupant()
    assert occupant2.phiM == 0

    occupant3 = squareGrid.spaces[(1, 1)].getOccupant()
    assert occupant3.phiM == 0.5

    occupant4 = squareGrid.spaces[(0, 2)].getOccupant()
    assert occupant4.phiM == 0.75

    occupant5 = squareGrid.spaces[(2, 2)].getOccupant()
    assert occupant5.phiM == 0.3

