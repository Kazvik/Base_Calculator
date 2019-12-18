from conversion import convert_10_to_16, convert_16_to_10, convert_to_16

def addition(x, y, base):
    #base is the base in which the addition is performed
    #x and y are the numbers to be added - they are lists
    #the function returns the result in a string
    result = "" #holds the result
    carry = 0 #holds the carry
    
    #if the length of y is bigger than x, we interchange them because we want to iterate the length of the smaller number first
    if len(y) > len(x):
        z = y
        y = x
        x = z
    i = 1
    #iterating through the numbers by the length of the smaller one
    while i <= len(y):
        #r hold the partial result of the current digit addition
        r = int(y[len(y) - i]) + int(x[len(x) - i]) + carry
        #if the base is 16, we want to convert digits like '10' to 'A'
        if base == 16:
            result = convert_10_to_16(r % base) + result # r % base is the digit we want to put into result
        else:
            result = str(r % base) + result
        #carry is set after an integer division between r (current result) and the base in which the operation is performed
        carry = r // base
        i = i + 1
    #then we iterate through the remaining digits of x (the bigger number)
    i = len(x) - len(y) - 1
    while i >= 0:
        #the same method is applied, but this time we add just the carry
        r = int(x[i]) + carry
        if base == 16:
            result = convert_10_to_16(r % base) + result
        else:
            result = str(r % base) + result
        carry = r // base
        i = i - 1
    #finally, if the carry is set to, we add him to the result too
    if carry != 0:
        if base == 16:
            carry = convert_10_to_16(carry)
        result = str(carry) + result
    return result
