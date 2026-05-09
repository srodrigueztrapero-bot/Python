### classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" # propiedad privada
        self.name = name # propiedad privada
        self.surname = surname # propiedad privada

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def walk(self):
        print(f"{self.full_name} está caminando")    

my_person = Person("Saray", "Rodriguez")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Saray", "Rodriguez", "Sarayasecas")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (el loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)