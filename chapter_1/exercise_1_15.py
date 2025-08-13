def cube(x):
    return x * x * x

def p(x):
    return (3 * x) - (4 * cube(x))

def sine(angle, step):
    print(f"{step}: {angle}")
    if not abs(angle) > 0.1:
        return angle
    else:
        return p(sine(angle/3.0, step+1)) 
    
# a
print(sine(12.15, 1))

# b Theta(log(as))