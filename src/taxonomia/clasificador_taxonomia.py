def clasificar_taxonomia(texto):

    texto = texto.lower()

    categorias = []

    # Procesamiento de Lenguaje Natural
    if (
        "chatbot" in texto
        or "comentario" in texto
        or "correo" in texto
        or "texto" in texto
        or "contrato" in texto
        or "traducir" in texto
        or "sentimiento" in texto
        or "opinion" in texto
        or "pregunta" in texto
        or "respuesta" in texto
    ):
        categorias.append("Procesamiento de Lenguaje Natural")

    # Visión por Computador
    if (
        "imagen" in texto
        or "imagenes" in texto
        or "camara" in texto
        or "camaras" in texto
        or "rostro" in texto
        or "rostros" in texto
        or "fotografia" in texto
        or "fotografias" in texto
        or "matricula" in texto
        or "matriculas" in texto
        or "peaton" in texto
        or "peatones" in texto
    ):
        categorias.append("Vision por Computador")

    if (
        "predecir" in texto
        or "fraude" in texto
        or "fraudes" in texto
        or "demanda" in texto
        or "estimar" in texto
        or "ventas" in texto
        or "riesgo" in texto
        or "riesgos" in texto
        or "sensores" in texto
        or "sensores" in texto
        or "anomalia" in texto
        or "anomalias" in texto
        or "pronosticar" in texto
    ):
        categorias.append("Aprendizaje Automatico Predictivo")

    # Sistemas de Recomendación
    if (
        "recomendar" in texto
        or "recomendacion" in texto
        or "recomendaciones" in texto
        or "preferencias" in texto
        or "sugerir" in texto
        or "historial" in texto
    ):
        categorias.append("Sistemas de Recomendacion")

    # Búsqueda y Optimización
    if (
        "ruta" in texto
        or "rutas" in texto
        or "optimizar" in texto
        or "optimizacion" in texto
        or "logistica" in texto
        or "inventario" in texto
        or "inventarios" in texto
        or "horario" in texto
        or "horarios" in texto
        or "planificar" in texto
        or "transporte" in texto
    ):
        categorias.append("Busqueda y Optimizacion")

    # Sistemas Expertos
    if (
        "diagnostico" in texto
        or "diagnosticos" in texto
        or "reglas" in texto
        or "credito" in texto
        or "prestamo" in texto
        or "prestamos" in texto
        or "politicas" in texto
        or "normas" in texto
        or "sintomas" in texto
    ):
        categorias.append("Sistemas Expertos")

    if (
        "robot" in texto
        or "robots" in texto
        or "dron" in texto
        or "drones" in texto
        or "autonomo" in texto
        or "autonomos" in texto
        or "vehiculo autonomo" in texto
        or "trayectoria" in texto
        or "obstaculos" in texto
    ):
        categorias.append("Robotica y Sistemas Autonomos")

    if not categorias:
        categorias.append("Requiere Analisis")

    return categorias


if __name__ == "__main__":

    consultas = [
        "crear un chatbot para atender estudiantes",
        "analizar comentarios de clientes",
        "clasificar correos electrónicos como spam",
        "traducir mensajes de usuarios",
        "detectar matriculas de vehiculos",
        "reconocer rostros en fotografias",
        "analizar imagenes medicas",
        "detectar incendios en camaras de seguridad",
        "predecir fraudes bancarios",
        "predecir demanda de energia",
        "estimar ventas de una empresa",
        "pronosticar riesgo crediticio",
        "detectar anomalias en sensores",
        "recomendar peliculas a un usuario",
        "sugerir productos segun historial",
        "optimizar una ruta de transporte",
        "planificar rutas de distribucion",
        "optimizar inventarios de una bodega",
        "crear un sistema de diagnostico medico",
        "evaluar creditos mediante reglas",
        "analizar sintomas para dar diagnosticos",
        "controlar un dron autonomo",
        "programar un robot industrial",
        "guiar robots dentro de un almacen",
        "identificar peatones mediante un vehiculo autonomo"
    ]

    print("=" * 70)
    print("CLASIFICADOR DE TAXONOMIA DE IA")
    print("=" * 70)

    for consulta in consultas:

        categorias = clasificar_taxonomia(consulta)

        print("\nConsulta:")
        print(consulta)

        print("Categorias detectadas:")

        for categoria in categorias:
            print(f" - {categoria}")