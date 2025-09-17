def subsets(s):
    if not s:
        return [[]]

    rest = subsets(s[1:])
    return rest + [ [s[0]] + x for x in rest ]

a = [1, 2, 3]
print(subsets(a))
