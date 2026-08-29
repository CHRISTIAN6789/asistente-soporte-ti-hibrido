def clasificar_ticket(texto):

    texto = texto.lower()

    # ==========================
    # SERVIDORES
    # ==========================

    if "servidor" in texto:

        return {
            "tipo": "Infraestructura",
            "criticidad": "Alta",
            "impacto": "Alto",
            "prioridad": "P1",
            "escalamiento": "Administrador de Servidores"
        }

    # ==========================
    # SEGURIDAD
    # ==========================

    if (
        "malware" in texto
        or "virus" in texto
        or "antivirus" in texto
    ):

        return {
            "tipo": "Seguridad",
            "criticidad": "Alta",
            "impacto": "Alto",
            "prioridad": "P1",
            "escalamiento": "Equipo de Seguridad"
        }

    # ==========================
    # VPN
    # ==========================

    if "vpn" in texto:

        return {
            "tipo": "Red",
            "criticidad": "Media",
            "impacto": "Alto",
            "prioridad": "P2",
            "escalamiento": "Equipo de Redes"
        }

    # ==========================
    # CORREO
    # ==========================

    if (
        "correo" in texto
        or "outlook" in texto
    ):

        return {
            "tipo": "Correo Corporativo",
            "criticidad": "Media",
            "impacto": "Medio",
            "prioridad": "P2",
            "escalamiento": "Mesa de Ayuda"
        }

    # ==========================
    # IMPRESORAS
    # ==========================

    if "impresora" in texto:

        return {
            "tipo": "Perifericos",
            "criticidad": "Baja",
            "impacto": "Bajo",
            "prioridad": "P4",
            "escalamiento": "Soporte Local"
        }

    # ==========================
    # INTERNET / WIFI
    # ==========================

    if (
        "internet" in texto
        or "wifi" in texto
        or "conectividad" in texto
    ):

        return {
            "tipo": "Conectividad",
            "criticidad": "Media",
            "impacto": "Alto",
            "prioridad": "P2",
            "escalamiento": "Equipo de Redes"
        }

    # ==========================
    # CONTRASEÑAS Y MFA
    # ==========================

    if (
        "contraseña" in texto
        or "mfa" in texto
        or "autenticacion" in texto
        or "usuario" in texto
    ):

        return {
            "tipo": "Acceso",
            "criticidad": "Media",
            "impacto": "Medio",
            "prioridad": "P3",
            "escalamiento": "Mesa de Ayuda"
        }

    # ==========================
    # SOFTWARE
    # ==========================

    if (
        "software" in texto
        or "aplicacion" in texto
        or "sistema" in texto
    ):

        return {
            "tipo": "Aplicacion",
            "criticidad": "Media",
            "impacto": "Medio",
            "prioridad": "P3",
            "escalamiento": "Soporte Aplicativo"
        }

    # ==========================
    # COMPUTADORES
    # ==========================

    if (
        "computador" in texto
        or "pc" in texto
        or "portatil" in texto
        or "disco" in texto
    ):

        return {
            "tipo": "Hardware",
            "criticidad": "Media",
            "impacto": "Medio",
            "prioridad": "P3",
            "escalamiento": "Soporte Tecnico"
        }

    # ==========================
    # GENERAL
    # ==========================

    return {
        "tipo": "General",
        "criticidad": "Media",
        "impacto": "Medio",
        "prioridad": "P3",
        "escalamiento": "Mesa de Ayuda"
    }