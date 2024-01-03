#https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))

    result = '{:02X}{:02X}{:02X}'.format(r, g, b)
    
    return result
