def d_euler(i):
    if i%3 == 2:
        return 2 * ((i + 1) / 3)
    return 1

def cont_frac(n, d, k):
    def recur(i):
        if k == i:
            return n(i) / d(i)
        return n(i) / (d(i) + recur(i + 1))
    
    return recur(1)
                                   

print(cont_frac(lambda i: 1, d_euler, 15))