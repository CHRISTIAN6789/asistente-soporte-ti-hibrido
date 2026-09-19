import os
import sys


# Permite importar los modulos ubicados dentro de src
SRC_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)


from flask import Flask, render_template, request

from taxonomia.clasificador_taxonomia import clasificar_taxonomia
from clasificador.clasificar_ticket import clasificar_ticket
from clasificador.clasificador_csv import clasificar_csv

from reglas.motor_reglas import aplicar_reglas
from conocimiento.recuperador_tfidf import recuperar_informacion

from busqueda.astar_soporte import astar
from semana07_representaciones import analizar_representaciones


app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None

    if request.method == "POST":

        consulta = request.form.get(
            "consulta",
            ""
        ).strip()

        if consulta:

            categorias = clasificar_taxonomia(
                consulta
            )

            ticket = clasificar_ticket(
                consulta
            )

            regla = aplicar_reglas(
                consulta
            )

            informacion, similitud = recuperar_informacion(
                consulta
            )

            categoria_predicha, similitud_clase = clasificar_csv(
                consulta
            )

            ruta = astar()

            representaciones = analizar_representaciones(
                criticidad=ticket["criticidad"],
                impacto=ticket["impacto"],
                tipo=ticket["tipo"]
            )

            resultado = {
                "consulta": consulta,
                "categorias": categorias,
                "ticket": ticket,
                "regla": regla,
                "informacion": informacion,
                "similitud": similitud,
                "categoria_predicha": categoria_predicha,
                "similitud_clase": similitud_clase,
                "ruta": ruta,
                "representaciones": representaciones
            }

    return render_template(
        "index.html",
        resultado=resultado
    )


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )