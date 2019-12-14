from conversion import convert_10_to_16, convert_16_to_10, convert_to_16

def addition(x, y, base):
    #base is the base in which the addition is performed
    #x and y are the numbers to be added - they are lists
    #the function returns the result in a string
    result = ""
    carry = 0
    if len(y) > len(x):
        z = y
        y = x
        x = z
    i = 1
    while i <= len(y):
        r = int(y[len(y) - i]) + int(x[len(x) - i]) + carry
        if base == 16:
            result = convert_10_to_16(r % base) + result
        else:
            result = str(r % base) + result
        carry = r // base
        i = i + 1
    i = len(x) - len(y) - 1
    while i >= 0:
        r = x[i] + carry
        if base == 16:
            result = convert_10_to_16(r % base) + result
        else:
            result = str(r % base) + result
        carry = r // base
        i = i - 1
    if carry != 0:
        if base == 16:
            carry = convert_10_to_16(carry)
        result = str(carry) + result
    return "Result: " + result
