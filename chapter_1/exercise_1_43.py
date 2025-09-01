def square(x):
    return x * x

def compose(f, g):
    return lambda x: f(g(x))

def repeated(f, n):
    if n == 1:
        return f
    else:
        return compose(f, repeated(f, n - 1))
    
print(repeated(square, 2)(5))