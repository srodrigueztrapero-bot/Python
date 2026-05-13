### tuples ###

my_tuple = tuple() # creación de una tupla vacía
my_other_tuple = ()

my_tuple = (38, 1.54, "Saray", "Rodriguez")
print(my_tuple) # impresión de la tupla

my_other_tuple = (38, 40, 56, 23, 54, 12)
print(my_other_tuple) # impresión de la tupla

print(my_tuple[0]) # acceso a un elemento de la tupla
print(my_tuple[3])

print(my_tuple.count("Saray")) # cuenta el número de veces que aparece un elemento en la tupla
print(my_tuple.index("Saray")) # devuelve la posición del primer elemento que coincide con el valor especificado

### my_tuple[1] = 1.55 # error, las tuplas son inmutables

my_sum_tuple = my_tuple + my_other_tuple # concatenación de tuplas  
print(my_sum_tuple) # impresión de la tupla resultante

print(my_sum_tuple[3:6]) # slicing de la lista convertida a tupla

## las tuplas no son mutables, pero se pueden convertir a listas para modificar su contenido

my_tuple = list(my_tuple) # conversión de tupla a lista
print(type(my_tuple)) # tipo de dato de la variable my_tuple

my_tuple[1] = 1.55 # modificación de un elemento de la lista
my_tuple.insert(4, "Rubia") # inserción de un elemento en la lista
print(tuple(my_tuple)) # impresión de la lista convertida a tupla

### se puede realizar un del my_tuple para eliminar la variable my_tuple, 
### pero no se puede eliminar un elemento de la tupla directamente ###


