### exceptions ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

try:
    print(numberOne + numberTwo)
    print("no se ha producido un error")
except:
    print("se ha producido un error")
else: # opcional
    print("la ejecución continúa sin problemas")
finally: # opcional
    # se ejecuta siempre, haya o no un error
    print("la ejecución continúa sin problemas")

# excecpiones por tipo

try:
    print(numberOne + numberTwo)
    print("no se ha producido un error")
except ValueError:
    print("se ha producido un error de valor")
except TypeError:
    print("se ha producido un error de tipo")

# captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("no se ha producido un error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)

