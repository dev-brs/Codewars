#https://www.codewars.com/kata/584d05422609c8890f0000be

from math import factorial
from functools import reduce

def proc_arr(arr):
    output = []
    sorted_arr = sorted(arr)
    output.append(factorial(len(arr)) // reduce(lambda x, y: x * factorial(arr.count(y)), set(arr), 1))
    output.append(int(''.join(sorted_arr).lstrip("0")))
    output.append(int(''.join(sorted_arr[::-1])))

    return output