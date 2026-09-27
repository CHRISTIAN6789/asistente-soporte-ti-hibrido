from taxonomia.clasificador_taxonomia import clasificar_taxonomia
from clasificador.clasificar_ticket import clasificar_ticket
from clasificador.clasificador_csv import clasificar_csv

from reglas.motor_reglas import aplicar_reglas
from conocimiento.recuperador_tfidf import recuperar_informacion

from busqueda.astar_soporte import astar

# SEMANA 7
from semana07_representaciones import analizar_representaciones

# SEMANA 8
from semana08_red_ontologia import analizar_semana08


def main():

    print("=" * 70)
    print("      ASISTENTE INTELIGENTE DE SOPORTE TI HIBRIDO")
    print("=" * 70)

    consulta = input("\nIngrese su consulta: ")

    # ======================================================
    # TAXONOMIA IA
    # ======================================================

    categorias = clasificar_taxonomia(
        consulta
    )

    # ======================================================
    # CLASIFICACION DEL TICKET
    # ======================================================

    ticket = clasificar_ticket(
        consulta
    )

    # ======================================================
    # SISTEMA EXPERTO
    # ======================================================

    regla = aplicar_reglas(
        consulta
    )

    # ======================================================
    # RECUPERACION DE INFORMACION
    # ======================================================

    informacion, similitud = recuperar_informacion(
        consulta
    )

    # ======================================================
    # CLASIFICACION INTELIGENTE CSV
    # ======================================================

    categoria_predicha, similitud_clase = clasificar_csv(
        consulta
    )

    # ======================================================
    # A*
    # ======================================================

    ruta = astar()

    # ======================================================
    # SEMANA 7
    # REPRESENTACIONES DEL RECONOCIMIENTO
    # ======================================================

    representaciones = analizar_representaciones(
        criticidad=ticket["criticidad"],
        impacto=ticket["impacto"],
        tipo=ticket["tipo"]
    )

    # ======================================================
    # SEMANA 8
    # RED NEURONAL + SQLITE + ONTOLOGIA
    # ======================================================

    resultado_semana08 = analizar_semana08(
        consulta
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

    print(
        f"Tipo         : "
        f"{ticket['tipo']}"
    )

    print(
        f"Criticidad   : "
        f"{ticket['criticidad']}"
    )

    print(
        f"Impacto      : "
        f"{ticket['impacto']}"
    )

    print(
        f"Prioridad    : "
        f"{ticket['prioridad']}"
    )

    print(
        f"Escalamiento : "
        f"{ticket['escalamiento']}"
    )

    # ======================================================
    # SISTEMA EXPERTO
    # ======================================================

    print("\nSistema Experto:")
    print("-" * 70)

    print(
        f"Regla activada : "
        f"{regla}"
    )

    # ======================================================
    # TF-IDF
    # ======================================================

    print("\nRecuperacion de Informacion:")
    print("-" * 70)

    print("Informacion recuperada:")

    print(
        f"   {informacion}"
    )

    print(
        f"\nSimilitud TF-IDF : "
        f"{similitud}"
    )

    # ======================================================
    # CLASIFICACION INTELIGENTE
    # ======================================================

    print("\nClasificacion Inteligente:")
    print("-" * 70)

    print(
        f"Categoria predicha : "
        f"{categoria_predicha}"
    )

    print(
        f"Similitud          : "
        f"{similitud_clase}"
    )

    # ======================================================
    # A*
    # ======================================================

    print("\nAnalisis del Incidente (A*)")
    print("-" * 70)

    print(
        "Estado inicial      : "
        "Incidente"
    )

    print(
        "Meta objetivo       : "
        "Solucionado"
    )

    print(
        "Algoritmo aplicado  : "
        "A*"
    )

    print(
        "Heuristica          : "
        "Estimacion de pasos restantes"
    )

    print("\nRuta sugerida:\n")

    for i, paso in enumerate(
        ruta
    ):

        print(
            f"[{paso}]"
        )

        if i < len(ruta) - 1:

            print("     |")
            print("     v")

    # ======================================================
    # MINIMAX
    # ======================================================

    print(
        "\nAnalisis de Priorizacion (Minimax)"
    )

    print("-" * 70)

    print(
        """
                    MAX
                     |
         +-----------+-----------+
         |           |           |
         v           v           v
      Servidor      VPN     Impresora
         10          6          2
        """
    )

    if ticket["prioridad"] == "P1":

        decision = (
            "Atender SERVIDOR CRITICO"
        )

    elif ticket["prioridad"] == "P2":

        decision = (
            "Atender INCIDENTE IMPORTANTE"
        )

    else:

        decision = (
            "Atender INCIDENTE DE BAJA PRIORIDAD"
        )

    print(
        "Decision seleccionada:"
    )

    print(
        f"-> {decision}"
    )

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

    print(
        "SEMANA 7 - REPRESENTACIONES DEL RECONOCIMIENTO"
    )

    print("=" * 70)

    # ------------------------------------------------------
    # REPRESENTACION NUMERICA
    # ------------------------------------------------------

    numerica = representaciones[
        "numerica"
    ]

    print(
        "\n1. Representacion Numerica"
    )

    print("-" * 70)

    print(
        f"Vector del incidente : "
        f"{numerica['vector']}"
    )

    print(
        f"Vector de referencia : "
        f"{numerica['referencia']}"
    )

    print(
        f"Distancia numerica   : "
        f"{numerica['distancia']}"
    )

    print(
        "\nInterpretacion: cuanto menor sea la distancia, "
        "mayor es la similitud con el patron de "
        "incidente critico."
    )

    # ------------------------------------------------------
    # REPRESENTACION SIMBOLICA
    # ------------------------------------------------------

    simbolica = representaciones[
        "simbolica"
    ]

    print(
        "\n2. Representacion Simbolica"
    )

    print("-" * 70)

    print(
        "Hechos reconocidos:"
    )

    for hecho in simbolica["hechos"]:

        print(
            f"   - {hecho}"
        )

    print(
        f"\nConclusion simbolica : "
        f"{simbolica['conclusion']}"
    )

    # ------------------------------------------------------
    # AUTOMATA
    # ------------------------------------------------------

    automata = representaciones[
        "automata"
    ]

    print(
        "\n3. Reconocimiento mediante Automata"
    )

    print("-" * 70)

    print(
        "Recorrido del ticket:\n"
    )

    recorrido = automata[
        "recorrido"
    ]

    for i, estado in enumerate(
        recorrido
    ):

        print(
            f"[{estado}]"
        )

        if i < len(recorrido) - 1:

            print("     |")
            print("     v")

    print(
        f"\nEstado final : "
        f"{automata['estado_final']}"
    )

    if automata["aceptado"]:

        print(
            "Aceptado     : SI"
        )

        print(
            "Interpretacion: el ticket alcanzo "
            "correctamente el estado RESUELTO."
        )

    else:

        print(
            "Aceptado     : NO"
        )

        if automata["error"]:

            print(
                f"Detalle      : "
                f"{automata['error']}"
            )

    # ======================================================
    # SEMANA 8
    # RED NEURONAL + SQLITE + ONTOLOGIA
    # ======================================================

    print("\n" + "=" * 70)

    print(
        "SEMANA 8 - RECONOCIMIENTO INTELIGENTE"
    )

    print("=" * 70)

    # ------------------------------------------------------
    # RED NEURONAL MLP
    # ------------------------------------------------------

    print(
        "\n1. Red Neuronal MLP"
    )

    print("-" * 70)

    print(
        f"Categoria predicha : "
        f"{resultado_semana08['categoria_predicha']}"
    )

    print(
        f"Confianza MLP      : "
        f"{resultado_semana08['confianza_porcentaje']}%"
    )

    print(
        f"Accuracy del modelo: "
        f"{resultado_semana08['accuracy_porcentaje']}%"
    )

    print(
        f"Modelo utilizado   : "
        f"{resultado_semana08['modelo']}"
    )

    print(
        f"Vectorizador       : "
        f"{resultado_semana08['vectorizador']}"
    )

    # ------------------------------------------------------
    # SQLITE
    # ------------------------------------------------------

    print(
        "\n2. Evidencia SQLite"
    )

    print("-" * 70)

    print(
        f"Base de datos      : "
        f"{resultado_semana08['base_datos']}"
    )

    print(
        f"Registros guardados: "
        f"{resultado_semana08['registros']}"
    )

    print(
        "Estado             : "
        "Evidencia disponible"
    )

    # ------------------------------------------------------
    # ONTOLOGIA
    # ------------------------------------------------------

    print(
        "\n3. Ontologia de Soporte TI"
    )

    print("-" * 70)

    print(
        f"Archivo GraphML    : "
        f"{resultado_semana08['ontologia']}"
    )

    print(
        f"Relaciones         : "
        f"{resultado_semana08['relaciones']}"
    )

    print(
        f"Escalamiento       : "
        f"{resultado_semana08['escalamiento']}"
    )

    # ------------------------------------------------------
    # RELACIONES ONTOLOGICAS
    # ------------------------------------------------------

    relaciones_categoria = resultado_semana08[
        "relaciones_categoria"
    ]

    if relaciones_categoria:

        print(
            "\nRelaciones asociadas:"
        )

        for relacion in relaciones_categoria:

            print(
                f"   {relacion['origen']} "
                f"-> {relacion['relacion']} "
                f"-> {relacion['destino']}"
            )

    else:

        print(
            "\nRelaciones asociadas: "
            "No se encontraron relaciones directas."
        )

    # ------------------------------------------------------
    # INTERPRETACION SEMANA 8
    # ------------------------------------------------------

    print(
        "\nInterpretacion:"
    )

    print("-" * 70)

    print(
        f"La red neuronal reconoce la consulta como "
        f"'{resultado_semana08['categoria_predicha']}'."
    )

    print(
        "La base de datos SQLite conserva evidencia "
        "de los incidentes utilizados por el sistema."
    )

    print(
        "La ontologia relaciona la categoria reconocida "
        "con conceptos y areas responsables de Soporte TI."
    )

    # ======================================================
    # RESUMEN FINAL
    # ======================================================

    print("\n" + "=" * 70)

    print(
        "RESUMEN DEL ANALISIS"
    )

    print("=" * 70)

    print(
        "\n[OK] Incidente analizado"
    )

    print(
        "[OK] Categoria IA identificada"
    )

    print(
        "[OK] Ticket clasificado"
    )

    print(
        "[OK] Regla experta aplicada"
    )

    print(
        "[OK] Informacion recuperada"
    )

    print(
        "[OK] Clasificacion inteligente realizada"
    )

    print(
        "[OK] Ruta de resolucion generada"
    )

    print(
        "[OK] Priorizacion calculada"
    )

    # ------------------------------------------------------
    # RESUMEN SEMANA 7
    # ------------------------------------------------------

    print(
        "\nSEMANA 7:"
    )

    print(
        "[OK] Representacion numerica generada"
    )

    print(
        "[OK] Representacion simbolica generada"
    )

    print(
        "[OK] Automata ejecutado"
    )

    # ------------------------------------------------------
    # RESUMEN SEMANA 8
    # ------------------------------------------------------

    print(
        "\nSEMANA 8:"
    )

    print(
        "[OK] Red neuronal MLP ejecutada"
    )

    print(
        "[OK] Prediccion neuronal generada"
    )

    print(
        "[OK] Evidencia SQLite disponible"
    )

    print(
        "[OK] Ontologia de Soporte TI consultada"
    )

    print("\n" + "=" * 70)

    print(
        "FIN DEL ANALISIS"
    )

    print("=" * 70)


if __name__ == "__main__":
    main()