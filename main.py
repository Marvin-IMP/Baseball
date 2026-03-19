from entidades.perro import Perro
from exceptions.perro_error import PerroError
from exceptions.edad_error import EdadError
try:

    print("Ingresa el nombre del perro")
    nombre = input()

    print("Ingrese el color del perro")
    color = input()

    print("¿Comó hace este perro?")
    onomatopeya = input()

    print("Ingrece la edad")
    edad = int(input())
    
    perro = Perro(nombre,color,onomatopeya, edad)

    saludo = perro.saludar()
    print(saludo)

except ValueError:
    print("eso noooo")

except PerroError as ex:
    print(ex.mensaje)

except EdadError as ex:
    print(ex.mensaje)