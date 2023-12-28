#https://www.codewars.com/kata/58ad317d1541651a740000c5

from itertools import permutations
import math

def middle_permutation(string):
    length = len(string)
    total_permutations = math.factorial(length)

    if total_permutations % 2 == 0:
        index = total_permutations // 2 - 1
    else:
        index = total_permutations // 2

    result = ''
    chars = sorted(list(string))
    for i in range(length):
        total_permutations //= length - i
        current_index = index // total_permutations
        result += chars.pop(current_index)
        index %= total_permutations

    return result