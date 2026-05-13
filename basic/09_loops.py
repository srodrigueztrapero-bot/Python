### loops ###

# while

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("mi condición es mayor o igual a 10")

print("la ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("se detiene la ejecución")
        break
        
    print(my_condition)

print("la ejecución continúa")

# for
# sirve para iterar sobre un una secuencia de elementos

my_list = [38,40,56,23,54,12]

for element in my_list:
    print(element)

my_dict = {
    "nombre": "Saray",
    "apellido": "Rodríguez",
    "edad": 35,
    "profesion": "Programadora", 
    "lenguajes": ["Python", "JavaScript", "C#"]
}

for element in my_dict:
    print(element)
    if element == "edad":
        print("se detiene la ejecución")
        break

else:
    print("el bucle for para mi diccionario ha finalizado")

print("la ejecución continúa")

for element in my_dict:
    print(element)
    if element == "edad":
        print("se detiene la ejecución")
        continue

else:
    print("el bucle for para mi diccionario ha finalizado")


