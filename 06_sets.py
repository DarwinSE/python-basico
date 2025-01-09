# Ejercicios con Sets
my_set = set()
my_other_set = {}

print(type(my_set)) # type set
print(type(my_other_set)) # type dict

my_other_set = {'Darwin', 'Guerra', 24}
print(type(my_other_set)) # type set

print(len(my_other_set))

my_other_set.add('Lawi')
print(my_other_set) # los sets no son estructuras ordenadas

my_other_set.add('Lawi')
print(my_other_set) # los sets no permiten repetidos

print('Guerra' in my_other_set)
print('Guerrero' in my_other_set)

my_other_set.remove(24)
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set # Borra toda la variable

# Al usar los sets no es recomendable transformarlo a otro tipo

my_set = {'Darwin', 'Guerra', 24}
my_other_set = {'Python', 'SQL', 'Java'}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union({'JavaScript', 'ETLs'}))

print(my_new_set.difference(my_set))