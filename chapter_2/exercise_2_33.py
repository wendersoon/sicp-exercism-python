def accumulate(op, initial, sequence):
    if not sequence:
        return initial
    return op(sequence[0], accumulate(op, initial, sequence[1:]))

def map_acc(p, sequence):
    return accumulate(lambda x, y: [p(x)] + y, [], sequence)

def append_acc(seq1, seq2):
    return accumulate(lambda x, y: [x] + y, seq2, seq1)

def length(sequence):
    return accumulate(lambda _, y: 1 + y, 0, sequence)
