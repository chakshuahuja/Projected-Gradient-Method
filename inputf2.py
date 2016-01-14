import math
def f(v):
    return (7*v[0]*v[1])/(math.e**(v[0]**2 + v[1]**2))
def gradf(v):
    rx = (7*v[1] - 14*v[1]*v[0]**2)/(math.e**(v[0]**2 + v[1]**2))
    ry = (7*v[0] - 14*v[0]*v[1]**2)/(math.e**(v[0]**2 + v[1]**2))
    return [rx, ry]
def rect():
    return [(+0.5, -0.5), (2,-2)]
