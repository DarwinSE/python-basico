# Ejercicios de Manejo de Errores y Excepciones

number_one, number_two = 5, 1
number_two = '4'

# try except

try:
    print(number_one + number_two)
    print('Se ejecuto correctamente')
except:
    # se ejecuta cuando se produce una excepcion
    print('Se ha producido un error')

# try except else finlly // else y finally son opcionales

try:
    print(number_one + number_two)
    print('Se ejecuto correctamente')
except:
    print('Se ha producido un error')
else:
    # se ejecuta si no se produce una excepcion
    print('La ejecucion continua sin problemas')
finally:
    # se ejecuta siempre
    print('La ejecucion continua')

# Excepciones por tipo

try:
    print(number_one + number_two)
    print('Se ejecuto correctamente')
except ValueError:
    print('Se ha producido un error')
except TypeError:
    print('Se ha producido un error')

# Captura de la informacion de la excepcion

try:
    print(number_one + number_two)
    print('Se ejecuto correctamente')
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)