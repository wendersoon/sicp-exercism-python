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

def fast_prime(n, times=5):
    if times == 0:
        return True
    elif fermat_test(n):
        return fast_prime(n, times - 1)
    return False


def timed_prime_test(n, times=5):
    start = time.time()
    result = fast_prime(n, times)
    elapsed = time.time() - start
    if result:
        print(f"{n} *** {elapsed:.6f} seconds")
        return True
    else:
        print(f"{n} is not prime")
        return False

def search_for_primes(start, count=3, times=100):
    if start % 2 == 0:
        start += 1
    found = 0
    n = start
    while found < count:
        if timed_prime_test(n, times):
            found += 1
        n += 2

print("Primes > 1,000:")
search_for_primes(1000)

print("\nPrimes > 10,000:")
search_for_primes(10000)

print("\nPrimes > 100,000:")
search_for_primes(100000)

print("\nPrimes > 1,000,000:")
search_for_primes(1000000)

print("\nPrimes > 1,000,000,000:")
search_for_primes(1000000000)
