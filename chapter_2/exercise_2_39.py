def fold_right(op, initial, sequence):
    if not sequence:
        return initial
    return op(sequence[0], fold_right(op, initial, sequence[1:]))

def fold_left(op, initial, sequence):
    print(initial)
    print(sequence)
    if not sequence:
        return initial
    return fold_left(op, op(initial, sequence[0]), sequence[1:])

def reverse_right(sequence):
    # op(x, acc) -> acc + [x], initial = []
    return fold_right(lambda x, acc: acc + [x], [], sequence)

def reverse_left(sequence):
    # op(acc, x) -> [x] + acc, initial = []
    return fold_left(lambda acc, x: [x] + acc, [], sequence)

print(reverse_right([1, 2, 3]))
print(reverse_left([1, 2, 3]))