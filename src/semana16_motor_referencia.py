import re
import unicodedata


# ==========================================================
# BASE DE REFERENCIAS VALIDADA
# ==========================================================

REFERENCIAS = [

    {
        "id": "REF-ACCESO",

        "titulo":
            "Problemas de Acceso",

        "claves": [
            "sesion",
            "inicio",
            "contraseña",
            "contrasena",
            "password",
            "mfa",
            "autenticacion",
            "autenticación",
            "usuario",
            "bloqueado",
            "cuenta"
        ],

        "respuesta":
            "Validar credenciales, MFA, bloqueo de usuario y estado de la cuenta corporativa.",

        "fuente":
            "Base de Conocimiento TI",

        "validada":
            True
    },

    {
        "id": "REF-CORREO",

        "titulo":
            "Incidentes de Correo",

        "claves": [
            "correo",
            "outlook",
            "mail",
            "mensaje",
            "buzon",
            "buzón",
            "sincroniza",
            "enviar"
        ],

        "respuesta":
            "Validar conectividad, perfil de Outlook y disponibilidad del buzón.",

        "fuente":
            "Manual Correo Corporativo",

        "validada":
            True
    },

    {
        "id": "REF-HARDWARE",

        "titulo":
            "Problemas de Hardware",

        "claves": [
            "pantalla",
            "azul",
            "teclado",
            "computador",
            "equipo",
            "lento",
            "disco",
            "reinicia"
        ],

        "respuesta":
            "Ejecutar diagnóstico de hardware y revisar recursos del equipo.",

        "fuente":
            "Procedimiento Hardware",

        "validada":
            True
    },

    {
        "id": "REF-INFRA",

        "titulo":
            "Incidentes de Infraestructura",

        "claves": [
            "servidor",
            "servicio",
            "infraestructura",
            "memoria",
            "caido",
            "caído",
            "recursos"
        ],

        "respuesta":
            "Escalar inmediatamente al administrador de infraestructura.",

        "fuente":
            "Runbook Infraestructura",

        "validada":
            True
    },

    {
        "id": "REF-RED",

        "titulo":
            "Problemas de Red",

        "claves": [
            "internet",
            "wifi",
            "vpn",
            "red",
            "conexion",
            "conexión",
            "conectividad"
        ],

        "respuesta":
            "Validar conectividad de red, VPN y acceso a servicios corporativos.",

        "fuente":
            "Manual de Redes",

        "validada":
            True
    },

    {
        "id": "REF-SEGURIDAD",

        "titulo":
            "Incidentes de Seguridad",

        "claves": [
            "malware",
            "virus",
            "amenaza",
            "seguridad",
            "antivirus",
            "sospechoso"
        ],

        "respuesta":
            "Aislar el equipo y ejecutar procedimiento de análisis de amenazas.",

        "fuente":
            "Manual Seguridad TI",

        "validada":
            True
    },

    {
        "id": "REF-SOFTWARE",

        "titulo":
            "Problemas de Software",

        "claves": [
            "software",
            "erp",
            "programa",
            "aplicacion",
            "aplicación",
            "sistema",
            "error"
        ],

        "respuesta":
            "Validar configuración, logs y estado de la aplicación.",

        "fuente":
            "Manual Aplicaciones Empresariales",

        "validada":
            True
    }

]
# ==========================================================
# NORMALIZAR TEXTO
# ==========================================================

def normalizar(texto):

    descompuesto = unicodedata.normalize(
        "NFD",
        texto.casefold()
    )

    sin_tildes = "".join(

        caracter

        for caracter in descompuesto

        if unicodedata.category(
            caracter
        ) != "Mn"

    )

    return set(

        re.findall(
            r"[a-z0-9]+",
            sin_tildes
        )

    )


# ==========================================================
# MOTOR DE REFERENCIA
# ==========================================================

def buscar_referencia(
    consulta
):

    palabras = normalizar(
        consulta
    )

    candidatos = []

    for referencia in REFERENCIAS:

        if not referencia[
            "validada"
        ]:
            continue

        coincidencias = (

            palabras.intersection(
                referencia["claves"]
            )

        )

        if coincidencias:

            candidatos.append(

                (
                    len(
                        coincidencias
                    ),
                    referencia
                )

            )

    if not candidatos:

        return {

            "estado":
                "SIN_REFERENCIA",

            "referencia":
                None,

            "titulo":
                None,

            "respuesta":
                (
                    "No existe una referencia validada "
                    "para la consulta realizada."
                ),

            "fuente":
                None
        }

    candidatos.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    mejor = candidatos[
        0
    ][1]

    return {

        "estado":
            "ENCONTRADA",

        "referencia":
            mejor["id"],

        "titulo":
            mejor["titulo"],

        "respuesta":
            mejor["respuesta"],

        "fuente":
            mejor["fuente"]
    }


# ==========================================================
# SEMANA 16
# ==========================================================

def analizar_semana16(
    consulta
):

    if not consulta:

        return {

            "estado":
                "SIN_CONSULTA",

            "referencia":
                None,

            "titulo":
                None,

            "respuesta":
                "No se recibió una consulta.",

            "fuente":
                None
        }

    return buscar_referencia(
        consulta
    )


# ==========================================================
# PRUEBA LOCAL
# ==========================================================

if __name__ == "__main__":

    resultado = analizar_semana16(
        "No puedo acceder a la VPN institucional"
    )

    print(
        "\n===== SEMANA 16 =====\n"
    )

    print(resultado)