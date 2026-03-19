from exceptions.perro_error import PerroError
from exceptions.edad_error import EdadError
class Perro:

    def __init__(self, nombre: str, color: str, onomatopeya: str, edad: int):
        self.nombre = nombre
        self.color = color
        self.onomatopeya = onomatopeya
        self.edad = edad

    def saludar(self):
        if self.onomatopeya != "guau":
            raise PerroError("Esto no es un perro")
        if self.edad > 20:
            raise EdadError ("Este perro ya se va a morir")
        
        return f"Hola,{self.nombre}, so un perro guau"