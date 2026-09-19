from taxonomia.clasificador_taxonomia import clasificar_taxonomia
from clasificador.clasificar_ticket import clasificar_ticket
from clasificador.clasificador_csv import clasificar_csv

from reglas.motor_reglas import aplicar_reglas
from conocimiento.recuperador_tfidf import recuperar_informacion

from busqueda.astar_soporte import astar

# SEMANA 7
from semana07_representaciones import analizar_representaciones


def main():

    print("=" * 70)
    print("      ASISTENTE INTELIGENTE DE SOPORTE TI HIBRIDO")
    print("=" * 70)

    consulta = input("\nIngrese su consulta: ")

    # ======================================================
    # TAXONOMIA IA
    # ======================================================

    categorias = clasificar_taxonomia(consulta)

    # ======================================================
    # CLASIFICACION DEL TICKET
    # ======================================================

    ticket = clasificar_ticket(consulta)

    # ======================================================
    # SISTEMA EXPERTO
    # ======================================================

    regla = aplicar_reglas(consulta)

    # ======================================================
    # RECUPERACION DE INFORMACION
    # ======================================================

    informacion, similitud = recuperar_informacion(
        consulta
    )

    # ======================================================
    # CLASIFICACION CSV
    # ======================================================

    categoria_predicha, similitud_clase = clasificar_csv(
        consulta
    )

    # ======================================================
    # A*
    # ======================================================

    ruta = astar()

    # ======================================================
    # SEMANA 7 - REPRESENTACIONES DEL RECONOCIMIENTO
    # ======================================================

    representaciones = analizar_representaciones(
        criticidad=ticket["criticidad"],
        impacto=ticket["impacto"],
        tipo=ticket["tipo"]
    )

    # ======================================================
    # RESULTADO GENERAL
    # ======================================================

    print("\n" + "=" * 70)
    print("RESULTADO DEL ANALISIS")
    print("=" * 70)

    # ======================================================
    # CONSULTA
    # ======================================================

    print("\nConsulta recibida:")
    print(f"   {consulta}")

    # ======================================================
    # TAXONOMIA
    # ======================================================

    print("\nCategorias detectadas:")

    for categoria in categorias:
        print(f"   - {categoria}")

    # ======================================================
    # CLASIFICACION DEL TICKET
    # ======================================================

    print("\nClasificacion del Ticket:")
    print("-" * 70)

    print(f"Tipo         : {ticket['tipo']}")
    print(f"Criticidad   : {ticket['criticidad']}")
    print(f"Impacto      : {ticket['impacto']}")
    print(f"Prioridad    : {ticket['prioridad']}")
    print(f"Escalamiento : {ticket['escalamiento']}")

    # ======================================================
    # SISTEMA EXPERTO
    # ======================================================

    print("\nSistema Experto:")
    print("-" * 70)

    print(f"Regla activada : {regla}")

    # ======================================================
    # TF-IDF
    # ======================================================

    print("\nRecuperacion de Informacion:")
    print("-" * 70)

    print("Informacion recuperada:")
    print(f"   {informacion}")

    print(f"\nSimilitud TF-IDF : {similitud}")

    # ======================================================
    # CLASIFICACION INTELIGENTE
    # ======================================================

    print("\nClasificacion Inteligente:")
    print("-" * 70)

    print(f"Categoria predicha : {categoria_predicha}")
    print(f"Similitud          : {similitud_clase}")

    # ======================================================
    # A*
    # ======================================================

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

    # ======================================================
    # MINIMAX
    # ======================================================

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
    print(f"-> {decision}")

    print("\nJustificacion:")
    print(
        "Se selecciona la alternativa "
        "con mayor utilidad operativa."
    )

    # ======================================================
    # SEMANA 7
    # REPRESENTACIONES DEL RECONOCIMIENTO
    # ======================================================

    print("\n" + "=" * 70)
    print("SEMANA 7 - REPRESENTACIONES DEL RECONOCIMIENTO")
    print("=" * 70)

    # ------------------------------------------------------
    # REPRESENTACION NUMERICA
    # ------------------------------------------------------

    numerica = representaciones["numerica"]

    print("\n1. Representacion Numerica")
    print("-" * 70)

    print(f"Vector del incidente : {numerica['vector']}")
    print(f"Vector de referencia : {numerica['referencia']}")
    print(f"Distancia numerica   : {numerica['distancia']}")

    print(
        "\nInterpretacion: cuanto menor sea la distancia, "
        "mayor es la similitud con el patron de incidente critico."
    )

    # ------------------------------------------------------
    # REPRESENTACION SIMBOLICA
    # ------------------------------------------------------

    simbolica = representaciones["simbolica"]

    print("\n2. Representacion Simbolica")
    print("-" * 70)

    print("Hechos reconocidos:")

    for hecho in simbolica["hechos"]:
        print(f"   - {hecho}")

    print(
        f"\nConclusion simbolica : "
        f"{simbolica['conclusion']}"
    )

    # ------------------------------------------------------
    # AUTOMATA
    # ------------------------------------------------------

    automata = representaciones["automata"]

    print("\n3. Reconocimiento mediante Automata")
    print("-" * 70)

    print("Recorrido del ticket:\n")

    recorrido = automata["recorrido"]

    for i, estado in enumerate(recorrido):

        print(f"[{estado}]")

        if i < len(recorrido) - 1:
            print("     |")
            print("     v")

    print(
        f"\nEstado final : "
        f"{automata['estado_final']}"
    )

    if automata["aceptado"]:
        print("Aceptado     : SI")
        print(
            "Interpretacion: el ticket alcanzo "
            "correctamente el estado RESUELTO."
        )
    else:
        print("Aceptado     : NO")

        if automata["error"]:
            print(
                f"Detalle      : "
                f"{automata['error']}"
            )

    # ======================================================
    # RESUMEN FINAL
    # ======================================================

    print("\n" + "=" * 70)
    print("RESUMEN DEL ANALISIS")
    print("=" * 70)

    print("\n[OK] Incidente analizado")
    print("[OK] Categoria IA identificada")
    print("[OK] Ticket clasificado")
    print("[OK] Regla experta aplicada")
    print("[OK] Informacion recuperada")
    print("[OK] Clasificacion inteligente realizada")
    print("[OK] Ruta de resolucion generada")
    print("[OK] Priorizacion calculada")

    print("\nSEMANA 7:")

    print("[OK] Representacion numerica generada")
    print("[OK] Representacion simbolica generada")
    print("[OK] Automata ejecutado")

    print("\n" + "=" * 70)
    print("FIN DEL ANALISIS")
    print("=" * 70)


if __name__ == "__main__":
    main()

                