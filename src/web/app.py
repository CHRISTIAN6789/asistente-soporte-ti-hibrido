import os
import sys
import uuid
from pathlib import Path


# ==========================================================
# CONFIGURACION DE RUTAS
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

from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename


# ==========================================================
# MODULOS DEL PROYECTO
# ==========================================================

from taxonomia.clasificador_taxonomia import clasificar_taxonomia
from clasificador.clasificar_ticket import clasificar_ticket
from clasificador.clasificador_csv import clasificar_csv
from reglas.motor_reglas import aplicar_reglas
from conocimiento.recuperador_tfidf import recuperar_informacion
from busqueda.astar_soporte import astar


# ==========================================================
# SEMANA 7
# ==========================================================

from semana07_representaciones import analizar_representaciones


# ==========================================================
# SEMANA 8
# ==========================================================

from semana08_red_ontologia import analizar_semana08


# ==========================================================
# SEMANA 9
# ==========================================================

from semana09_vision import analizar_semana09


# ==========================================================
# CREAR APLICACION FLASK
# ==========================================================

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


# ==========================================================
# CONFIGURACION DE CARGA DE IMAGENES
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

UPLOAD_FOLDER = (
    BASE_DIR
    / "static"
    / "uploads"
)

UPLOAD_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)

app.config["UPLOAD_FOLDER"] = str(UPLOAD_FOLDER)


# Limite de 8 MB por solicitud
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024


# ==========================================================
# EXTENSIONES PERMITIDAS
# ==========================================================

EXTENSIONES_PERMITIDAS = {
    "png",
    "jpg",
    "jpeg"
}


# ==========================================================
# VALIDAR ARCHIVO
# ==========================================================

def extension_permitida(nombre_archivo):

    return (
        "."
        in nombre_archivo
        and nombre_archivo.rsplit(".", 1)[1].lower()
        in EXTENSIONES_PERMITIDAS
    )


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route(
    "/",
    methods=[
        "GET",
        "POST"
    ]
)
def inicio():

    resultado = None
    error_imagen = None

    # ======================================================
    # POST
    # ======================================================

    if request.method == "POST":

        consulta = request.form.get(
            "consulta",
            ""
        ).strip()

        imagen = request.files.get("imagen")

        # ==================================================
        # VARIABLES GENERALES
        # ==================================================

        categorias = None
        ticket = None
        regla = None

        informacion = None
        similitud = None

        categoria_predicha = None
        similitud_clase = None

        ruta = None

        representaciones = None
        semana08 = None
        semana09 = None

        imagen_url = None


        # ==================================================
        # PROCESAR CONSULTA TEXTUAL
        # ==================================================

        if consulta:

            # ==============================================
            # TAXONOMIA
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

            (
                informacion,
                similitud
            ) = recuperar_informacion(
                consulta
            )


            # ==============================================
            # CLASIFICADOR CSV
            # ==============================================

            (
                categoria_predicha,
                similitud_clase
            ) = clasificar_csv(
                consulta
            )


            # ==============================================
            # A*
            # ==============================================

            ruta = astar()


            # ==============================================
            # SEMANA 7
            # ==============================================

            representaciones = analizar_representaciones(
                criticidad=ticket["criticidad"],
                impacto=ticket["impacto"],
                tipo=ticket["tipo"]
            )


            # ==============================================
            # SEMANA 8
            # ==============================================

            semana08 = analizar_semana08(
                consulta
            )


        # ==================================================
        # SEMANA 9 - PROCESAMIENTO DE IMAGEN
        # ==================================================
        # Se procesa independientemente de la consulta
        # textual.
        # ==================================================

        if imagen and imagen.filename:

            nombre_original = secure_filename(
                imagen.filename
            )


            # ==============================================
            # VALIDAR EXTENSION
            # ==============================================

            if extension_permitida(
                nombre_original
            ):

                extension = (
                    nombre_original
                    .rsplit(".", 1)[1]
                    .lower()
                )


                # ==========================================
                # GENERAR NOMBRE UNICO
                # ==========================================

                nombre_guardado = (
                    f"{uuid.uuid4().hex}.{extension}"
                )


                ruta_imagen = (
                    UPLOAD_FOLDER
                    / nombre_guardado
                )


                # ==========================================
                # GUARDAR IMAGEN
                # ==========================================

                imagen.save(
                    str(ruta_imagen)
                )


                # ==========================================
                # ANALIZAR SEMANA 9
                # ==========================================

                try:

                    semana09 = analizar_semana09(
                        str(ruta_imagen),
                        sigma=2.0
                    )

                    # ======================================
                    # URL PARA MOSTRAR IMAGEN
                    # ======================================

                    imagen_url = url_for(
                        "static",
                        filename=(
                            f"uploads/{nombre_guardado}"
                        )
                    )

                    if semana09 is None:
                        semana09 = {}

                    semana09["imagen_url"] = imagen_url


                except Exception as error:

                    error_imagen = (
                        "Ocurrio un error al analizar "
                        f"la imagen: {str(error)}"
                    )


            else:

                error_imagen = (
                    "Formato de imagen no permitido. "
                    "Use PNG, JPG o JPEG."
                )


        # ==================================================
        # RESULTADO GENERAL
        # ==================================================

        if consulta or (imagen and imagen.filename):

            resultado = {

                # Consulta
                "consulta":
                    consulta,

                # Taxonomia
                "categorias":
                    categorias,

                # Ticket
                "ticket":
                    ticket,

                # Sistema experto
                "regla":
                    regla,

                # Recuperacion
                "informacion":
                    informacion,

                "similitud":
                    similitud,

                # Clasificacion
                "categoria_predicha":
                    categoria_predicha,

                "similitud_clase":
                    similitud_clase,

                # A*
                "ruta":
                    ruta,

                # Semana 7
                "representaciones":
                    representaciones,

                # Semana 8
                "semana08":
                    semana08,

                # Semana 9
                "semana09":
                    semana09
            }


    # ======================================================
    # RENDERIZAR PAGINA
    # ======================================================

    return render_template(
        "index.html",
        resultado=resultado,
        error_imagen=error_imagen
    )


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )