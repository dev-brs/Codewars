#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

from collections import Counter

def duplicate_encode(word):
    msg = ''
    counts = Counter(word.lower())
    for char in word:
        if counts[char.lower()] > 1:
            msg += ')'
        else:
            msg += '('
    return msg
