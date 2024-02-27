class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        return "Estoy comiendo"


class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza

    def correr(self):
        return "Estoy corriendo"


# La clase Águila hereda directamente de Animal
class Águila(Animal):
    def volar(self):
        return "Estoy volando"


# Ejemplo de uso
animal_ejemplo = Animal(4, "Vertebrado")
print(animal_ejemplo.comer())

perro_ejemplo = Perro(4, "Vertebrado", "Max", "Labrador")
print(perro_ejemplo.comer())
print(perro_ejemplo.correr())

águila_ejemplo = Águila(2, "Vertebrado")
print(águila_ejemplo.comer())
print(águila_ejemplo.volar())
