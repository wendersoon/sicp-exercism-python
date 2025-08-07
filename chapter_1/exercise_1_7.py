def square(x):
    return x * x

def average(x, y):
    return (x + y) / 2

def improve(guess, x):
    return average(guess, (x / guess))

def good_enough(previous_guess, guess):
    return abs((guess - previous_guess)/ guess) < 0.00000000001

def sqrt_iter(guess, x):
    print(guess)
    if good_enough(guess, improve(guess, x)):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)

def sqrt(x):
    return sqrt_iter(1.0, x)

print(sqrt(0.000000000000000123))
