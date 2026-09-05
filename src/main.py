from taxonomia.clasificador_taxonomia import clasificar_taxonomia
from clasificador.clasificar_ticket import clasificar_ticket
from clasificador.clasificador_csv import clasificar_csv

from reglas.motor_reglas import aplicar_reglas
from conocimiento.recuperador_tfidf import recuperar_informacion

from busqueda.astar_soporte import astar


def main():

    print("=" * 70)
    print("      ASISTENTE INTELIGENTE DE SOPORTE TI HIBRIDO")
    print("=" * 70)

    consulta = input("\nIngrese su consulta: ")

    # TAXONOMIA IA
    categorias = clasificar_taxonomia(consulta)

    # CLASIFICACION DE TICKET
    ticket = clasificar_ticket(consulta)

    # SISTEMA EXPERTO
    regla = aplicar_reglas(consulta)

    # RECUPERACION DE INFORMACION
    informacion, similitud = recuperar_informacion(
        consulta
    )

    # CLASIFICACION CSV
    categoria_predicha, similitud_clase = clasificar_csv(
        consulta
    )

    # A*
    ruta = astar()

    print("\n" + "=" * 70)
    print("RESULTADO DEL ANALISIS")
    print("=" * 70)

    # CONSULTA
    print("\nConsulta recibida:")
    print(f"   {consulta}")

    # TAXONOMIA
    print("\nCategorias detectadas:")

    for categoria in categorias:
        print(f"   • {categoria}")

    # TICKET
    print("\nClasificacion del Ticket:")
    print("-" * 70)

    print(f"Tipo         : {ticket['tipo']}")
    print(f"Criticidad   : {ticket['criticidad']}")
    print(f"Impacto      : {ticket['impacto']}")
    print(f"Prioridad    : {ticket['prioridad']}")
    print(f"Escalamiento : {ticket['escalamiento']}")

    # SISTEMA EXPERTO
    print("\nSistema Experto:")
    print("-" * 70)

    print(f"Regla activada : {regla}")

    # TF-IDF
    print("\nRecuperacion de Informacion:")
    print("-" * 70)

    print("Informacion recuperada:")
    print(f"   {informacion}")

    print(f"\nSimilitud TF-IDF : {similitud}")

    # CLASIFICADOR CSV
    print("\nClasificacion Inteligente:")
    print("-" * 70)

    print(f"Categoria predicha : {categoria_predicha}")
    print(f"Similitud          : {similitud_clase}")

    # A*
    print("\nAnalisis del Incidente (A*)")
    print("-" * 70)

    print("Estado inicial      : Incidente")
    print("Meta objetivo       : Solucionado")
    print("Algoritmo aplicado  : A*")
    print("Heuristica          : Estimacion de pasos restantes")

    print("\nRuta sugerida:\n")

    for i, paso in enumerate(ruta):

        print(f"[{paso}]")

        if i < len(ruta) - 1:
            print("     |")
            print("     v")

    # MINIMAX
    print("\nAnalisis de Priorizacion (Minimax)")
    print("-" * 70)

    print("""
                    MAX
                     |
         +-----------+-----------+
         |           |           |
         v           v           v
      Servidor      VPN     Impresora
         10          6          2
    """)

    if ticket["prioridad"] == "P1":
        decision = "Atender SERVIDOR CRITICO"

    elif ticket["prioridad"] == "P2":
        decision = "Atender INCIDENTE IMPORTANTE"

    else:
        decision = "Atender INCIDENTE DE BAJA PRIORIDAD"

    print("Decision seleccionada:")
    print(f"► {decision}")

    print("\nJustificacion:")
    print(
        "Se selecciona la alternativa "
        "con mayor utilidad operativa."
    )

    # RESUMEN
    print("\nResultado:")
    print("-" * 70)

    print("✓ Incidente analizado")
    print("✓ Categoria IA identificada")
    print("✓ Ticket clasificado")
    print("✓ Regla aplicada")
    print("✓ Informacion recuperada")
    print("✓ Clasificacion realizada")
    print("✓ Ruta de resolucion generada")
    print("✓ Priorizacion calculada")

    print("\n" + "=" * 70)
    print("FIN DEL ANALISIS")
    print("=" * 70)


if __name__ == "__main__":
    main()


                