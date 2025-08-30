TOLERANCE = 0.00001


def fixed_point(f, guess):
    def close_enough(v1, v2):
        return abs(v1 - v2) < TOLERANCE
    
    def tente(guess):
        next = f(guess)

        if close_enough(guess, next):
            return next
        return tente(next)
    
    return tente(guess)

print(fixed_point(lambda x: 1 + 1/x, 1))

# Resulte = 1.6180327868852458