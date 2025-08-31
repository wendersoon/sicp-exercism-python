def double(g):
    return lambda x: g(g(x))

def inc(x):
    return x + 1

print((double(double(double))(inc))(5))