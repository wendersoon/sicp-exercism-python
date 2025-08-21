########################### A ##############################

def square(n):
    return n * n

def next(n):
    if n == 2:
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

def inc(x):
    return x + 1

def filtered_accumulatte(filter, combiner, null_value, term, a, next, b):
    if a > b:
        return null_value
    return combiner(term(a) if filter(a) else null_value, filtered_accumulatte(filter, combiner, null_value, term, next(a), next, b))
    
def sum_squares_prime(a, b):
    return filtered_accumulatte(prime, lambda x, y: x + y, 0, square, a, inc, b)

print(sum_squares_prime(1, 10))

########################### B ##############################
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def identity(x):
    return x

def product_of_relative_prime(n):

    def relative_prime(i):
        return gcd(i, n) == 1

    return filtered_accumulatte(relative_prime, lambda x, y: x * y, 1, identity, 1, inc, (n-1))

print(product_of_relative_prime(10))
