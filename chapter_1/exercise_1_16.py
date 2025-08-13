def square(x):
    return x * x

def fast_expt_iter(b, n, a):
    if n == 0:
        return a
    elif n % 2 == 0:
        return fast_expt_iter(square(b), n/2, a)
    else:
        a = a * b
        n = n - 1
        return fast_expt_iter(b, n, a)

def fast_expt(b, n):
    return fast_expt_iter(b, n, 1)

print(fast_expt(3, 10))