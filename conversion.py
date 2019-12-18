

def convert_16_to_10(a):
     #a = str
     #function that converts a digit letter to it's corresponding numeric digit
     try:
          return int(a)
     except:
          d = { 
          "0" : 0,
          "1" : 1,
          "2" : 2,
          "3" : 3,
          "4" : 4,
          "5" : 5,
          "6" : 6,
          "7" : 7,
          "8" : 8,
          "9" : 9,
          "A" : 10,
          "B" : 11,
          "C" : 12,
          "D" : 13,
          "E" : 14,
          "F" : 15
          }
          return d[a]

def convert_10_to_16(a):
     #function that converts a numeric digit to it's corresponding digit - letter
     d = { 
         0 : "0",
         1 : "1",
         2 : "2",
         3 : "3",
         4 : "4",
         5 : "5",
         6 : "6",
         7 : "7",
         8 : "8",
         9 : "9",
         10 : "A",
         11 : "B",
         12 : "C",
         13 : "D",
         14 : "E",
         15 : "F"
     }
     return d[a]

def convert_to_16(a):
    #function that converts a list 'a' which represents a list of digits in hexa to a list in decimal
    for i in range(len(a)):
        a[i] = convert_16_to_10(a[i])
        
def rapid_2_to_4(bits):
     #function that converts a group of two bits to their corresponding value in base 4
     d = {
          "00" : "0",
          "01" : "1",
          "10" : "2",
          "11" : "3"
     }
     return d[bits]

def rapid_2_to_8(bits):
     #function that converts a group of 3 bits to their corresponding value in base 8
     d = {
          "000" : "0",
          "001" : "1",
          "010" : "2",
          "011" : "3",
          "100" : "4",
          "101" : "5",
          "110" : "6",
          "111" : "7"
     }
     return d[bits]

def rapid_2_to_16(bits):
     #function that converts a group of 4 bits to their corresponding value in base 16
     d = {
          "0000" : "0",
          "0001" : "1",
          "0010" : "2",
          "0011" : "3",
          "0100" : "4",
          "0101" : "5",
          "0110" : "6",
          "0111" : "7",
          "1000" : "8",
          "1001" : "9",
          "1010" : "A",
          "1011" : "B",
          "1100" : "C",
          "1101" : "D",
          "1110" : "E",
          "1111" : "F"
     }
     return d[bits]
     
def rapid_16_to_2(digit):
     #function that converts a digit in base 16 to it's 4 bits representation in bynary
     d = {
          "0" : "0000",
          "1" : "0001",
          "2" : "0010",
          "3" : "0011",
          "4" : "0100",
          "5" : "0101",
          "6" : "0110",
          "7" : "0111",
          "8" : "1000",
          "9" : "1001",
          "A" : "1010",
          "B" : "1011",
          "C" : "1100",
          "D" : "1101",
          "E" : "1110",
          "F" : "1111"
     }
     return d[digit]

def rapid_8_to_2(digit):
     #function that converts a digit in base 8 to it's 3 bits representation in bynary
     d = {
          "0" : "000",
          "1" : "001",
          "2" : "010",
          "3" : "011",
          "4" : "100",
          "5" : "101",
          "6" : "110",
          "7" : "111"
     }
     return d[digit]

def rapid_4_to_2(digit):
     #function that converts a digit in base 4 to it's 2 bits representation in bynary
     d = {
          "0" : "00",
          "1" : "01",
          "2" : "10",
          "3" : "11"
     }
     return d[digit]