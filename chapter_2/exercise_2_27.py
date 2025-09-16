x = [[1, 2], [3, 4]]


def deep_reverse(x):
    if not isinstance(x, list):
        return x
    return [deep_reverse(i) for i in reversed(x)]


print(deep_reverse(x))