zero = lambda f: (lambda x: x)

def add1(n):
    return lambda f: (lambda x: f(n(f)(x)))

one   = add1(zero)
two   = add1(one)
three = add1(two)

def add(m, n):
    return lambda f: (lambda x: m(f)(n(f)(x)))

inc = lambda x: x + 1

print(zero(inc)(0))
print((add1(zero))(inc)(0))
print((add1(add1(zero)))(inc)(0))
