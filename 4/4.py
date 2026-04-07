# Ejercicio 4


def transformar_lista(lista, numero):
    nueva_lista = []
    for item in lista:
        if numero == 1:
            nueva_lista.append(item.upper())
        elif numero == 2:
            nueva_lista.append(item.lower())
        elif numero == 3:
            nueva_lista.append(item.capitalize())
    return nueva_lista


lista = ["LUZ", "oscuridad", "grises"]
print("Ejercicio 4:", transformar_lista(lista, 1))
