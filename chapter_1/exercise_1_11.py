# Generates Recursive Process
def f(n):
    if n < 3:
        return n
    else:
        return f(n-1) + 2 * f(n-2) + 3 * f(n-3)

print(f(5))
print(f(7))
print(5*'-')
# Generates Iterative Process
def f_iter_loop(n):
    if n < 3:
        return n
    n3, n2, n1 = 0, 1, 2  # f(0), f(1), f(2)
    nth = 2
    while nth < n:
        novo = n1 + 2*n2 + 3*n3
        n3, n2, n1 = n2, n1, novo
        nth += 1
    return n1
    
print(f_iter_loop(5))
print(f_iter_loop(7))