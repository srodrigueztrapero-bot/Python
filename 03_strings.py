### strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string)) # longitud del string
print(len(my_other_string))

print(my_string + " " + my_other_string) # concatenación de strings

my_new_line_string = "Este es un string\ncon un salto de línea"
print(my_new_line_string) # impresión del string con salto de línea

my_tab_string = "Este es un string con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un string\\n escapado"
print(my_scape_string)

### formateo de strings ###

name, surname, age = "Saray", "Rodriguez", 38

print("Mi nombre es {} {} y tengo {} años".format(name, surname, age))
print(f"Mi nombre es {name} {surname} y tengo {age} años")

### desempaquetado de caracteres ###
Language = "Python"
a, b, c, d, e, f = Language
print(a)
print(e)

### división de strings ###

language_slice = Language[1:3] # slice de string
print(language_slice)

language_slice = Language[1:] # slice de string
print(language_slice)

language_slice = Language[0:6:2] # slice de string
print(language_slice)

### reversión de strings ###

reversed_language = Language[::-1] # reversión de string
print(reversed_language)

### funciones de strings ###

print(Language.capitalize()) # primera letra en mayúscula
print(Language.upper()) # todas las letras en mayúscula
print(Language.count("o")) # cuenta el número de veces que aparece un carácter
print(Language.isnumeric()) # verifica si el string es numérico
print(Language.lower()) # todas las letras en minúscula
print(Language.lower().isupper()) # verifica si el string es mayúscula
print(Language.startswith("Py")) # verifica si el string empieza con un prefijo