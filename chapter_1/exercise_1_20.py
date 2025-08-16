def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

"""
# Here is a great solution https://sicp-solutions.net/post/sicp-solution-exercise-1-20/

"""