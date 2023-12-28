from math import pi
def circle_area(r):
    if r <= 0:
        raise ValueError
    return pi*r*r
