def for_each(proc, items):
    if not items:
        return True
    else:
        proc(items[0])        
        return for_each(proc, items[1:])

for_each(lambda x: print(x), [57, 321, 88])
