def square(x):
    return x * x

def inc(x):
    return x + 1

def compose(f, g):
    return lambda x: f(g(x))

print(compose(square, inc)(6))