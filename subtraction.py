from conversion import convert_10_to_16, convert_16_to_10, convert_to_16

def subtraction(x, y, base):
    #function that subtracts 'y' from 'x' in a given base 'base'
    #x and y are the numbers to be added - they are lists
    #the function returns the result in a string
    carry = 0 #holds the carry, at first it is 0
    result = "" #result is empty at first
    i = 1
    while i <= len(y): #iterating the numbers from right to left as long as y (the smaller number) is
        
        #we check if we can substract without a carry
        #if we can't we set the carry to 1
        if int(x[len(x) - i]) - carry < int(y[len(y) - i]):
            r = int(x[len(x) - i]) + base - int(y[len(y) - i]) - carry
            carry = 1
        #otherwise, we substract and reinitialize the carry with 0
        else:
            r = int(x[len(x) - i]) - int(y[len(y) - i]) - carry
            carry = 0
        
        #if the base is 16, we want to convert the digits like '10' to A for example
        if base == 16:
            result = convert_10_to_16(r) + result
        else:
            result = str(r) + result
        i = i + 1
    
    #then we iterate through the remaining parts of x
    i = len(x) - len(y) - 1
    while i >= 0:
        #if we can't substract the carry, we borrow again and set the carry to 1
        if int(x[i]) - carry < 0:
            r = int(x[i]) - carry + base
            carry = 1
        #otherwise, the carry becomes 1
        else:
            r = int(x[i]) - carry
            carry = 0
            
        #if the base is 16, we want to convert the digits like '10' to A for example
        if base == 16:
            result = convert_10_to_16(r) + result
        else:
            result = str(r) + result
        i = i - 1
    #we return the result in a string
    return result

