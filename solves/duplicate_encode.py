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
