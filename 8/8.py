# Ejercicio 8


def programa_final():
    print("--- BIENVENIDO AL SISTEMA ---")
    txt = input("Ingrese su texto: ")
    print("1. MAYÚSCULAS\n2. minúsculas\n3. Capitalize")
    op = int(input("Seleccione opción: "))

    if op == 1:
        print(txt.upper())
    elif op == 2:
        print(txt.lower())
    elif op == 3:
        print(txt.capitalize())
    else:
        print("Esa opción no existe.")


programa_final()
