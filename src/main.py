from taxonomia.clasificador_taxonomia import clasificar_taxonomia

def main():

    print("=" * 40)
    print("ASISTENTE SOPORTE TI HIBRIDO")
    print("=" * 40)

    consulta = input("Ingrese una consulta: ")

    categoria = clasificar_taxonomia(consulta)

    print("\n--- RESULTADO ---")
    print("Consulta:", consulta)
    print("Categoria IA:", categoria)


if __name__ == "__main__":
    main()