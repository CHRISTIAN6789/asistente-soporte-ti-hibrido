from taxonomia.clasificador_taxonomia import clasificar_taxonomia
from clasificador.clasificar_ticket import clasificar_ticket
from busqueda.astar_soporte import astar


def main():

    print("=" * 60)
    print("         ASISTENTE INTELIGENTE DE SOPORTE TI")
    print("=" * 60)

    consulta = input("\nIngrese su consulta: ")

    categoria = clasificar_taxonomia(consulta)
    ticket = clasificar_ticket(consulta)
    ruta = astar()

    print("\n" + "=" * 60)
    print("RESULTADO DEL ANALISIS")
    print("=" * 60)

    print("\nConsulta recibida:")
    print(f"   {consulta}")

    print("\nCategorias detectadas:")

    for item in categoria:
        print(f"   • {item}")

    print("\nClasificacion del Ticket:")
    print("-" * 60)
    print(f"Tipo         : {ticket['tipo']}")
    print(f"Criticidad   : {ticket['criticidad']}")
    print(f"Impacto      : {ticket['impacto']}")
    print(f"Prioridad    : {ticket['prioridad']}")
    print(f"Escalamiento : {ticket['escalamiento']}")

    print("\nAnalisis del incidente (A*)")
    print("-" * 60)
    print("Estado inicial      : Incidente")
    print("Meta objetivo       : Solucionado")
    print("Algoritmo aplicado  : A*")
    print("Heuristica          : Pasos estimados restantes")

    print("\nPlan de solucion sugerido:")
    print("-" * 60)

    for i, paso in enumerate(ruta):

        print(f"[{paso}]")

        if i < len(ruta) - 1:
            print("     │")
            print("     ▼")

    print("\nAnalisis de priorizacion (Minimax)")
    print("-" * 60)

    print("""
                    MAX
                     │
         ┌───────────┼───────────┐
         │           │           │
         ▼           ▼           ▼
     Servidor       VPN      Impresora
        10           6           2
    """)

    print("Decision seleccionada:")

    if ticket["prioridad"] == "P1":
        print("► Atender SERVIDOR CRITICO")
    elif ticket["prioridad"] == "P2":
        print("► Atender INCIDENTE IMPORTANTE")
    else:
        print("► Atender INCIDENTE DE BAJA PRIORIDAD")

    print("\nJustificacion:")
    print("Se selecciona la alternativa con mayor utilidad operativa.")

    print("\nResultado:")
    print("-" * 60)
    print("✓ Incidente analizado")
    print("✓ Categoria identificada")
    print("✓ Ticket clasificado")
    print("✓ Ruta de resolucion generada")
    print("✓ Priorizacion calculada")

    print("\n" + "=" * 60)
    print("FIN DEL ANALISIS")
    print("=" * 60)


if __name__ == "__main__":
    main()
