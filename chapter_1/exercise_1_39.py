def cont_frac_iterative(n, d, k):

    def iterative(i, result):
        if i == 0:
            return result
        
        return iterative(i - 1, n(i) / (result + d(i)))
    
    return iterative(k - 1, n(k) / d(k))

                                
def tang_cf(x, k):
    return cont_frac_iterative(
        lambda i: x if i == 1 else -(x**2),
        lambda i: (2 * i) - 1,
        k
    )

x = 1

print(tang_cf(x, 10))