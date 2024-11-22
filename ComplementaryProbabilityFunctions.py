probDoNothing = 0.0
import math

def p_r(fitness, s):
    return 1 - p_q(fitness, s) - p_a(fitness)

def p_q(fitness, s):
    return (1 - (fitness**100) / (s**100 + fitness**100)) * (1 - p_a(fitness))

def p_a(fitness):
    return 1 - math.sqrt(fitness)

def p_n(fitness, s):
    return (fitness**100) / (s**100 + fitness**100)