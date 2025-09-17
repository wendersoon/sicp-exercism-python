def square_tree_direct(tree):
    if isinstance(tree, list):
        return [square_tree_direct(subtree) for subtree in tree]
    else:
        return tree * tree

def square_tree_map(tree):
    if isinstance(tree, list):
        return list(map(square_tree_map, tree))
    else:
        return tree * tree


tree = [1, [4, [9, 16], 25], [36, 49]]

print(square_tree_direct(tree))
print(square_tree_map(tree))