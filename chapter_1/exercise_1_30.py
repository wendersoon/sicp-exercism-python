def sum(term, a, next, b):

    def iter(a, result):
        if a > b:
            return result
        return iter(next(a), result + term(a))
    
    return iter(a, 0)

def inc(n):
    return n + 1

def cube(x):
    return x * x * x

def sum_cubes(a, b):
    return sum(cube, a, inc, b)

print(sum_cubes(1, 10))


def identity(x):
    return x

def sum_integers(a, b):
    return sum(identity, a, inc, b)

print(sum_integers(1, 10))