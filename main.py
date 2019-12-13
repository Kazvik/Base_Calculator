from division import division
from addition import addition
from calculator import Calculator
from console import Console
from validators import validate_integer

calculator = Calculator(division, addition)

console = Console(calculator, validate_integer)

console.run()