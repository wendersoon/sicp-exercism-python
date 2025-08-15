def double(a):
    return a + a

def halve(a):
    return a / 2

def fast_mul_iter(a, b, i):
    if b == 0:
        return i
    elif b % 2 == 0:
        return fast_mul_iter(double(a), halve(b), i)
    else:
        return fast_mul_iter(double(a), halve(b - 1), i + a)
    
def mul(a, b):
    return fast_mul_iter(a, b, 0)

print(mul(7, 7))
print(mul(2, 30))
print(mul(51, 0))
print(mul(7, 1))
print(mul(9, 9))
print(mul(4, 25))
