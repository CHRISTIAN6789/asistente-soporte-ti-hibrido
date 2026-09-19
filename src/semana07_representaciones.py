import math


# ==========================================
# SEMANA 7
# REPRESENTACIONES DEL RECONOCIMIENTO
# PROYECTO: ASISTENTE INTELIGENTE SOPORTE TI
# ==========================================


# ------------------------------------------
# 1. REPRESENTACION NUMERICA
# ------------------------------------------

def representacion_numerica(
    criticidad,
    impacto,
    sintomas
):
    vector_incidente = [
        criticidad,
        impacto,
        sintomas
    ]

    # Referencia de un incidente critico
    vector_critico = [
        3,
        3,
        3
    ]

    distancia = math.sqrt(
        sum(
            (actual - referencia) ** 2
            for actual, referencia
            in zip(vector_incidente, vector_critico)
        )
    )

    return {
        "vector": vector_incidente,
        "referencia": vector_critico,
        "distancia": round(distancia, 3)
    }


# ------------------------------------------
# 2. REPRESENTACION SIMBOLICA
# ------------------------------------------

def representacion_simbolica(
    criticidad,
    impacto,
    tipo
):
    hechos = set()

    if criticidad == "Alta":
        hechos.add("criticidad_alta")

    if criticidad == "Media":
        hechos.add("criticidad_media")

    if criticidad == "Baja":
        hechos.add("criticidad_baja")

    if impacto == "Alto":
        hechos.add("impacto_alto")

    if impacto == "Medio":
        hechos.add("impacto_medio")

    if impacto == "Bajo":
        hechos.add("impacto_bajo")

    if tipo == "Infraestructura":
        hechos.add("infraestructura")

    if tipo == "Red":
        hechos.add("red")

    if tipo == "Seguridad":
        hechos.add("seguridad")

    if (
        "criticidad_alta" in hechos
        and "impacto_alto" in hechos
    ):
        conclusion = "incidente_critico"

    elif (
        "criticidad_media" in hechos
        or "impacto_medio" in hechos
    ):
        conclusion = "incidente_importante"

    else:
        conclusion = "incidente_controlado"

    return {
        "hechos": sorted(hechos),
        "conclusion": conclusion
    }


# ------------------------------------------
# 3. AUTOMATA DE ESTADOS DEL TICKET
# ------------------------------------------

def automata_ticket(secuencia):
    estado = "NUEVO"

    transiciones = {
        ("NUEVO", "diagnosticar"): "DIAGNOSTICO",
        ("DIAGNOSTICO", "resolver"): "RESUELTO",
        ("DIAGNOSTICO", "escalar"): "ESCALADO",
        ("ESCALADO", "resolver"): "RESUELTO"
    }

    recorrido = [estado]

    for accion in secuencia:
        clave = (estado, accion)

        if clave not in transiciones:
            return {
                "aceptado": False,
                "estado_final": estado,
                "recorrido": recorrido,
                "error": (
                    f"Transicion no valida: "
                    f"{estado} -> {accion}"
                )
            }

        estado = transiciones[clave]
        recorrido.append(estado)

    aceptado = estado == "RESUELTO"

    return {
        "aceptado": aceptado,
        "estado_final": estado,
        "recorrido": recorrido,
        "error": None
    }


# ------------------------------------------
# PRUEBA INTEGRADA
# ------------------------------------------

def analizar_representaciones(
    criticidad,
    impacto,
    tipo
):
    mapa_numerico = {
        "Baja": 1,
        "Media": 2,
        "Alta": 3
    }

    resultado_numerico = representacion_numerica(
        mapa_numerico.get(criticidad, 1),
        mapa_numerico.get(impacto, 1),
        2
    )

    resultado_simbolico = representacion_simbolica(
        criticidad,
        impacto,
        tipo
    )

    if criticidad == "Alta":
        acciones = [
            "diagnosticar",
            "escalar",
            "resolver"
        ]
    else:
        acciones = [
            "diagnosticar",
            "resolver"
        ]

    resultado_automata = automata_ticket(
        acciones
    )

    return {
        "numerica": resultado_numerico,
        "simbolica": resultado_simbolico,
        "automata": resultado_automata
    }


# ------------------------------------------
# EJECUCION DIRECTA
# ------------------------------------------

if __name__ == "__main__":
    resultado = analizar_representaciones(
        criticidad="Alta",
        impacto="Alto",
        tipo="Infraestructura"
    )

    print("=" * 60)
    print("SEMANA 7 - REPRESENTACIONES DEL RECONOCIMIENTO")
    print("=" * 60)

    print("\n1. REPRESENTACION NUMERICA")
    print(resultado["numerica"])

    print("\n2. REPRESENTACION SIMBOLICA")
    print(resultado["simbolica"])

    print("\n3. AUTOMATA")
    print(resultado["automata"])