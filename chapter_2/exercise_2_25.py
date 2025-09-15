def cons(x, y):
    return lambda m: m(x, y)

def car(z):
    return z(lambda p, q: p)

def cdr(z):
    return z(lambda p, q: q)

list1 = cons(1,cons(3, cons(cons(5, cons(7, None)), cons(9, None))))

list2 = cons(cons(7, None), None)

list3 = cons(1, cons(cons(2, cons(cons(3, cons(cons(4, cons(cons(5, cons(cons(6, cons(7, None)), None)), None)), None)), None)), None))

result1 = car(cdr(car(cdr(cdr(list1)))))
print(result1)

result2 = car(car(list2))
print(result2)

result3 = car(cdr(car(cdr(car(cdr(car(cdr(car(cdr(car(cdr(list3))))))))))))
print(result3)