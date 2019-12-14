from conversion import convert_to_16

class Calculator():
    
    def __init__(self, division, addition, subtraction, multiplication, validator):
        self._division = division
        self._addition = addition
        self._subtraction = subtraction
        self._multiplication = multiplication
        self._validator = validator
    
    @staticmethod    
    def convert_str_to_list(number):
        return list(number)
    
    def division(self, number1, number2, base):
        number1 = self.convert_str_to_list(number1)
        if int(base) == 16:
            convert_to_16(number1)
        self._validator(number1, base)
        return self._division(number1, number2, base)
    
    def addition(self, number1, number2, base):
        number1 = self.convert_str_to_list(number1)
        number2 = self.convert_str_to_list(number2)
        if int(base) == 16:
            convert_to_16(number1)
            convert_to_16(number2)
        self._validator(number1, base)
        self._validator(number2, base)
        return self._addition(number1, number2, int(base))
    
    def subtraction(self, number1, number2, base):
        number1 = self.convert_str_to_list(number1)
        number2 = self.convert_str_to_list(number2)
        if int(base) == 16:
            convert_to_16(number1)
            convert_to_16(number2)
        self._validator(number1, base)
        self._validator(number2, base)
        return self._subtraction(number1, number2, int(base))
    
    def multiplication(self, number1, number2, base):
        number1 = self.convert_str_to_list(number1)
        number2 = self.convert_str_to_list(number2)
        if int(base) == 16:
            convert_to_16(number1)
            convert_to_16(number2)
        self._validator(number1, base)
        self._validator(number2, base)
        return self._multiplication(number1, number2, int(base))
    