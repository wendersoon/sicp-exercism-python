def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def cons(x, y):
    return [x, y]

def car(obj):
    return obj[0]

def cdr(obj):
    return obj[1]    

def make_rat(n, d):
    g = gcd(n, d)
    sing = 1 if d > 0 else -1

    return cons((n / g) * sing, (d / g) * sing)

def numer(x):
    return car(x)

def denom(x):
    return cdr(x)

def print_rat(x):
    print(f"{numer(x)}/{denom(x)}")

def add_rat(x, y):
    return make_rat(
        (numer(x) * denom(y)) + (numer(y) * denom(x)),
        denom(x) * denom(y)
    )

def sub_rat(x, y):
    return make_rat(
        (numer(x) * denom(y)) - (numer(y) * denom(x)),
        denom(x) * denom(y)
    )

def mul_rat(x, y):
    return make_rat(
        numer(x) * numer(y),
        denom(x) * denom(y)
    )

def div_rat(x, y):
    return make_rat(
        numer(x) * denom(y),
        denom(x) * numer(y)
    )

def equal_rat(x, y):
    return (numer(x) * denom(y)) == (numer(y) * denom(x))

one_third= make_rat(-1, 3)
test = make_rat(-1, -3)
test2 = make_rat(1, -3)


print(add_rat(one_third, one_third))
print(add_rat(test, test))
print(add_rat(test2, test2))
print(add_rat(test, test2))


