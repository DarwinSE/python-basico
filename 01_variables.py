# Introduccion a variables

my_variable = 'My variable string'
print(my_variable)

int_variable = 14
print(int_variable)

bool_variable = False
print(bool_variable)

# Concatenacion de variables
print(my_variable, int_variable, bool_variable)
print('Todo lo que te dice es', bool_variable)

print(str(int_variable))
print(type(str(int_variable)))

# Variables en una linea
name,surname, alias, age = 'Darwin', 'Guerra', 'Lawi', 24 # Se puede hacer pero es mala praxis
print('Me llamo:', name, surname, ', Tengo:', age, 'de Edad y me dicen', alias)

# Ejemplo de inputs
"""
your_name = input('Cual es tu nombre? ')
your_age = input('Cual es tu edad? ')

print('Tu nombre es:', your_name, ', y tienes', your_age, 'años')
"""

# Cambiamos tipos
name = 54
age = 'Hola'

print(name)
print(age)

# Le asignamos un tipo a una variable?
address: str = 'Mi direccion'
address = 25

print(type(address))