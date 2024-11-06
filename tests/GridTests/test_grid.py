from Grid import Grid
import pytest


def test_construction():
    constructorGrid = Grid(10, 10, [])

    assert constructorGrid.dimensions == (10, 10)

def test_nonpositive_dimensions():
    with pytest.raises(ValueError):
        nonpositiveGrid = Grid(0, 0, [])

def test_negative_dimensions():
    with pytest.raises(ValueError):
        negativeGrid = Grid(-1, -1, [])