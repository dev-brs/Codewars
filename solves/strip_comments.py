#https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def strip_comments(strng, markers):
    strings = strng.split('\n')
    output_strings = []

    for string in strings:
        index_to_strip = len(string)
        for marker in markers:
            marker_index = string.find(marker)
            if marker_index != -1 and marker_index < index_to_strip:
                index_to_strip = marker_index

        output_strings.append(string[:index_to_strip].rstrip())

    result = '\n'.join(output_strings)

    if strng.endswith('\n'):
        result += '\n'

    return result
