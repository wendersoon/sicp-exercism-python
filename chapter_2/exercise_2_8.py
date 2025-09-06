def cons(x, y):
    return lambda m: m(x, y)

def car(z):
    return z(lambda p, q: p)

def cdr(z):
    return z(lambda p, q: q)

def make_interval(x, y):
    return cons(x, y)

def lower_bound(x):
    return car(x)

def upper_bound(x):
    return cdr(x)

def sub_interval(x, y):
    return make_interval(
        lower_bound(x) + upper_bound(y),
        upper_bound(x) + lower_bound(y)
    )
