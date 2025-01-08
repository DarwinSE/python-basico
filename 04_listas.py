# Ejercicios con Listas
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [21, 34, 54, 22, 32, 44, 32, 19]
print(my_list)
print(len(my_list))

my_other_list = [24, 1.72, 'Darwin', 'Guerra']

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

print(my_list.count(32))

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)

my_other_list.append('Lawi')
print(my_other_list)

my_other_list.insert(1, 'Mi direccion')
print(my_other_list)

my_other_list[1] = 'Mi direccion cambiada'
print(my_other_list)

my_other_list.remove('Mi direccion cambiada')
print(my_other_list)

my_list.pop()
my_list_pop = my_list.pop(2)
print(my_list_pop)
print(my_list)

my_list_changed = my_list.copy()
print(my_list_changed)

my_list_changed.reverse()
print(my_list_changed)

my_list_changed.sort()
print(my_list_changed)

my_list.clear()
print(my_list)