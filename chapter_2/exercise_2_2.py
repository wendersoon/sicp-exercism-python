def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def cons(x, y):
    return [x, y]

def car(obj):
    return obj[0]

def cdr(obj):
    return obj[1]    


# Point
def make_point(x_cord, y_cord):
    return cons(x_cord, y_cord)

def x_point(point):
    return car(point)

def y_point(point):
    return cdr(point)

# Segment
def make_segment(start_point, end_point):
    return cons(start_point, end_point)

def start_segment(segment):
    return car(segment)

def end_segment(segment):
    return cdr(segment)


def midpoint_segment(segment):
    
    point_x = (x_point(start_segment(segment)) + x_point(end_segment(segment))) / 2
    point_y = (y_point(start_segment(segment)) + y_point(end_segment(segment))) / 2
    
    return make_point(point_x, point_y)


start_point = make_point(2, 5)
end_point = make_point(6, 7)

segment = make_segment(start_point, end_point)

print(midpoint_segment(segment))
