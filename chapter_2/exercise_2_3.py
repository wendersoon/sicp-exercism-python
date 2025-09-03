import math

def cons(x, y):
    return [x, y]

def car(obj):
    return obj[0]

def cdr(obj):
    return obj[1]    

def square(x):
    return x * x

def root(x):
    return math.sqrt(x)


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

def distance_segment(segment):
    return root(
        square(
            x_point(end_segment(segment)) - x_point(start_segment(segment))
        ) + 
        square(
            y_point(end_segment(segment)) - y_point(start_segment(segment))
        )
    )

# Rectangle
def make_rectangle(segment_base, segment_height):
    return cons(segment_base, segment_height)

def base_segment(rectangle):
    return distance_segment(car(rectangle))

def height_segment(rectangle):
    return distance_segment(cdr(rectangle))

def perimeter(rectangle):
    return (2 * base_segment(rectangle)) + (2 * height_segment(rectangle))

def area(rectangle):
    return base_segment(rectangle) * height_segment(rectangle)


point1 = make_point(0, 0)
point2 = make_point(5, 0)
point3 = make_point(5, 5)

segment_base = make_segment(point1, point2)
segment_height = make_segment(point2, point3)

rectangle = make_rectangle(segment_base, segment_height)

print(perimeter(rectangle))
print(area(rectangle))

"""
To be possible for any rectangle it will be necessary to implement 
notions of vectors and time does not allow me

"""