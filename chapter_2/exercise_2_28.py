x = [[1, 2], [3, 4]]
a = [[1, 2], [3, 4]]

def fringe(tree):
   
    if not isinstance(tree, list):
        return [tree]
    
    result = []
    for item in tree:
        result.extend(fringe(item))
    
    return result

x.append(a)
print(fringe(x))