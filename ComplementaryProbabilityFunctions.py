probDoNothing = 0.0

def p_r(fitness):
    return (1 - probDoNothing) * (fitness)

def p_q(fitness):
    return (1 - probDoNothing) * (1 - fitness) / 2

def p_a(fitness):
    return (1 - probDoNothing) * (1 - fitness) / 2

def p_n(fitness):
    return fitness