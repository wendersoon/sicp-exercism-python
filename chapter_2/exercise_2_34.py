def accumulate(op, initial, sequence):
    if not sequence:
        return initial
    return op(sequence[0], accumulate(op, initial, sequence[1:]))

def horner_eval(x, coefficient_sequence):
    return accumulate(
        lambda this_coeff, higher_terms: this_coeff + (higher_terms * x), 
        0, 
        coefficient_sequence
    )

print(horner_eval(2, [1, 3, 0, 5, 0, 1]))
