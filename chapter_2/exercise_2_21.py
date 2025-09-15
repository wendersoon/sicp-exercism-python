def square_list(items):
    if not items:
        return []
    else:
        return [items[0] ** 2] + square_list(items[1:])

def square_list_map(items):
    return list(map(lambda x: x**2, items))

print(square_list([1, 2, 3, 4]))
print(square_list_map([1, 2, 3, 4]))  
