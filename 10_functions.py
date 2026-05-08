### Functions ###

def my_function():
    print("Esto es una función")

my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(1038, 8815)
sum_two_values("5", "7")
sum_two_values(1.5, 2.5)

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(name = "Saray", surname = "Rodríguez")

def print_name_with_default(name, surname, alias="sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default( "Saray", "Rodríguez")

def print_upper_text(*texts):
    for text in texts:
        print(text.upper())

print_upper_text("hola", "python", "que tal")
print_upper_text("hola")