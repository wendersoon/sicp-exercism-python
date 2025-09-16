def make_mobile(left, right):
    return [left, right]

def make_branch(length, structure):
    return [length, structure]


# A

def left_branch(x):
    return x[0]

def right_branch(x):
    return x[1]

def branch_length(x):
    return x[0]

def branch_structure(x):
    return x[1]

# B
def total_weight(struct):

    if not isinstance(struct, list):
        return 0
    elif not isinstance(struct[0], list) and not isinstance(struct[1], list):
        return struct[1]
    total = 0
    for i in struct:
        total += total_weight(i)
    return total

simple_mobile = make_mobile(make_branch(10, 5),  make_branch(5, 10))
submobile1 = make_mobile(make_branch(2, 3), make_branch(3, 2))
complex_mobile = make_mobile(make_branch(4, submobile1), make_branch(10, 2))

print(total_weight(simple_mobile))
print(total_weight(complex_mobile))


# C

def is_mobile(structure):
    return isinstance(structure, list) and len(structure) == 2 and isinstance(structure[0], list)

def is_balanced(mobile):
    if not is_mobile(mobile):
        return True
    
    left = left_branch(mobile)
    right = right_branch(mobile)
    
    left_length = branch_length(left)
    right_length = branch_length(right)
    left_structure = branch_structure(left)
    right_structure = branch_structure(right)
    
    left_weight = total_weight(left_structure)
    right_weight = total_weight(right_structure)
    left_torque = left_length * left_weight
    right_torque = right_length * right_weight
    
    return (left_torque == right_torque and 
            is_balanced(left_structure) and 
            is_balanced(right_structure))

print(is_balanced(simple_mobile))
print(is_balanced(complex_mobile))