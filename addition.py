from conversion import convert_10_to_16, convert_16_to_10

def convert_to_16(a):
    #function that converts a list 'a' which represents a list of digits in hexa to a list in decimal
    for i in range(len(a)):
        a[i] = convert_16_to_10(a[i])

def addition(x, y, base):
    #base is the base in which the addition is performed
    #x and y are the numbers to be added - they are lists
    #the function returns the result in a string
    result = ""
    carry = 0
    if base == 16:
        convert_to_16(x)
        convert_to_16(y)
    if len(y) > len(x):
        z = y
        y = x
        x = z
    i = len(y) - 1
    while i >= 0:
        r = int(y[i]) + int(x[i]) + carry
        if base == 16:
            result = convert_10_to_16(r % base) + result
        else:
            result = str(r % base) + result
        carry = r // base
        i = i - 1
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
    return result

"""
x = "5677034"
y = "1234567"
x = list(x)
y = list(y)
base = 8
print(addition(x,y,base))
"""