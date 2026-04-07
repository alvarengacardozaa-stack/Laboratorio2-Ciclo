# Ejercicio 2


def mostrar_resultado(palabra, numero):
    if numero == 1:
        print(palabra.upper())
    elif numero == 2:
        print(palabra.lower())
    elif numero == 3:
        print(palabra.capitalize())


# Ejemplo de uso:
print("Ejercicio 2:")
mostrar_resultado("Zelda ocarina of time", 3)
