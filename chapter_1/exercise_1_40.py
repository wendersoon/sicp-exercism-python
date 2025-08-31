DX = 0.000001
TOLERANCE = 0.000001

def fixed_point(f, guess):
    def close_enough(v1, v2):
        return abs(v1 - v2) < TOLERANCE
    
    def tente(guess):
        next = f(guess)

        if close_enough(guess, next):
            return next
        return tente(next)
    
    return tente(guess)

def fixed_point_of_transform(g, transform, guess):
    return fixed_point(transform(g), guess)

def deriv(g):
    return lambda x: (g(x + DX) - g(x)) / DX

def newton_transform(g):
    return lambda x: x - (g(x)/(deriv(g)(x)))

def newtons_method(g, guess):
    return fixed_point(newton_transform(g), guess)

def cubic(a, b, c):
    return lambda x: (x * x *x) + (a * x * x) + (b * x) + c

a=1
b=1
c=1

print(newtons_method(cubic(a, b, c), 1.0))