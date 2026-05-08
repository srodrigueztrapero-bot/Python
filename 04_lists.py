### listas ###

my_list = list() # creación de una lista vacía
my_other_list = []

print(len(my_list)) # longitud de la lista

my_list = [38,40,56,23,54,12]

print(my_list) # impresión de la lista
print(len(my_list)) # longitud de la lista

my_other_list = [38, 1.54, "Saray", "Rodriguez"]
print(my_other_list) # impresión de la lista
print(my_other_list[0]) # acceso a un elemento de la lista  
print(my_list.count(38)) # cuenta el número de veces que aparece un elemento en la lista

my_other_list.append("Rubia")
print(my_other_list) # impresión de la lista con el nuevo elemento insertado

my_other_list.insert(1, "verde")
print(my_other_list) # impresión de la lista con el nuevo elemento insertado en la posición 1

my_other_list[1] = "Azul"
print(my_other_list) # impresión de la lista con el elemento en la posición 1 mod

my_other_list.remove("Saray")
print(my_other_list) # impresión de la lista con el elemento "Saray" eliminado

my_pop_element = my_list.pop(2) # elimina el elemento en la posición 2 de la lista y lo devuelve
print(my_list) # impresión de la lista con el elemento eliminado
print(my_pop_element) # impresión del elemento eliminado

del my_list[2] # elimina el elemento en la posición 2 de la lista
print(my_list) # impresión de la lista con el elemento eliminado

name,height,age,surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] # desempaquetado de la lista con más variables que elementos
print(age)


print(my_list + my_other_list) # concatenación de listas


my_new_list = my_list.copy() # copia de la lista

my_list.clear() # limpieza de la lista
print(my_list) # impresión de la lista vacía
print(my_new_list) # impresión de la lista copiada

print(my_new_list.reverse()) # reversión de la lista
print(my_new_list) # impresión de la lista reversa

my_list = "Hola Python"
print(my_list) # impresión de la lista como string
print(type(my_list)) # tipo de dato de la variable my_list































