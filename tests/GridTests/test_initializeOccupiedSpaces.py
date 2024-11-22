from Grid import Grid
import itertools

def test_filledUnitaryGrid():
    unitaryGrid = Grid(1, 1, [[(0, 0), 1, 1, False, 0.5]])

    assert len(unitaryGrid.spaces) == 1
    assert unitaryGrid.spaces[(0, 0)].getOccupant() != None

    occupant = unitaryGrid.spaces[(0, 0)].getOccupant()
    assert occupant.t_mFrac == 1


def test_bookendLinearGrid():
    linearGrid = Grid(10, 1, [
        [(0, 0), 1, 0.25, False, 0.5],
        [(9, 0), 1, 0.6, False, 0.5]
    ])

    occupant1 = linearGrid.spaces[(0, 0)].getOccupant()
    assert occupant1.t_mFrac == 0.25

    occupant2 = linearGrid.spaces[(9, 0)].getOccupant()
    assert occupant2.t_mFrac == 0.6

def test_checkeredSquareGrid():
    squareGrid = Grid(3, 3, [
        [(0, 0), 1, 1, False, 0.5],
        [(2, 0), 1, 0, False, 0.5],
        [(1, 1), 1, 0.5, False, 0.5],
        [(0, 2), 1, 0.75, False, 0.5],
        [(2, 2), 1, 0.3, False, 0.5]
    ])

    occupant1 = squareGrid.spaces[(0, 0)].getOccupant()
    assert occupant1.t_mFrac == 1

    occupant2 = squareGrid.spaces[(2, 0)].getOccupant()
    assert occupant2.t_mFrac == 0

    occupant3 = squareGrid.spaces[(1, 1)].getOccupant()
    assert occupant3.t_mFrac == 0.5

    occupant4 = squareGrid.spaces[(0, 2)].getOccupant()
    assert occupant4.t_mFrac == 0.75

    occupant5 = squareGrid.spaces[(2, 2)].getOccupant()
    assert occupant5.t_mFrac == 0.3

