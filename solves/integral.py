def area(a, b, c):
    #achar as raizes, que serão os limites da nossa integral
    delta = b**2 - 4*a*c

    if delta >= 0:
        # Calcula as duas raízes reais
        x1 = (-b + (delta**0.5)) / (2*a)
        x2 = (-b - (delta**0.5)) / (2*a)
    else:
        return 0
    first_limit = a*(x1**3)/3 + b*x1**2/2 + c*x1
    second_limit = a*(x2**3)/3 + b*x2**2/2 + c*x2
    
    return abs(first_limit-second_limit)
