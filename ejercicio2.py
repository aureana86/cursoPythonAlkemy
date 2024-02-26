""" Crear una lista con 5 elementos y luego aplica los siguientes
accionables:
Imprimir el último elemento
Modificar el valor del tercer elemento
Agregar dos elementos
Eliminar algún elemento """


mis_frutas = ['banana', 'manzana', 'cereza', 'durazno', 'frutilla']
print(mis_frutas)

# Imprimir el último elemento
print("Ultimo elemento:", mis_frutas[-1])

# Modificar el valor del tercer elemento
mis_frutas[2] = 'melon'

# Agregar dos elementos
mis_frutas.append('sandia')
mis_frutas.append('pera')

# Eliminar algún elemento (por ejemplo, el segundo elemento)
elemento_eliminado = mis_frutas.pop(1)

# Imprimir la lista actualizada
print("Lista despues de las acciones:")
print(mis_frutas)

# Imprimir el elemento eliminado
print("Elemento eliminado:", elemento_eliminado)
