def validate_integer(data):
    #function that validates if a given data is an integer or not
    try:
        data = int(data)
    except:
        raise Exception("The data is not an integer.")

def validate_number_base(number, base):
    #function that validates a given number in a specific base
    
    #firstly we check if the base is valid: 2, 3, 4,....10, 16
    if (int(base) <= 1 or int(base) > 10) and int(base) != 16:
        raise Exception("The base is not valid.")
    #then we check if every digit of the number is smaller than the base
    for x in number:
        if int(x) >= int(base):
            raise Exception("The number is not valid in the given base.")
            