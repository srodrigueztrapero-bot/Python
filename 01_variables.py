# variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

print(my_string_variable, my_int_variable, my_bool_variable)

# concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("este es el valor de:", my_bool_variable)

# Algunas funciones de sistema
print(len(my_string_variable))  # longitud de la variable

# Variables en una sola línea, no abusar de esta práctica
name, surname, alias, age = "Saray", "Rodríguez", "Saray_asecas", 38
print("Me llamo:", name, surname, ". Mi edad es:", age, "y mi alias es:", alias)

#inputs
'''
first_name = input("What is your name? ")
age = input("What is your age? ")

print(first_name)
print(age)
'''

# Forzamos el tipo de dato de una variable
address: str = "Mi direccion"
address = 32
print(type(address))
