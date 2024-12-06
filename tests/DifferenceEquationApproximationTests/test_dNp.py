from differenceEquationApproximation import dNp
import math

def test_fullGridFitness1():
    populations_ = [2601, 2500, 2600, 2500]
    fitness_ = 1

    assert dNp(populations_, fitness_) == [2500, -2500, 2500, -2500]

def test_fullGridFitness0():
    populations_ = [2500, 2500, 2500, 2500]
    fitness_ = 0

    assert dNp(populations_, fitness_) == [-2500, 0, -2500, 0]

def test_emptyGridFitness1():
    populations_ = [0, 0, 0, 0]
    fitness_ = 1

    assert dNp(populations_, fitness_) == [0, 0, 0, 0]

def test_emptyGridFitness0():
    populations_ = [0, 0, 0, 0]
    fitness_ = 0

    assert dNp(populations_, fitness_) == [0, 0, 0, 0]

def test_fullGridHalfFitness():
    populations_ = [2601, 2500, 2600, 2500]
    fitness_ = 0.5

    assert dNp(populations_, fitness_) == [2500 - (1 - math.sqrt(0.5)) * 2601, -2500, 2500 - (1 - math.sqrt(0.5)) * 2600, -2500]

'''
def test_halfGridFitness1():
    pass

def test_halfGridFitness0():
    pass
'''