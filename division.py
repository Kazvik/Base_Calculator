from conversion import convert_16_to_10, convert_10_to_16

def division(x, y, b):
    #x is a number (list)
    #y is an single digit integer
    #b is the base; b = {1 -> 10, 16}
    i = 0
    a = 0
    rez = ""
    if b == 16:
        y = convert_16_to_10(y)
    else:
        y = int(y)
    while i < len(x):
        
        if b == 16:
            a = int(convert_16_to_10(str(a))) * b + int(x[i])
            rez = rez + str(convert_10_to_16(a // y))
            if rez == "0":
                rez = ""
            a = convert_10_to_16(a % y)
        else:
            a = int(a) * int(b) + int(x[i])
            rez = rez + str(a // y)
            if rez == "0":
                rez = ""
            a = a % y
        i = i + 1
        #print("a " + str(a))
        #print("r " + str(rez))
    return "Quotient: " + str(rez) + "\n" + "Remainder: " + str(a)

