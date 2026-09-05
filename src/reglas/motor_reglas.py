def aplicar_reglas(consulta):

    consulta = consulta.lower()

    if "correo" in consulta:
        return "Verificar credenciales y servicio de correo"

    elif "vpn" in consulta:
        return "Validar configuracion y conectividad VPN"

    elif "impresora" in consulta:
        return "Revisar controladores y cola de impresion"

    elif "servidor" in consulta:
        return "Validar servicios criticos del servidor"

    elif "malware" in consulta:
        return "Aislar equipo y ejecutar analisis"

    elif "contraseña" in consulta:
        return "Restablecer contraseña"

    elif "usuario bloqueado" in consulta:
        return "Desbloquear cuenta"

    elif "mfa" in consulta:
        return "Verificar autenticacion multifactor"

    elif "wifi" in consulta:
        return "Revisar punto de acceso"

    elif "internet" in consulta:
        return "Validar conectividad de red"

    return "Escalar a mesa de ayuda"