#https://www.codewars.com/kata/537baa6f8f4b300b5900106c

from math import pi

def circle_area(r):
    if r <= 0:
        raise ValueError
    return pi*r*r
