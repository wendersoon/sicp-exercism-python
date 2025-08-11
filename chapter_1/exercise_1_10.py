def A(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return 2 * y
    elif y == 1:
        return 2
    else:
        return A((x - 1), A(x, y-1))

print(A(1, 10))
print(A(2, 4))
print(A(3, 3))

# f computes 2*n
def f(n):
    return A(0, n)

# g computes 2^n
def g(n):
    return A(1, n)

# h computes 2^h(n-1)
def h(n):
    return A(2, n)
