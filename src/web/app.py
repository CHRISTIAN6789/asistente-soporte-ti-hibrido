import os
import sys


# ==========================================================
# CONFIGURACION DE RUTAS
# Permite importar los modulos ubicados dentro de src
# ==========================================================

SRC_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)


# ==========================================================
# FLASK
# ==========================================================

from flask import Flask, render_template, request


# ==========================================================
# MODULOS PRINCIPALES DEL PROYECTO
# ==========================================================

from taxonomia.clasificador_taxonomia import clasificar_taxonomia

from clasificador.clasificar_ticket import clasificar_ticket

from clasificador.clasificador_csv import clasificar_csv

from reglas.motor_reglas import aplicar_reglas

from conocimiento.recuperador_tfidf import recuperar_informacion

from busqueda.astar_soporte import astar


# ==========================================================
# SEMANA 7
# REPRESENTACIONES DEL RECONOCIMIENTO
# ==========================================================

from semana07_representaciones import analizar_representaciones


# ==========================================================
# SEMANA 8
# RED NEURONAL + SQLITE + ONTOLOGIA
# ==========================================================

from semana08_red_ontologia import analizar_semana08


# ==========================================================
# CREAR APLICACION FLASK
# ==========================================================

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


# ==========================================================
# PAGINA PRINCIPAL
# ==========================================================

@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None

    if request.method == "POST":

        # ==================================================
        # CONSULTA DEL USUARIO
        # ==================================================

        consulta = request.form.get(
            "consulta",
            ""
        ).strip()

        if consulta:

            # ==============================================
            # TAXONOMIA IA
            # ==============================================

            categorias = clasificar_taxonomia(
                consulta
            )


            # ==============================================
            # CLASIFICACION DEL TICKET
            # ==============================================

            ticket = clasificar_ticket(
                consulta
            )


            # ==============================================
            # SISTEMA EXPERTO
            # ==============================================

            regla = aplicar_reglas(
                consulta
            )


            # ==============================================
            # RECUPERACION DE INFORMACION
            # ==============================================

            informacion, similitud = recuperar_informacion(
                consulta
            )


            # ==============================================
            # CLASIFICACION INTELIGENTE CSV
            # ==============================================

            categoria_predicha, similitud_clase = clasificar_csv(
                consulta
            )


            # ==============================================
            # ALGORITMO A*
            # ==============================================

            ruta = astar()


            # ==============================================
            # SEMANA 7
            # NUMERICO + SIMBOLICO + AUTOMATA
            # ==============================================

            representaciones = analizar_representaciones(
                criticidad=ticket["criticidad"],
                impacto=ticket["impacto"],
                tipo=ticket["tipo"]
            )


            # ==============================================
            # SEMANA 8
            # MLP + SQLITE + ONTOLOGIA
            # ==============================================

            semana08 = analizar_semana08(
                consulta
            )


            # ==============================================
            # RESULTADOS ENVIADOS AL HTML
            # ==============================================

            resultado = {

                # Consulta
                "consulta": consulta,

                # Taxonomia
                "categorias": categorias,

                # Ticket
                "ticket": ticket,

                # Sistema experto
                "regla": regla,

                # Recuperacion de informacion
                "informacion": informacion,

                "similitud": similitud,

                # Clasificacion CSV
                "categoria_predicha": categoria_predicha,

                "similitud_clase": similitud_clase,

                # A*
                "ruta": ruta,

                # ==========================================
                # SEMANA 7
                # ==========================================

                "representaciones": representaciones,

                # ==========================================
                # SEMANA 8
                # ==========================================

                "semana08": semana08
            }


    # ======================================================
    # MOSTRAR INDEX.HTML
    # ======================================================

    return render_template(
        "index.html",
        resultado=resultado
    )


# ==========================================================
# INICIAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )