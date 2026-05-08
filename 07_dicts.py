### diccionarios ###

### un diccionario es una estructura de datos que almacena 
# pares de clave-valor. Es mutable, l
# lo que significa que se pueden modificar después de su creación. 
# Las claves deben ser únicas y de tipo inmutable 
# (como cadenas, números o tuplas), 
# mientras que los valores pueden ser de cualquier tipo.

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"nombre": "Saray", "apellido": "Rodríguez", "edad": 35, "profesion": "Programadora"}

my_dict = {
    "nombre": "Saray",
    "apellido": "Rodríguez",
    "edad": 35,
    "profesion": "Programadora", 
    "lenguajes": ["Python", "JavaScript", "C#"]
}

print(my_other_dict)
print(my_dict)

print(my_dict["lenguajes"])
my_dict["nombre"] = "Saray que guay"
print(my_dict["nombre"])

my_dict["pais"] = "España"
print(my_dict)

del my_dict["edad"]
print(my_dict)

print("profesion" in my_dict)
print("edad" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, "Saray")
print(my_new_dict)

my_values = my_new_dict.values()
print(dict.fromkeys(list(my_new_dict.values())))
print(tuple(my_new_dict))
print(set(my_new_dict))

