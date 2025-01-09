# Ejercicios con diccionarios
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'Nombre': 'Darwin', 'Apellido': 'Guerra', 'Edad': 24, 1: 'Python'}
print(type(my_other_dict))
print(my_other_dict)

my_dict = {
    'Nombre': 'Darwin', 
    'Apellido': 'Guerra', 
    'Edad': 24, 
    'Lenguajes': {'Python', 'Java', 'JavaScript'}
    }

print(type(my_dict))
print(my_dict)
print(len(my_dict))

print(my_dict['Lenguajes'])

my_dict['Apellido'] = 'Melian'
print(my_dict)

my_dict['Calle'] = 'Mi direccion'
print(my_dict)

del my_dict['Calle']
print(my_dict)

print('Melian' in my_dict)
print('Apellido' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ['Nombre', 'Apellido']

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(('Nombre', 'Apellido'))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, 'Lawi')
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))