
class Calculator():
    
    def __init__(self, division, addition, subtraction, multiplication):
        self._division = division
        self._addition = addition
        self._subtraction = subtraction
        self._multiplication = multiplication
    
    @staticmethod    
    def convert_str_to_list(number):
        return list(number)
    
    def division(self, number1, number2, base):
        number1 = self.convert_str_to_list(number1)
        return self._division(number1, number2, base)
    
    def addition(self, number1, number2, base):
        number1 = self.convert_str_to_list(number1)
        number2 = self.convert_str_to_list(number2)
        return self._addition(number1, number2, int(base))
    
    def subtraction(self, number1, number2, base):
        number1 = self.convert_str_to_list(number1)
        number2 = self.convert_str_to_list(number2)
        return self._subtraction(number1, number2, int(base))
    
    def multiplication(self, number1, number2, base):
        number1 = self.convert_str_to_list(number1)
        number2 = self.convert_str_to_list(number2)
        return self._multiplication(number1, number2, int(base))
    