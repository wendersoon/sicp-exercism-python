def accumulate(op, initial, sequence):
    if not sequence:
        return initial
    return op(sequence[0], accumulate(op, initial, sequence[1:]))

def append_acc(seq1, seq2):
    return accumulate(lambda x, y: [x] + y, seq2, seq1)

def enumerate_tree(tree):
    if not tree:
        return []
    elif not isinstance(tree, list):
        return [tree]
    else:
        return append_acc(
            enumerate_tree(tree[0]),
            enumerate_tree(tree[1:])
        )

def count_leaves(tree):
    return accumulate(
        lambda x, y: x + y, 
        0,
        list(map(lambda x: 1, enumerate_tree(tree)))
    )

print(count_leaves([[1, 2], 3, 4]))