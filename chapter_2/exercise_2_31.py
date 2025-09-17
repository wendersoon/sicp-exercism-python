def square(x):
    return x * x

def tree_map(f, tree):
    if isinstance(tree, list):
        return [tree_map(f, subtree) for subtree in tree]
    else:
        return f(tree)

def square_tree(tree):
    return tree_map(square, tree)

tree = [1, [4, [9, 16], 25], [36, 49]]

print(square_tree(tree))