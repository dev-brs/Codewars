#https://www.codewars.com/kata/525f50e3b73515a6db000b83

def create_phone_number(numbers):
    if len(numbers) != 10:
        return "Invalid input: Array must contain 10 integers."

    phone_number = "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)
    
    return phone_number