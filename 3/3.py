# Ejercicio 3


def transformar_usuario():
    texto = input("Escribe algo: ")
    opcion = int(input("Elige (1: Mayús, 2: Minús, 3: Título): "))

    if opcion == 1:
        print(texto.upper())
    elif opcion == 2:
        print(texto.lower())
    elif opcion == 3:
        print(texto.capitalize())


print("Ejercicio 3:")
transformar_usuario()
