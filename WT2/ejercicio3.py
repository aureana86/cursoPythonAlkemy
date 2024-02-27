class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def trabajar(self):
        return f"{self.nombre} esta trabajando"

    def caminar(self):
        return f"{self.nombre} esta caminando despues de trabajar"


class Bicicleta:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

    def dar_vueltas(self):
        return (
            f"La bicicleta {self.color} marca "
            f"{self.marca} esta dando vueltas"
            )


# Crear instancia de Persona y Bicicleta según el enunciado
juan_lopez = Persona("Juan Lopez", 25, "Abogado")
bicicleta_juan = Bicicleta("amarilla", "Massino")

# Realizar acciones descritas en el enunciado
print(juan_lopez.trabajar())
print(juan_lopez.caminar())
print(bicicleta_juan.dar_vueltas())
