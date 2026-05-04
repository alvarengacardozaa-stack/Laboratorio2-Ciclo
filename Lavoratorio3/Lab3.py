# Laboratorio 3: Sistema de votación
# Estudiante: Patrick Alejandro Alvarenga Cardoza


def sistema_votacion():
    print("--- BIENVENIDO AL SISTEMA DE VOTACIÓN ---")

    votos_candidato_1 = 0
    votos_candidato_2 = 0
    votos_nulos = 0
    total_votantes = 0

    continuar = "si"

    # ITEM: USO DE WHILE PARA VOTAR
    while continuar.lower() == "si":
        print(f"\nRegistro del votante #{total_votantes + 1}")

        # ITEM: USO DE IF PARA VALIDAR EDAD
        edad = int(input("Ingrese su edad: "))

        if edad >= 18:
            print("Acceso concedido. Por favor, elija un candidato:")
            print("1. Candidato A (Renovación)")
            print("2. Candidato B (Progreso)")
            opcion = input("Ingrese el número de su elección: ")

            # ITEM: SELECT CASE (Simulado con if-elif en Python)
            if opcion == "1":
                votos_candidato_1 += 1
                print("Voto registrado por Candidato A.")
            elif opcion == "2":
                votos_candidato_2 += 1
                print("Voto registrado por Candidato B.")
            else:
                votos_nulos += 1
                print("Opción no válida. Voto registrado como Nulo.")

            total_votantes += 1
        else:
            print("Lo sentimos, debe ser mayor de 18 años para votar.")

        continuar = input("\n¿Desea registrar otro voto? (si/no): ")

    # ITEM: USO DE FOR PARA CONTAR/MOSTRAR RESULTADOS
    print("\n" + "=" * 30)
    print("RESUMEN DE RESULTADOS")
    print("=" * 30)

    resultados = [
        ("Candidato A", votos_candidato_1),
        ("Candidato B", votos_candidato_2),
        ("Votos Nulos", votos_nulos),
    ]

    for nombre, conteo in resultados:
        print(f"{nombre}: {conteo} votos")

    print(f"\nTotal de ciudadanos atendidos: {total_votantes}")


if __name__ == "__main__":
    sistema_votacion()
