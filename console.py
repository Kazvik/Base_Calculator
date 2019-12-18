
class Console():
    
    #Console is in fact the UI of the program.
    def __init__(self, Calculator, Validator_Integer):
        #function that initializes the Console
        #Calculator = Calculator object type, here are the main functions = SERVICE LAYER
        #Validator_Integer = a function that verifies if a given string can be converted to an integer.
        self._calculator = Calculator
        self._validate_integer = Validator_Integer
    
    @staticmethod
    def print_menu():
        #function that prints the menu on the screen
        print("BASE CALCULATOR:")
        print("1. Convert a number.")
        print("2. Add two numbers in a specific base.")
        print("3. Subtract two numbers in a specific base.")
        print("4. Multiply two numbers in a specific base.")
        print("5. Divide two numbers in a specific base.")
        print("6. Exit.")
    
    def ui_division(self):
        #function that handles input and output of the division
        base = input("Enter the base: ")
        self._validate_integer(base) #check if the base is an integer or not
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number (one digit): ")
        rez = self._calculator.division(number1, number2, int(base)) #calling the division function from Calculator
        print("Quotient: " + str(rez[0]) + ", Remainder: " + str(rez[1])) #printing the result on the screen
    
    def ui_addition(self):
        #function that handles input and output of the addition
        base = input("Enter the base: ")
        self._validate_integer(base) #check if the base is an integer or not
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")
        print("Result: " + self._calculator.addition(number1, number2, int(base))) #printing and calling the result from the addition on the screen
    
    def ui_subtraction(self):
        #function that handles input and output of the subtraction
        base = input("Enter the base: ")
        self._validate_integer(base) #check if the base is an integer or not
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")
        print("Result: " + self._calculator.subtraction(number1, number2, int(base)))#printing and calling the result from the subtraction on the screen
    
    def ui_multiplication(self):
        #function that handles input and output of the multiplication
        base = input("Enter the base: ")
        self._validate_integer(base) #checks if the base is an integer or not
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number (one digit): ")
        print("Result: " + self._calculator.multiplication(number1, number2, int(base)))#printing and calling the result from the multiplication on the screen
    
    def ui_convert(self):
        #function that handles the data from a conversion
        source_base = input("Enter source base: ")
        self._validate_integer(source_base) #checks if the source base is an integer
        number = input("Enter the number: ")
        destination_base = input("Enter the destination base: ")
        self._validate_integer(destination_base) #checks if the destination base is an integer
        print(self._calculator.convert_bases(number, int(source_base), int(destination_base)))
    
    def run(self):
        #the run function 
        print("AUTHOR: KOKOVICS RAZVAN-FLORIN, 914\n")
        commands = {
            "1" : self.ui_convert,
            "2" : self.ui_addition,
            "3" : self.ui_subtraction,
            "4" : self.ui_multiplication,
            "5" : self.ui_division
        }
        while True: 
            self.print_menu()
            cmd = input("Enter option: ")
            if cmd == "6":
                break
            try:
                if cmd not in commands:
                    raise Exception("Command not found!")
                commands[cmd]()
            except Exception as ex:
                print(str(ex))
            print("\n")