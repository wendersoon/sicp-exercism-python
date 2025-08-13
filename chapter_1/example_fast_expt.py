def square(x):
    return x * x

def fast_expt(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(fast_expt(b, n/2))
    else:
        return b * fast_expt(b, n-1)
    
print(fast_expt(2, 5))