def square(x):
    return x * x

def average(x, y):
    return (x + y) / 2

def improve(guess, x):
    return (((x / square(guess)) + 2 * guess) / 3)

def good_enough(previous_guess, guess):
    return abs((guess - previous_guess)/ guess) < 0.00000000001

def sqrt_iter(guess, x):
    if good_enough(guess, improve(guess, x)):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)

def sqrt(x):
    return sqrt_iter(1.0, x)

print(sqrt(27))
print(10*'-')
print(sqrt(64))