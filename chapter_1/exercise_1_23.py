import time

def square(n):
    return n * n

def next(n):
    if n == 3:
        return 3
    return n + 2

def find_divisor(n , test_divisor):
    if square(test_divisor) > n:
        return n
    elif n % test_divisor == 0:
        return test_divisor
    else:
        return find_divisor(n, next(test_divisor))

def smallest_divisor(n):
    return find_divisor(n, 2)

def prime(n):
    return n == smallest_divisor(n)

def timed_prime_test(n):
    print(n)
    return start_prime_test(n, time.time())

def start_prime_test(n, start_time):
    if prime(n):
        report_time(time.time() - start_time)
        return True
    print("nothing")
    return False

def report_time(elapsed_time):
    print("***", elapsed_time)

def search_for_primes(start_range, end_range):
    if start_range % 2 == 0:   # garante que começa em ímpar
        return search_for_primes(start_range + 1, end_range)
    elif start_range > end_range:
        print("done")
        return
    else:
        timed_prime_test(start_range)
        return search_for_primes(start_range + 2, end_range)

search_for_primes(10000, 10009)
