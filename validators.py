def validate_integer(data):
    try:
        data = int(data)
    except:
        raise Exception("The data is not an integer.")