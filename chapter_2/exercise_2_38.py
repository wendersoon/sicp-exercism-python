def fold_right(op, initial, sequence):
    if not sequence:
        return initial
    return op(sequence[0], fold_right(op, initial, sequence[1:]))

def fold_left(op, initial, sequence):
    if not sequence:
        return initial
    return fold_left(op, op(initial, sequence[0]), sequence[1:])

print(fold_right(lambda x, y: x / y, 1, [1, 2, 3]))
print(fold_left(lambda x, y: x / y, 1, [1, 2, 3]))

print(fold_right(lambda x, y: [x, y], None, [1, 2, 3]))
print(fold_left(lambda x, y: [x, y], None, [1, 2, 3]))

# Any associative or commutative operation produces the same values