from dataclasses import dataclass


# ==========================================================
# ESTRUCTURA DE REGLA
# ==========================================================

@dataclass(frozen=True)
class Regla:

    nombre: str

    premisas: frozenset

    conclusion: str


# ==========================================================
# MOTOR DE INFERENCIA
# ==========================================================

def inferir(
    hechos_iniciales,
    reglas
):

    hechos = set(
        hechos_iniciales
    )

    trazas = []

    cambios = True

    while cambios:

        cambios = False

        for regla in reglas:

            if (
                regla.premisas.issubset(
                    hechos
                )
                and
                regla.conclusion
                not in hechos
            ):

                hechos.add(
                    regla.conclusion
                )

                trazas.append(
                    regla.nombre
                )

                cambios = True

    return hechos, trazas


# ==========================================================
# SEMANA 13
# INGENIERIA DEL CONOCIMIENTO
# ==========================================================

def analizar_semana13(
    ticket,
    semana09
):

    hechos = set()

    # ======================================================
    # HECHOS INICIALES
    # ======================================================

    if ticket:

        criticidad = (
            str(
                ticket.get(
                    "criticidad",
                    ""
                )
            )
            .lower()
            .strip()
        )

        impacto = (
            str(
                ticket.get(
                    "impacto",
                    ""
                )
            )
            .lower()
            .strip()
        )

        tipo = (
            str(
                ticket.get(
                    "tipo",
                    ""
                )
            )
            .lower()
            .strip()
        )

        prioridad = (
            str(
                ticket.get(
                    "prioridad",
                    ""
                )
            )
            .lower()
            .strip()
        )

        # ------------------------------
        # CRITICIDAD
        # ------------------------------

        if (
            "alta" in criticidad
            or
            "critica" in criticidad
            or
            "crítica" in criticidad
        ):

            hechos.add(
                "incidente_critico"
            )

        # ------------------------------
        # IMPACTO
        # ------------------------------

        if (
            "alto" in impacto
            or
            "alta" in impacto
        ):

            hechos.add(
                "alto_impacto"
            )

        # ------------------------------
        # TIPO
        # ------------------------------

        if (
            "servidor" in tipo
        ):

            hechos.add(
                "categoria_servidor"
            )

        # ------------------------------
        # PRIORIDAD
        # ------------------------------

        if (
            "alta" in prioridad
            or
            "critica" in prioridad
            or
            "crítica" in prioridad
        ):

            hechos.add(
                "prioridad_alta"
            )

    # ----------------------------------
    # EVIDENCIA VISUAL
    # ----------------------------------

    if semana09:

        hechos.add(
            "evidencia_disponible"
        )

    # ======================================================
    # REGLAS
    # ======================================================

    reglas = [

        # ----------------------------------------------
        # R1
        # ----------------------------------------------

        Regla(
            "R1",
            frozenset([
                "alto_impacto"
            ]),
            "escalamiento_requerido"
        ),

        # ----------------------------------------------
        # R2
        # ----------------------------------------------

        Regla(
            "R2",
            frozenset([
                "escalamiento_requerido",
                "evidencia_disponible"
            ]),
            "atencion_prioritaria"
        ),

        # ----------------------------------------------
        # R3
        # ----------------------------------------------

        Regla(
            "R3",
            frozenset([
                "atencion_prioritaria"
            ]),
            "ticket_urgente"
        ),

        # ----------------------------------------------
        # R4
        # ----------------------------------------------

        Regla(
            "R4",
            frozenset([
                "ticket_urgente",
                "prioridad_alta"
            ]),
            "accion_inmediata"
        )

    ]

    # ======================================================
    # MOTOR DE INFERENCIA
    # ======================================================

    hechos_finales, trazas = inferir(
        hechos,
        reglas
    )

    # ======================================================
    # CONCLUSION
    # ======================================================

    if (
        "accion_inmediata"
        in hechos_finales
    ):

        conclusion = (
            "Acción inmediata requerida"
        )

    elif (
        "ticket_urgente"
        in hechos_finales
    ):

        conclusion = (
            "Ticket urgente"
        )

    elif (
        "atencion_prioritaria"
        in hechos_finales
    ):

        conclusion = (
            "Atención prioritaria"
        )

    elif (
        "escalamiento_requerido"
        in hechos_finales
    ):

        conclusion = (
            "Escalamiento requerido"
        )

    else:

        conclusion = (
            "No se generó una conclusión crítica"
        )

    # ======================================================
    # RETURN
    # ======================================================

    return {

        "hechos":
            sorted(
                hechos_finales
            ),

        "trazas":
            trazas,

        "reglas_activadas":
            len(trazas),

        "conclusion":
            conclusion
    }


# ==========================================================
# PRUEBA LOCAL
# ==========================================================

if __name__ == "__main__":

    ticket_prueba = {

        "criticidad":
            "Alta",

        "impacto":
            "Alto",

        "tipo":
            "Servidor",

        "prioridad":
            "Crítica"
    }

    semana09_prueba = {

        "imagen":
            "router.png"
    }

    resultado = analizar_semana13(
        ticket_prueba,
        semana09_prueba
    )

    print(
        "\n===== RESULTADO SEMANA 13 =====\n"
    )

    print(resultado)