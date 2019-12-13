

from division import division
from calculator import Calculator
from console import Console

calculator = Calculator(division)

console = Console(calculator)

console.run()