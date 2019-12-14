from conversion import convert_10_to_16, convert_16_to_10, convert_to_16

def multiplication(x, y, base):
    
    carry = 0
    result = ""
    y = int(y[0])
    i = len(x) - 1
    while i >= 0:
        r = int(x[i]) * y + carry
        carry = r // base
        if base == 16:
            result = str(convert_10_to_16(r % base)) + result
        else:
            result = str(r % base) + result
        i = i - 1
    if carry != 0:
        result = str(carry) + result
    return "Result: " + result