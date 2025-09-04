def cons(x, y):
    return lambda m: m(x, y)

def car(z):
    return z(lambda p, q: p)

def cdr(z):
    return z(lambda p, q: q)


teste = cons(1, 2)
print(car(teste))
print(cdr(teste))
