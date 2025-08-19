import sys
sys.setrecursionlimit(10000000)

def cube(n):
    return n * n * n

def sum(term, a, next, b):
    if a > b:
        return 0
    return term(a) + sum(term, next(a), next, b)

def integral(f, a, b, dx):
    def add_dx(x):
        return dx + x
    return sum(f, (a + (dx / 2.0)), add_dx, b) * dx

print(integral(cube, 0, 1, 0.001))

####### SIMPSON'S RULE #############

def integral_simpson_rule(f, a, b, n):
    h = (b - a)/n
    
    def add_2h(x):
        return x + h + h
    
    return (h / 3) * (f(a) + f(b) + (2 * sum(f, add_2h(a), add_2h , b - h)) + (4 * sum(f, a + h, add_2h, b))) 

print(integral_simpson_rule(cube, 0, 1, 1000))
