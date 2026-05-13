### stets ###

# los sets son colecciones de elementos únicos, es decir, 
# no pueden contener elementos duplicados.

my_set =set()
print(type(my_set)) # <class 'set'>   

my_other_set = {}
print(type(my_other_set)) # <class 'dict'>

my_other_set = {"Saray", "Rodriguez", 35}
print(type(my_other_set)) # <class 'set'>

my_other_set.add("asecas")
print(my_other_set) # {'Saray', 'Rodriguez', 35, 'asecas'}

print("Rodriguezon" in my_other_set) # False, busqueda de un elemento que no existe en el set
print("Saray" in my_other_set) # True

my_other_set.remove("Saray")
print(my_other_set) # {'Rodriguez', 35, 'asecas'}

my_other_set.add(38)
print(my_other_set) # {'Rodriguez', 35, 'asecas', 38}

my_other_set.remove(35)
print(my_other_set) # {'Rodriguez', 'asecas', 38}

my_other_set.clear()
print(my_other_set) # set()

my_set = {"Saray", "Rodriguez", 35}
my_list = list(my_set)
print(my_list) # ['Saray', 'Rodriguez', 35]
print(my_list[0]) # Saray

my_other_set = {"piruleta", "chocolate", "caramelo"}

my_new_set = my_set.union(my_other_set)
print(my_new_set) # {'Saray', 'Rodriguez', 35, 'piruleta', 'chocolate', 'caramelo'}