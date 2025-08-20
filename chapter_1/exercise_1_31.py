
###################### A ##############################

def product(term, a, next, b):
    if a > b:
        return 1
    return term(a) * product(term, next(a), next, b)

def inc(x):
    return x + 1

def identify(x):
    return x

def factorial(n):
    return product(identify, 1, inc, n)

print(factorial(10))

def wallis_product(n):
    def term(n):
        return ((2*n) / ((2 * n) - 1)) * ((2*n) / ((2 * n) + 1)) 

    return product(term, 1, inc, n)

print(wallis_product(100))

###################### B ##############################

def product_iter(term, a, next, b):
    
    def iter(a, result):
        if a > b:
            return result
        return iter(next(a), result * term(a))
    
    return iter(a, 1)

def inc(x):
    return x + 1

def identify(x):
    return x

def factorial2(n):
    return product_iter(identify, 1, inc, n)

print(factorial2(10))
