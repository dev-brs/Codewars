def create_phone_number(numbers):
    # Check if the input array has exactly 10 elements
    if len(numbers) != 10:
        return "Invalid input: Array must contain 10 integers."

    # Format the phone number
    phone_number = "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)
    
    return phone_number