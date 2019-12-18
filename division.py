from conversion import convert_16_to_10, convert_10_to_16

def division(x, y, b):
    #function that divides x (number) to y (digit) in a given base (b)
    #x is a number (list)
    #y is an single digit integer
    #b is the base; b = {1 -> 10, 16}
    remainder = 0 #holds the reaminder
    rez = "" #holds the result
    #if the base is 16, we want to convert the letter y to y it's corresponding digit
    if b == 16:
        y = convert_16_to_10(str(y))
    else:
        y = int(y)
    i = 0
    #we iterate through the number x from left to right
    while i < len(x):
        #if the base is 16, we want to take care of the digit - letters
        if b == 16:
            remainder = int(convert_16_to_10(str(remainder))) * b + int(x[i]) #a it's the current result of the partial multiplication
            rez = rez + str(convert_10_to_16(remainder // y)) #we divide a to y an obtain an integer which we add it to the result
            if rez == "0":
                rez = "" #if result is 0, we make it empty
            remainder = convert_10_to_16(remainder % y) #we set the remainder
        else:
            #if the base is not 16, we maintain the same algorithm but without handling digit - letters
            remainder = int(remainder) * int(b) + int(x[i])
            rez = rez + str(remainder // y)
            if rez == "0":
                rez = ""
            remainder = remainder % y
        i = i + 1
    #if the result is empty, we make it 0
    y = convert_10_to_16(y)
    if rez == "":
        rez = "0"
    #we return a list which contains the quotinet(result) and the remainder
    l = [rez, remainder]
    return l
    #return "Quotient: " + str(rez) + "\n" + "Remainder: " + str(a)

