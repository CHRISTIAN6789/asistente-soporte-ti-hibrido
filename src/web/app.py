import sys
import os

# Permite acceder a los módulos que están en src
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from flask import Flask, render_template, request

from taxonomia.clasificador_taxonomia import clasificar_taxonomia
from clasificador.clasificar_ticket import clasificar_ticket
from clasificador.clasificador_csv import clasificar_csv

from reglas.motor_reglas import aplicar_reglas
from conocimiento.recuperador_tfidf import recuperar_informacion

from busqueda.astar_soporte import astar


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None

    if request.method == "POST":

        consulta = request.form["consulta"]

        # Taxonomía IA
        categorias = clasificar_taxonomia(
            consulta
        )

        # Clasificación de ticket
        ticket = clasificar_ticket(
            consulta
        )

        # Sistema experto
        regla = aplicar_reglas(
            consulta
        )

        # Recuperación de información
        informacion, similitud = recuperar_informacion(
            consulta
        )

        # Clasificación inteligente
        categoria_predicha, similitud_clase = clasificar_csv(
            consulta
        )

        # A*
        ruta = astar()

        resultado = {
            "consulta": consulta,
            "categorias": categorias,
            "ticket": ticket,
            "regla": regla,
            "informacion": informacion,
            "similitud": similitud,
            "categoria_predicha": categoria_predicha,
            "similitud_clase": similitud_clase,
            "ruta": ruta
        }

    return render_template(
        "index.html",
        resultado=resultado
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )