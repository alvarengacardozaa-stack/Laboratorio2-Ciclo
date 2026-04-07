# Ejercicio 1
def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    return texto


# COMPROBACIÓN
if __name__ == "__main__":
    # Probamos las 3 variantes con un mismo texto
    print(f"Opcion 1: {transformar_texto('hola mundo', 1)}")  # Resultado: HOLA MUNDO
    print(f"Opcion 2: {transformar_texto('HOLA MUNDO', 2)}")  # Resultado: hola mundo
    print(f"Opcion 3: {transformar_texto('hola mundo', 3)}")  # Resultado: Hola mundo
