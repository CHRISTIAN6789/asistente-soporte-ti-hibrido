def clasificar_taxonomia(texto):

    texto = texto.lower()

    categorias = []

    # SOPORTE TI
    if (
        "computador" in texto
        or "pc" in texto
        or "portatil" in texto
        or "correo" in texto
        or "outlook" in texto
        or "internet" in texto
        or "wifi" in texto
        or "vpn" in texto
        or "impresora" in texto
        or "aplicacion" in texto
        or "software" in texto
        or "contraseña" in texto
        or "usuario" in texto
        or "mfa" in texto
        or "autenticacion" in texto
        or "servidor" in texto
        or "disco" in texto
        or "antivirus" in texto
        or "malware" in texto
        or "conectividad" in texto
    ):
        categorias.append("Soporte TI")

    # PLN
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

    # Visión
    if (
        "imagen" in texto
        or "camara" in texto
        or "rostro" in texto
        or "fotografia" in texto
        or "matricula" in texto
        or "peaton" in texto
    ):
        categorias.append("Vision por Computador")

    # Predictivo
    if (
        "predecir" in texto
        or "fraude" in texto
        or "demanda" in texto
        or "ventas" in texto
        or "riesgo" in texto
        or "sensores" in texto
        or "anomalia" in texto
    ):
        categorias.append("Aprendizaje Automatico Predictivo")

    # Recomendación
    if (
        "recomendar" in texto
        or "sugerir" in texto
        or "preferencias" in texto
        or "historial" in texto
    ):
        categorias.append("Sistemas de Recomendacion")

    # Optimización
    if (
        "ruta" in texto
        or "optimizar" in texto
        or "logistica" in texto
        or "inventario" in texto
        or "horario" in texto
    ):
        categorias.append("Busqueda y Optimizacion")

    # Sistemas Expertos
    if (
        "diagnostico" in texto
        or "reglas" in texto
        or "credito" in texto
        or "politicas" in texto
        or "sintomas" in texto
    ):
        categorias.append("Sistemas Expertos")

    # Robótica
    if (
        "robot" in texto
        or "dron" in texto
        or "autonomo" in texto
        or "trayectoria" in texto
        or "obstaculos" in texto
    ):
        categorias.append("Robotica y Sistemas Autonomos")

    if not categorias:
        categorias.append("Requiere Analisis")

    return categorias