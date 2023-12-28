#https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def solution(s):
    pairs = []
    msg = ''
    for char in s:
        msg += char
        if(len(msg)>1):
            pairs.append(msg)
            msg = ''
    if len(msg) == 1:
        msg += '_'
        pairs.append(msg)
    return pairs