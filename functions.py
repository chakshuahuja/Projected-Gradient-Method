def norm(v):
    return sum([x**2 for x in v])**0.5
def multiply_sm(v, s):
    return [x*s for x in v]
def vector_diff(v1, v2):
    return [x[0] - x[1] for x in zip(v1, v2)]
def rectProj(v, rect):
    l, u = rect[0], rect[1]
    n = len(l)
    result = []
    for i in range(n):
        if(abs(v[i]) <= abs(l[i])):
            result.append(l[i])
        elif(abs(v[i]) >= abs(u[i])):
            result.append(u[i])
        else:
            result.append(v[i])
    return result
