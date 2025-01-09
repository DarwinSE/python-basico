# Ejercicios de bucles

# while
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print('Mi condicion es mayor o igual a 10')

print('La ejecucion continua')    

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('Se detiene la ejecucion')
        break    
    print(my_condition)

print('La ejecucion continua')

# for
my_list = [21, 34, 54, 22, 32, 44, 32, 19]

for element in my_list:
    print(element)

my_tuple = (24, 1.72, 'Darwin', 'Guerra')

for element in my_tuple:
    print(element)

my_set = {'Darwin', 'Guerra', 24}

for element in my_set:
    print(element)

my_dict = {'Nombre': 'Darwin', 'Apellido': 'Guerra', 'Edad': 24, 1: 'Python'}

for element in my_dict:
    print(element)
    if element == 'Edad':
        print('El elemento Edad no es valido')
        break
else:
    print('El bucle para mi dicccionario ha terminado')

print('La ejecucion continua')

for element in my_dict:
    print(element)
    if element == 'Edad':
        continue
    print('Se ejecuta')
else:
    print('El bucle para mi dicccionario ha terminado')