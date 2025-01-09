# Ejercicios de condicionales

my_condition = False

if my_condition: # Es lo mismo que escribir if my_condition == True:
    print('Se ejecuta la condicion')

my_condition = 5 ** 0

if my_condition > 10 and my_condition < 20:
    print('Es mayor que 10 y menor que 20')
elif my_condition == 1:
    print('Es igual a 1')    
else:
    print('Es menor o igual que 10 o mayor o igual que 20 o distinto de 1')

print('La ejecucion continua')

my_string = ''

if not my_string:
    print('Mi cadena de texto es vacia')

if my_string == 'AAAAAAAAAA':
    print('Mis cadenas de texto coinciden')