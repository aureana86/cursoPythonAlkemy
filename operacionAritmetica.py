def funcion_aritmetica(opcion, num1, num2):
    if opcion == 1:
        result = num1 + num2
        return result
    elif opcion == 2:
        result = num1 - num2
        return result
    elif opcion == 3:
        result = num1 * num2
        return result
    elif opcion == 4:
        if num2 == 0:
            return "Error: La division por 0 no esta permitida."
        result = num1 / num2
        return result
    else:
        return "Opcion Invalida.Por favor elige entre las opciones 1,2, 3 o 4."


print("Bienvenidos!!")

while True:
    opcion = int(input(
        "\nPor favor elige una opcion:\n"
        "1: Suma\n 2: Resta\n 3: Multiplicacion\n 4: Division\n"
    ))
    if opcion in [1, 2, 3, 4]:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        result = funcion_aritmetica(opcion, num1, num2)
        print(f"El resultado de la operacion es: {result}")

        continuar = input("¿Desea realizar otra operacion? (Si/No): ").lower()
        if continuar != 'si':
            break
    else:
        print("Opcion Invalida. Intentelo nuevamente.")

print("Gracias por usar el programa. ¡Hasta luego!")
