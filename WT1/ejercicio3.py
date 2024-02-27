""" Crea una función llamada verificar_calificacion que reciba tres
parámetros: nota1, nota2 y nota3
 Dentro de la función calcular el promedio de notas
 Si el promedio es mayor o igual a 6, entonces la función debe
retornar un mensaje “Aprobado”, en caso contrario
“Reprobado” """


def verificar_calificacion(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    if promedio >= 6:
        return "Aprobado", promedio
    else:
        return "Reprobado", promedio


nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

resultado, promedio = verificar_calificacion(nota1, nota2, nota3)
print("Resultado:", resultado)
print("Promedio:", promedio)
