# Ejercicios con Funciones

def my_function():
    print('Esto es una funcion')

my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(17, 23)
sum_two_values('17', '23')
sum_two_values(3.14, 2.89)

my_result = sum_two_values(14, 2)
print(my_result)

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(2, 3)
print(my_result)

def print_name(name, surname):
    print(f'{name} {surname}')

print_name(surname= 'Guerra', name= 'Darwin')

def print_name_with_default(name, surname, alias = 'No Alias'):
    print(f'{name} {surname} {alias}')

print_name_with_default('Darwin', 'Guerra')
print_name_with_default('Darwin', 'Guerra', 'Lawi')

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts('Elo', 'Que tar vamo', 'Lawi')
print_upper_texts('Elo')