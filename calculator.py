
class Calculator():
    
    def __init__(self, division):
        self._division = division
    
    @staticmethod    
    def convert_str_to_list(number):
        return list(number)
    
    def division(self, number1, number2, base):
        number1 = self.convert_str_to_list(number1)
        return self._division(number1, number2, base)
        