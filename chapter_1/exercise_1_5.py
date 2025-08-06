def p():
    return p

def test(x, y):
    if x == 0:
        return 0
    return y

print(test(0, p))

# Python uses normal-order evaluation