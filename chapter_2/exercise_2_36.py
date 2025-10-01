def accumulate(op, initial, sequence):
    if not sequence:
        return initial
    return op(sequence[0], accumulate(op, initial, sequence[1:]))


def accumulate_n(op, initial, sequences):
    # base: se as subsequências acabaram (primeira vazia), retornar lista vazia
    if not sequences or not sequences[0]:
        return []
    first_column = [seq[0] for seq in sequences]
    rest_seqs = [seq[1:] for seq in sequences]
    return [accumulate(op, initial, first_column)] + accumulate_n(op, initial, rest_seqs)


sum = lambda x, y: x + y

s = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print(accumulate_n(sum, 0, s))