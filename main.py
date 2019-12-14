from division import division
from addition import addition
from subtraction import subtraction
from multiplication import multiplication
from calculator import Calculator
from console import Console
from validators import validate_integer, validate_number_base

calculator = Calculator(division, addition, subtraction, multiplication, validate_number_base)

console = Console(calculator, validate_integer)

console.run()