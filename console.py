
class Console():
    
    def __init__(self, Calculator, Validator_Integer):
        self._calculator = Calculator
        self._validate_integer = Validator_Integer
    
    @staticmethod
    def print_menu():
        print("BASE CALCULATOR:")
        print("1. Convert a number.")
        print("2. Add two numbers in a specific base.")
        print("3. Subtract two numbers in a specific base.")
        print("4. Multiply two numbers in a specific base.")
        print("5. Divide two numbers in a specific base.")
        print("6. Exit.")
    
    def ui_division(self):
        base = input("Enter the base: ")
        self._validate_integer(base)
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number (one digit): ")
        print(self._calculator.division(number1, number2, int(base)))
    
    def ui_addition(self):
        base = input("Enter the base: ")
        self._validate_integer(base)
        number1 = input("Enter the first number ")
        number2 = input("Enter the second number ")
        print(self._calculator.addition(number1, number2, int(base)))
    
    def ui_subtraction(self):
        base = input("Enter the base: ")
        self._validate_integer(base)
        number1 = input("Enter the first number ")
        number2 = input("Enter the second number ")
        print(self._calculator.subtraction(number1, number2, int(base)))
    
    def ui_multiplication(self):
        base = input("Enter the base: ")
        self._validate_integer(base)
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number (one digit): ")
        print(self._calculator.multiplication(number1, number2, int(base)))
    
    
    def run(self):
        print("AUTHOR: KOKOVICS RAZVAN-FLORIN, 914\n")
        commands = {
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
            print("\n\n")