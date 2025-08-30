def cont_frac(n, d, k):
    def recur(i):
        if k == i:
            return n(i) / d(i)
        return n(i) / (d(i) + recur(i + 1))
    
    return recur(1)
                                   

print(cont_frac(lambda i: 1, lambda i: 1, 12))

def cont_frac_iterative(n, d, k):

    def iterative(i, result):
        if i == 0:
            return result
        
        return iterative(i - 1, n(i) / (result + d(i)))
    
    return iterative(k - 1, n(k) / d(k))

print(cont_frac_iterative(lambda i: 1, lambda i: 1, 12))
