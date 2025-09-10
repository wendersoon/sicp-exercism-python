def same_parity(*args):
    first = args[0]
    result = [first]

    if first % 2 == 0:
        for i in args[1:]:
            if i % 2 == 0:
                result.append(i)
    else:
        for i in args[1:]:
            if i % 2 != 0:
                result.append(i)

    return result


print(same_parity(1, 2, 3, 4, 5, 6, 7))
print(same_parity(2, 3, 4, 5, 6, 7))
