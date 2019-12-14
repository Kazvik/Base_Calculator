from conversion import convert_10_to_16, convert_16_to_10, convert_to_16

def subtraction(x, y, base):
    #function that subtracts y from x in a given base 'base'
    #x and y are the numbers to be added - they are lists
    #the function returns the result in a string
    carry = 0
    result = ""
    i = 1
    while i <= len(y):
        if int(x[len(x) - i]) - carry < int(y[len(y) - i]):
            r = int(x[len(x) - i]) + base - int(y[len(y) - i]) - carry
            carry = 1
        else:
            r = int(x[len(x) - i]) - int(y[len(y) - i]) - carry
            carry = 0
        if base == 16:
            result = convert_10_to_16(r) + result
        else:
            result = str(r) + result
        i = i + 1
    i = len(x) - len(y) - 1
    while i >= 0:
        if int(x[i]) - carry < 0:
            r = int(x[i]) - carry + base
            carry = 1
        else:
            r = int(x[i]) - carry
            carry = 0
        if base == 16:
            result = convert_10_to_16(r) + result
        else:
            result = str(r) + result
        i = i - 1
    return "Result: " + result

