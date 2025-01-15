# Ejercicios con Modulos

import mi_modulo

# import 10_funciones # Esta forma de llamar a un modulo no es correcta por lo tanto da error

mi_modulo.sum_value(2, 3, 5)
mi_modulo.print_value('Hola Mundo!')

from mi_modulo import sum_value, print_value

sum_value(2, 3, 5)
print_value('Hola Mundo!')

import math

print(math.sqrt(144))
print(math.pi)
print(math.isinf(math.pi))