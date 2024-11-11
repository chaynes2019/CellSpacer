probDoNothing = 0.5

def p_r(deltaPhi):
    return (1 - probDoNothing) * (1 - deltaPhi)

def p_q(deltaPhi):
    return (1 - probDoNothing) * (deltaPhi) / 2

def p_a(deltaPhi):
    return (1 - probDoNothing) * (deltaPhi) / 2

def p_n(deltaPhi):
    return 1 - deltaPhi