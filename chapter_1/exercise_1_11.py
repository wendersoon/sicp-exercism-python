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
def f_loop(n, n1, n2, n3, nth):
    if n == nth:
        return n1
    else:
        return f_loop(n, (n1 + 2 * n2 + 3 * n3),
                        n1, 
                        n2, 
                        1 + nth
                        )
        
def f_iterative(n):
    if n < 3:
        return n
    else:
        return f_loop(n, 2, 1, 0, 2)
    
print(f_iterative(5))
print(f_iterative(7))