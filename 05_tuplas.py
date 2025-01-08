# Ejercicios de Tuplas
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (24, 1.72, 'Darwin', 'Guerra')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count(24))
print(my_tuple.index('Guerra'))

# my_tuple[1] = 1.75
# A diferencia de las listas, las tuplas son constantes

my_other_tuple = (32, 24, 43)

my_mixed_tuple = my_tuple + my_other_tuple
print(my_mixed_tuple)
print(my_mixed_tuple[3:5])

del my_tuple
# print(my_tuple) borra la tupla completa