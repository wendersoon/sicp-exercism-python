from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

def unique_pairs(n):
    return [(i, j) for i in range(1, n + 1) for j in range(1, i)]

def prime_sum(pair):
    i, j = pair
    return is_prime(i + j)

 
def make_pair_sum(pair):
    i, j = pair
    return (i, j, i + j)

def prime_sum_pairs(n):
    return list(map(make_pair_sum, filter(prime_sum, unique_pairs(n))))


print(unique_pairs(6))
print(prime_sum_pairs(6))
