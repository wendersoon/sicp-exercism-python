def p():
    return p

def test(x, y):
    if x == 0:
        return 0
    return y

print(test(0, p))

# Python uses normal-order evaluation
# If python evaluated the expressions in applicative order, 
#"p" would be called and then the code would fall into an infinite loop.