
class Console():
    
    def __init__(self, Calculator):
        self._calculator = Calculator
    
    @staticmethod
    def print_menu():
        print("BASE CALCULATOR:")
        print("1. Convert a number.")
        print("2. Add two numbers in a specific base.")
        print("3. Subtract two numbers in a specific base.")
        print("4. Multiply two numbers in a specific base.")
        print("5. Divide two numbers in a specific base.")
    
    def ui_division(self):
        base = input("Enter the base: ")
        base = validate_integer
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")
        print(self._calculator.division(number1, number2, base))
    
    def run(self):
        
        commands = {
            "5" : self.ui_division
        }
        while True: 
            self.print_menu()
            cmd = input("Enter option: ")
            try:
                if cmd not in commands:
                    raise Exception("Command not found!")
                commands[cmd]()
            except Exception as ex:
                print(str(ex))