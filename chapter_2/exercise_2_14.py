def cons(x, y):
    return lambda m: m(x, y)

def car(z):
    return z(lambda p, q: p)

def cdr(z):
    return z(lambda p, q: q)

def make_interval(x, y):
    return cons(x, y)

def lower_bound(x):
    return car(x)

def upper_bound(x):
    return cdr(x)

def add_interval(x, y):
    return make_interval(
        lower_bound(x) + lower_bound(y),
        upper_bound(x) + upper_bound(y)
    )

def sub_interval(x, y):
    return make_interval(
        lower_bound(x) + upper_bound(y),
        upper_bound(x) + lower_bound(y)
    )

def mul_interval(x, y):
    x_low, x_high = lower_bound(x), upper_bound(x)
    y_low, y_high = lower_bound(y), upper_bound(y)

    def sign_case(low, high):
        if high < 0:
            return "neg"
        elif low > 0:
            return "pos"
        else:
            return "cross"

    case_x = sign_case(x_low, x_high)
    case_y = sign_case(y_low, y_high)

    if case_x == "pos" and case_y == "pos":
        return make_interval(x_low * y_low, x_high * y_high)

    elif case_x == "pos" and case_y == "neg":
        return make_interval(x_high * y_low, x_low * y_high)

    elif case_x == "pos" and case_y == "cross":
        return make_interval(x_high * y_low, x_high * y_high)

    elif case_x == "neg" and case_y == "pos":
        return make_interval(x_low * y_high, x_high * y_low)

    elif case_x == "neg" and case_y == "neg":
        return make_interval(x_high * y_high, x_low * y_low)

    elif case_x == "neg" and case_y == "cross":
        return make_interval(x_low * y_high, x_low * y_low)

    elif case_x == "cross" and case_y == "pos":
        return make_interval(x_low * y_high, x_high * y_high)

    elif case_x == "cross" and case_y == "neg":
        return make_interval(x_high * y_low, x_low * y_low)

    else:
        p1 = x_low * y_low
        p2 = x_low * y_high
        p3 = x_high * y_low
        p4 = x_high * y_high
        return make_interval(min(p1, p2, p3, p4),
                             max(p1, p2, p3, p4))


def div_interval(x, y):
    if lower_bound(y) <= 0 <= upper_bound(y):
        return "Division range includes zero"
    return mul_interval(
        x,
        make_interval(1 / upper_bound(y), 1 / lower_bound(y))
    )

def width(x):
    return (upper_bound(x) - lower_bound(x)) / 2

def center(x):
    return (lower_bound(x) + upper_bound(x)) / 2

def make_center_width(c, w):
    return make_interval(c - w, c + w)

def make_center_percent(c, percent):
    r = percent / 100.0
    w = abs(c) * r
    return make_center_width(c, w)

def percent(i):
    c = center(i)
    if c == 0:
        return None
    return (width(i) / abs(c)) * 100

# 100 ± 5% -> [95, 105]
r = make_center_percent(100.0, 5.0)
print("Resistor 100 ±5% ->", lower_bound(r), upper_bound(r))
print("center:", center(r), "width:", width(r), "percent:", percent(r))

# 10 ± 50 -> [-40, 60]
s = make_center_width(10, 50)
print("Interval 10 ± 50 ->", lower_bound(s), upper_bound(s))
print("center:", center(s), "width:", width(s))

def par1(r1, r2):
    return div_interval(
        mul_interval(r1, r2), add_interval(r1, r2)
    )

def par2(r1, r2):
    one = make_interval(1, 1)
    return div_interval(
        one, 
        add_interval(
            div_interval(one, r1),
            div_interval(one, r2)
        )
    )

# Resistors 100 ±5% e 200 ±5%
r1 = make_center_percent(100.0, 5.0)
r2 = make_center_percent(200.0, 5.0)

p1 = par1(r1, r2)
p2 = par2(r1, r2)

results = {
    "r1": (lower_bound(r1), upper_bound(r1)),
    "r2": (lower_bound(r2), upper_bound(r2)),
    "par1": (lower_bound(p1), upper_bound(p1), center(p1), percent(p1)),
    "par2": (lower_bound(p2), upper_bound(p2), center(p2), percent(p2)),
}

print(results)
