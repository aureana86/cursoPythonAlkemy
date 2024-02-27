class Bicicleta:
    def __init__(self, marca, color, tipo):
        self.marca = marca
        self.color = color
        self.tipo = tipo
        self.velocidad = 0

    def pedalear(self):
        self.velocidad += 5
        return f"Pedalear: Velocidad actual {self.velocidad} km/h"

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 3
            return f"Frenar: Velocidad actual {self.velocidad} km/h"
        else:
            return "La bicicleta ya está detenida"

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        return f"Color cambiado a {nuevo_color}"


# Ejemplo de uso
bicicleta_ejemplo = Bicicleta("MarcaX", "Rojo", "Montaña")
print(bicicleta_ejemplo.pedalear())
print(bicicleta_ejemplo.frenar())
print(bicicleta_ejemplo.cambiar_color("Azul"))
