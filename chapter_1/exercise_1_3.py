def square(x):
    return x*x

def sumSquare(x, y):
    return square(x) + square(y)

def fun(x, y, z):
    if (x <= y) and (x <= z):
        return sumSquare(y, z)
    elif (y <= x) and (y <= z):
        return sumSquare(x, z)
    else:
        return sumSquare(x, y)
    
print((fun(10, 10, 10))==(sumSquare(10, 10)))
print((fun(100, 1, 10))==(sumSquare(100, 10)))
