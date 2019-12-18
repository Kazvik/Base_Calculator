from conversion import convert_10_to_16, convert_16_to_10, convert_to_16

def multiplication(x, y, base):
    #function that multiplies two numbers in a given base
    #x and y are the numbers - they are lists
    #y is just a single digit number
    #base is the base in which the operation will be performed
    carry = 0 #holds the carry
    result = "" #holds the result
    y = int(y[0]) #holds the digit
    i = len(x) - 1 #we iterate through the number x (the bigger one), from left to right
    while i >= 0:
        r = int(x[i]) * y + carry #hold the partial result of the current multiplication
        carry = r // base #we get the carry by performing an integer division
        #if the base is 16, we want to convert the digits like '10' to 'A' and add them to the result
        if base == 16:
            result = str(convert_10_to_16(r % base)) + result #'r%b' is the partial digit added to the result
        else:
            result = str(r % base) + result
        i = i - 1
    #if the carry is different than 0, we add him to the result too
    if carry != 0:
        if base == 16:
            carry = convert_10_to_16(carry)
        result = str(carry) + result
    #we return the string with the result
    return result