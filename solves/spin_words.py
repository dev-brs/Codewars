#https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    output = ''
    words = sentence.split()
    for word in words:
        if len(word) > 4:
            output += word[::-1]
            output += ' '
        else:
            output += word
            output += ' '
    return output.rstrip()
