def cons(a, b):
    return (2**a) * (3**b)

def car(x):
    def car_iter(x, count):
        if x%2 == 0:
            return car_iter(x/2, count+1)
        return count
    
    return car_iter(x, 0)

def cdr(x):
    def cdr_iter(x, count):
        if x%3 == 0:
            return cdr_iter(x/3, count+1)
        return count
    
    return cdr_iter(x, 0)


test = cons(2, 0)
print(test)
print(car(test))
print(cdr(test))