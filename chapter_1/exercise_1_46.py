def iterative_improve(good_enough, improve):
    def iter_fn(guess):
        next_guess = improve(guess)
        if good_enough(guess, next_guess):
            return next_guess
        return iter_fn(next_guess)
    return iter_fn


def square(x):
    return x * x


def average(x, y):
    return (x + y) / 2


def fixed_point(f, first_guess, tolerance=1e-5):
    def close_enough(v1, v2):
        return abs(v1 - v2) < tolerance

    def improve_guess(guess):
        return f(guess)

    def try_guess(guess):
        next_guess = improve_guess(guess)
        if close_enough(guess, next_guess):
            return next_guess
        return try_guess(next_guess)

    return try_guess(first_guess)


def average_damp(f):
    return lambda x: average(x, f(x))


def sqrt_fixed_point(x):
    return fixed_point(average_damp(lambda y: x / y), 1.0)


def sqrt(x):
    def improve(guess):
        return average(guess, x / guess)

    def good_enough(guess, next_guess):
        return abs(square(next_guess) - x) < 0.001

    return iterative_improve(good_enough, improve)(1.0)


if __name__ == "__main__":
    print(sqrt(11))  
    print(sqrt_fixed_point(11))
