""" Crear un algoritmo para calcular la sumatoria de los primeros cien
números (del 01 al 100) con un ciclo while. """

sumatoria = 0
contador = 1
while contador <= 100:
    sumatoria += contador
    contador += 1

print("La sumatoria de los primeros cien numeros es:", sumatoria)
