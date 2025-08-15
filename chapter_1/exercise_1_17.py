def mul(a, b):
    if b == 0:
        return 0
    return a + mul(a, b - 1)

print(mul(5,9))

def double(a):
    return a + a

def halve(a):
    return a / 2

def fast_mul(a, b):
    if b == 0:
        return 0
    elif b % 2 == 0:
        return fast_mul(double(a), halve(b))
    else:
        return a + fast_mul(a, b - 1)
    
print(fast_mul(5, 10))