from conversion import convert_to_16, rapid_2_to_16, rapid_2_to_4, rapid_2_to_8, rapid_16_to_2, rapid_8_to_2, rapid_4_to_2

class Calculator():
    
    #Calculator is in fact the Controller class.
    def __init__(self, division, addition, subtraction, multiplication, validator):
        #division - function that handles the division
        #addition - function that handles the addition
        self._division = division
        self._addition = addition
        self._subtraction = subtraction
        self._multiplication = multiplication
        self._validator = validator
    
    @staticmethod    
    def convert_str_to_list(number):
        #converts a number from a string to a list of digits
        return list(number)
    
    def division(self, number1, number2, base):
        #function that calls the division from the division.py module
        number1 = self.convert_str_to_list(number1) #number1 becomes a list
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
    
    def rapid_conversion(self, number1, source_base, destination_base):
        
        #firstly, we convert the number to bynary
        bynary_representation = ""
        if int(source_base) == 4:
            i = 0
            while i < len(number1):
                bynary_representation = bynary_representation + str(rapid_4_to_2(number1[i]))   
                i = i + 1
        elif int(source_base) == 8:
            i = 0
            while i < len(number1):
                bynary_representation = bynary_representation + str(rapid_8_to_2(number1[i]))    
                i = i + 1        
        elif int(source_base) == 16:
            i = 0
            while i < len(number1):
                bynary_representation = bynary_representation + str(rapid_16_to_2(number1[i]))
                i = i + 1
        elif int(source_base) == 2:
            i = 0
            while i < len(number1):
                bynary_representation = bynary_representation + str(number1[i])
                i = i + 1
        else:
            raise Exception("The source base is not a power of 2.")
        
        #then, we convert it's bynary representation to the destination base 
        if int(destination_base) == 16:
            group_size = 4
            function = rapid_2_to_16
        elif int(destination_base) == 8:
            group_size = 3
            function = rapid_2_to_8
        elif int(destination_base) == 4:
            group_size = 2
            function = rapid_2_to_4
        elif int(destination_base) == 2:
            while bynary_representation[0] == "0":
                bynary_representation = bynary_representation[1 : ]
            return bynary_representation  
        else:
            raise Exception("The destination base is not a power of 2.")
        
        #bynary_representation = self.convert_str_to_list(bynary_representation)
        while bynary_representation[0] == "0":
                bynary_representation = bynary_representation[1 : ]
        if len(bynary_representation) % group_size != 0:
            nr_zeros = group_size - len(bynary_representation) % group_size
            bynary_representation = "0" * nr_zeros + bynary_representation
        #print(bynary_representation)
        i = len(bynary_representation) - 1
        result = ""
        group = ""
        while i >= 0:
            for j in range(i - group_size + 1, i + 1):
                group = group + str(bynary_representation[j])
            #group = bynary_representation[i - group_size + 1 : i]
            #print(group)
            result = str(function(group)) + result 
            i = i - group_size
            group = ""
        #print(result)
        return result
                
    def successive_divisions(self, number1, source_base, destination_base):
        number1 = self.convert_str_to_list(number1)
        rez = self.division(number1, int(destination_base), int(source_base))
        result = ""
        while rez[0] != "0":
            result = str(rez[1]) + result
            if source_base == 16:
                rez = self.division(self.convert_str_to_list(rez[0]), int(destination_base), int(source_base))
            else:
                rez = self.division(self.convert_str_to_list(rez[0]), int(destination_base), int(source_base))
        result = str(rez[1]) + result
        return result
            
    def substitution_method(self, number1, source_base, destination_base):
        pass
      
    def convert_bases(self, number1, source_base, destination_base):
        number1 = self.convert_str_to_list(number1)
        if (source_base & (source_base - 1)) == 0 and (destination_base & (destination_base - 1)) == 0:
            return self.rapid_conversion(number1, source_base, destination_base)
        elif source_base > destination_base:
            return self.successive_divisions(number1, source_base, destination_base)
        elif destination_base > source_base:
            return self.substitution_method(number1, source_base, destination_base)
        else:
            raise Exception("The given bases are the same!")
            
            