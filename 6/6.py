# Ejercicio 6


def transformar_y_contar(texto, numero):
    # Primero transformamos
    res = ""
    if numero == 1:
        res = texto.upper()
    elif numero == 2:
        res = texto.lower()
    elif numero == 3:
        res = texto.capitalize()

    # Luego contamos
    print(f"Resultado: {res} | Caracteres: {len(res)}")


# Ejemplo de uso:
print("Ejercicio 6:")
transformar_y_contar("My Besto Friendo", 2)
