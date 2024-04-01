# para ser usado en Sage

def Hosoya(G):
    f = sage.graphs.matchpoly.matching_polynomial(G, complement=True, name=None)
    a = [abs(x) for x in f.coefficients()]
    return [a, sum(a)]

