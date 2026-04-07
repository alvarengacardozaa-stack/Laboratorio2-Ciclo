# Ejercicio 5


def transformar_validando(texto, numero):
    if numero not in [1, 2, 3]:
        print("Error: opción inválida")
    else:
        if numero == 1:
            print(texto.upper())
        elif numero == 2:
            print(texto.lower())
        elif numero == 3:
            print(texto.capitalize())


# Ejemplo de uso:
print("Ejercicio 5:")
transformar_validando("Una voz silenciosa", 5)
