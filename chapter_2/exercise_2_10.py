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

def add_interval(x, y):
    return make_interval(
        lower_bound(x) + lower_bound(y),
        upper_bound(x) + upper_bound(y)
    )

def sub_interval(x, y):
    return make_interval(
        lower_bound(x) + upper_bound(y),
        upper_bound(x) + lower_bound(y)
    )

def mul_interval(x, y):
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return make_interval(
        min(p1, p2, p3, p4),
        max(p1, p2, p3, p4)
    )

def div_interval(x, y):
    if lower_bound(y) <= 0 <= upper_bound(y):
        return "Division range includes zero"
    return mul_interval(
        x,
        make_interval(1 / upper_bound(y), 1 / lower_bound(y))
    )

def width_interval(x):
    return (upper_bound(x) - lower_bound(x)) / 2

interval_1 = make_interval(22, 23)
interval_2 = make_interval(-2, 3)

result = div_interval(interval_1, interval_2)
print(f"Result division: {result}")
