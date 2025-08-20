########################### A ##############################

def accumulatte(combiner, null_value, term, a, next, b):
    if a > b:
        return null_value
    return combiner(term(a), accumulatte(combiner, null_value, term, next(a), next, b))

def inc(n):
    return n + 1

def identify(x):
    return x

def cube(x):
    return x * x * x

#### sum
def sum(term, a, next, b):
    return accumulatte(lambda x, y: x + y, 0, term, a, next, b)

def sum_cubes(a, b):
    return sum(cube, a, inc, b)

print(sum_cubes(1, 10))

#### product
def product(term, a, next, b):
    return accumulatte(lambda x, y: x * y, 1, term, a, next, b)

def factorial(n):
    return product(identify, 1, inc, n)

print(factorial(10))

print(15*"-")
########################### B ##############################
def accumulatte2(combiner, null_value, term, a, next, b):
    def iter(a, result):
        if a > b:
            return result
        return iter(next(a), combiner(result, term(a)))

    return iter(next(a), null_value)

### sum
def sum2(term, a, next, b):
    return accumulatte2(lambda x, y: x + y, 0, term, a, next, b)

def sum_cubes2(a, b):
    return sum2(cube, a, inc, b)

print(sum_cubes2(1, 10))

### product
def product2(term, a, next, b):
    return accumulatte2(lambda x, y: x * y, 1, term, a, next, b)

def factorial2(n):
    return product2(identify, 1, inc, n)

print(factorial2(10))
