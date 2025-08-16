def square(n):
    return n * n

def find_divisor(n , test_divisor):
    if square(test_divisor) > n:
        return n
    elif n % test_divisor == 0:
        return test_divisor
    else:
        return find_divisor(n, test_divisor + 1)

def smallest_divisor(n):
    return find_divisor(n, 2)

def prime(n):
    return n == smallest_divisor(n)

print(prime(199))
print(prime(1999))
print(prime(19999))