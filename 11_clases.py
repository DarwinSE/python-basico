# Ejercicios con Clases

class EmptyPerson:
    pass

print(EmptyPerson)

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

my_person = Person('Darwin', 'Guerra')
print(f'{my_person.name} {my_person.surname}')

class PersonV2:
    def __init__(self, name, surname, alias = 'No Alias'):
        self.full_name = f'{name} {surname} ({alias})' # Propiedades publicas modificables
        self.__name = name # Propiedades privadas inmodificables
        self.__surname = surname

    def get_name(self):
        return self.__name
    
    def get_surname(self):
        return self.__surname

    def walk(self):
        print(f'{self.full_name} esta caminando')

my_person = PersonV2('Darwin', 'Guerra')
print(my_person.full_name)
my_person.walk()

print(my_person.get_name())
print(my_person.get_surname())

my_other_person = PersonV2('Cri', 'Gri', 'Creesgreen')
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = 123
print(my_other_person.full_name)