# VECTORS
V1 = [1, 2, 3, 4]
V2 = [4, 5, 6, 6]
V3 = [6, 7, 8, 9]

# MATRICES
M = [V1, V2, V3]

_sum = lambda x, y: x + y

_mul = lambda x, y: x * y

append = lambda x, y: [x, y]

def accumulate(op, initial, sequence):
    if not sequence:
        return initial
    return op(sequence[0], accumulate(op, initial, sequence[1:]))

def accumulate_n(op, initial, sequences):
    if not sequences or not sequences[0]:
        return []
    first_column = [seq[0] for seq in sequences]
    rest_seqs = [seq[1:] for seq in sequences]
    return [accumulate(op, initial, first_column)] + accumulate_n(op, initial, rest_seqs)

def dot_product(v, w):
    return accumulate(_sum, 0, [x for x in map(_mul, v, w)])

def matrix_mult_vector(m, v):
    return [x for x in map(lambda row: dot_product(row, v), m)]

def transpose(mat):
    if not mat:
        return []
    return [list(col) for col in zip(*mat)]

def matrix_mult_matrix(m, n):
    
    if not m or not n:
        return []
    
    rows_m = len(m)
    cols_m = len(m[0])
    
    rows_n = len(n)
    cols_n = len(n[0])
    
    if cols_m != rows_n:
        raise ValueError(f"Incompatible dimensions: m is {rows_m}x{cols_m}, n is {rows_n}x{cols_n}")

    cols_of_n = transpose(n)
    return [[dot_product(row_m, col_n) for col_n in cols_of_n] for row_m in m]

