import time
import random

def square(x):
    return x * x

def remainder(x, y):
    return x % y

def expmod(base, exp, m):
    if exp == 0:
        return 1
    elif remainder(exp, 2) == 0:
        return remainder(square(expmod(base, exp // 2, m)), m)
    else:
        return remainder(base * expmod(base, exp - 1, m), m)

def fermat_test(n):
    def try_it(a):
        return expmod(a, n, n) == a
    return try_it(1 + random.randrange(1, n - 1))

def fast_prime(n, times=100):
    if times == 0:
        return True
    elif fermat_test(n):
        return fast_prime(n, times - 1)
    return False

print(fast_prime(561))
print(fast_prime(1105))
print(fast_prime(1729))
print(fast_prime(2465))
print(fast_prime(2821))
print(fast_prime(6601))
