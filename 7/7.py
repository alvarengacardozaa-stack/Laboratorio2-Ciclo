# Ejercicio 7


def aplicar_varios(texto, lista_numeros):
    resultado = texto
    for n in lista_numeros:
        if n == 1:
            resultado = resultado.upper()
        elif n == 2:
            resultado = resultado.lower()
        elif n == 3:
            resultado = resultado.capitalize()
    return resultado


# Ejemplo de uso:
# Primero lo hace mayúsculas, luego lo hace minúsculas, luego capitaliza.
print("Ejercicio 7:", aplicar_varios("HOLA", [1, 2, 3]))
