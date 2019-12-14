def validate_integer(data):
    try:
        data = int(data)
    except:
        raise Exception("The data is not an integer.")

def validate_number_base(data, base):
    for x in data:
        if int(x) >= int(base):
            raise Exception("The number is not valid in the given base.")
            