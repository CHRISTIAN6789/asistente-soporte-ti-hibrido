from collections import defaultdict


# ==========================================================
# RED SEMANTICA
# ==========================================================

class RedSemantica:

    def __init__(self):

        self.aristas = defaultdict(list)

    # ======================================================
    # AGREGAR RELACION
    # ======================================================

    def agregar(
        self,
        origen,
        relacion,
        destino
    ):

        origen = origen.lower().strip()
        relacion = relacion.lower().strip()
        destino = destino.lower().strip()

        self.aristas[origen].append(
            (
                relacion,
                destino
            )
        )

    # ======================================================
    # CONSULTA JERARQUICA
    # ======================================================

    def es_un(
        self,
        origen,
        categoria
    ):

        origen = origen.lower().strip()
        categoria = categoria.lower().strip()

        pendientes = [origen]

        visitados = set()

        while pendientes:

            actual = pendientes.pop()

            if actual == categoria:
                return True

            if actual in visitados:
                continue

            visitados.add(actual)

            for relacion, destino in self.aristas.get(
                actual,
                []
            ):

                if relacion == "es_un":

                    pendientes.append(
                        destino
                    )

        return False

    # ======================================================
    # HERENCIA DE PROPIEDADES
    # ======================================================

    def obtener_necesidades(
        self,
        concepto
    ):

        concepto = concepto.lower().strip()

        pendientes = [concepto]

        visitados = set()

        necesidades = set()

        while pendientes:

            actual = pendientes.pop()

            if actual in visitados:
                continue

            visitados.add(actual)

            for relacion, destino in self.aristas.get(
                actual,
                []
            ):

                if relacion == "necesita":

                    necesidades.add(
                        destino
                    )

                if relacion == "es_un":

                    pendientes.append(
                        destino
                    )

        return sorted(
            necesidades
        )

    # ======================================================
    # OBTENER RELACIONES
    # ======================================================

    def obtener_relaciones(self):

        relaciones = []

        for origen in self.aristas:

            for relacion, destino in self.aristas[
                origen
            ]:

                relaciones.append({

                    "origen":
                        origen,

                    "relacion":
                        relacion,

                    "destino":
                        destino
                })

        return relaciones


# ==========================================================
# CREAR RED DE SOPORTE TI
# ==========================================================

def crear_red_soporte_ti():

    red = RedSemantica()

    # --------------------------------------------------
    # JERARQUIA
    # --------------------------------------------------

    red.agregar(
        "servidor",
        "es_un",
        "infraestructura"
    )

    red.agregar(
        "vpn",
        "es_un",
        "red"
    )

    red.agregar(
        "router",
        "es_un",
        "red"
    )

    red.agregar(
        "red",
        "es_un",
        "infraestructura"
    )

    red.agregar(
        "infraestructura",
        "es_un",
        "activo_ti"
    )

    red.agregar(
        "impresora",
        "es_un",
        "activo_ti"
    )

    # --------------------------------------------------
    # PROPIEDADES
    # --------------------------------------------------

    red.agregar(
        "activo_ti",
        "necesita",
        "monitoreo"
    )

    red.agregar(
        "infraestructura",
        "necesita",
        "mantenimiento"
    )

    red.agregar(
        "red",
        "necesita",
        "conectividad"
    )

    red.agregar(
        "servidor",
        "necesita",
        "respaldo"
    )

    return red


# ==========================================================
# ANALISIS SEMANA 14
# ==========================================================

def analizar_semana14():

    red = crear_red_soporte_ti()

    relaciones = red.obtener_relaciones()

    consultas = [

        {

            "pregunta":
                "Servidor es un Activo_TI",

            "resultado":
                red.es_un(
                    "servidor",
                    "activo_ti"
                )
        },

        {

            "pregunta":
                "VPN es Infraestructura",

            "resultado":
                red.es_un(
                    "vpn",
                    "infraestructura"
                )
        },

        {

            "pregunta":
                "Router es Activo_TI",

            "resultado":
                red.es_un(
                    "router",
                    "activo_ti"
                )
        }
    ]

    necesidades_servidor = (
        red.obtener_necesidades(
            "servidor"
        )
    )

    necesidades_vpn = (
        red.obtener_necesidades(
            "vpn"
        )
    )

    return {

        "conceptos": [

            "Servidor",
            "VPN",
            "Router",
            "Red",
            "Infraestructura",
            "Activo_TI"
        ],

        "relaciones":
            relaciones,

        "consultas":
            consultas,

        "necesidades_servidor":
            necesidades_servidor,

        "necesidades_vpn":
            necesidades_vpn,

        "total_relaciones":
            len(relaciones)
    }

if __name__ == "__main__":

    print("Entrando a Semana 14...")

    resultado = analizar_semana14()

    print(resultado)