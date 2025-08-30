from math import log

TOLERANCE = 0.00001

def average(x, y):
    return (x+y)/2

def fixed_point(f, guess):
    def close_enough(v1, v2):
        return abs(v1 - v2) < TOLERANCE
    step = 1
    def tente(guess, step):
        next = f(guess)
        
        print(f"Number generate: {next}; step: {step}")
        step += 1
        
        if close_enough(guess, next):
            return next
        return tente(next, step)
    
    return tente(guess, step)

print(fixed_point(lambda x: log(1000)/log(x), 2))
print(30*"-")


print(fixed_point(lambda x: average(x, log(1000)/log(x)), 2))