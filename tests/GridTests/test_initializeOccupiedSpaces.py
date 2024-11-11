from Grid import Grid
import itertools

def test_filledUnitaryGrid():
    unitaryGrid = Grid(1, 1, [[(0, 0), 0, 0, 0, 1, 1, False]])

    assert len(unitaryGrid.spaces) == 1
    assert unitaryGrid.spaces[(0, 0)].getOccupant() != None

    occupant = unitaryGrid.spaces[(0, 0)].getOccupant()
    assert occupant.numberDivisionsPerformed == 0
    assert occupant.omega == 0


def test_bookendLinearGrid():
    linearGrid = Grid(10, 1, [
        [(0, 0), 0, 0, 0, 1, 1, False],
        [(9, 0), 0, 5, 10, 1, 1, False]
    ])

    occupant1 = linearGrid.spaces[(0, 0)].getOccupant()
    assert occupant1.numberDivisionsPerformed == 0
    assert occupant1.omega == 0

    occupant2 = linearGrid.spaces[(9, 0)].getOccupant()
    assert occupant2.numberDivisionsPerformed == 5
    assert occupant2.omega == 10

def test_checkeredSquareGrid():
    squareGrid = Grid(3, 3, [
        [(0, 0), 0, 5, 10, 1, 1, False],
        [(2, 0), 0, 3, 6, 1, 1, False],
        [(1, 1), 0, 2, 4, 1, 1, False],
        [(0, 2), 0, 6, 12, 1, 1, False],
        [(2, 2), 0, 4, 8, 1, 1, False]
    ])

    occupant1 = squareGrid.spaces[(0, 0)].getOccupant()
    assert occupant1.numberDivisionsPerformed == 5
    assert occupant1.omega == 10

    occupant2 = squareGrid.spaces[(2, 0)].getOccupant()
    assert occupant2.numberDivisionsPerformed == 3
    assert occupant2.omega == 6

    occupant3 = squareGrid.spaces[(1, 1)].getOccupant()
    assert occupant3.numberDivisionsPerformed == 2
    assert occupant3.omega == 4

    occupant4 = squareGrid.spaces[(0, 2)].getOccupant()
    assert occupant4.numberDivisionsPerformed == 6
    assert occupant4.omega == 12

    occupant5 = squareGrid.spaces[(2, 2)].getOccupant()
    assert occupant5.numberDivisionsPerformed == 4
    assert occupant5.omega == 8

