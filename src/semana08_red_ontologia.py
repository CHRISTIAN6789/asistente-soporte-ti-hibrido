from pathlib import Path
import pickle
import sqlite3

import networkx as nx
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


# ==========================================================
# SEMANA 8
# RED NEURONAL + SQLITE + ONTOLOGIA
# ASISTENTE INTELIGENTE DE SOPORTE TI
# ==========================================================


# ==========================================================
# RUTAS DEL PROYECTO
# ==========================================================

ROOT = Path(__file__).resolve().parent.parent

DATA = ROOT / "data"

ARTIFACTS = ROOT / "artifacts"

ARTIFACTS.mkdir(
    parents=True,
    exist_ok=True
)


RUTA_CSV = DATA / "consultas.csv"

RUTA_MODELO = ARTIFACTS / "modelo_soporte_mlp.pkl"

RUTA_VECTORIZADOR = ARTIFACTS / "vectorizador_tfidf.pkl"

RUTA_BD = ARTIFACTS / "incidentes_soporte.db"

RUTA_ONTOLOGIA = ARTIFACTS / "ontologia_soporte.graphml"


# Accuracy obtenido en la ejecucion final de Semana 8
ACCURACY_MODELO = 0.6429


# ==========================================================
# ENTRENAMIENTO SEMANA 8
# ==========================================================

def entrenar_semana08():

    # ------------------------------------------------------
    # 1. CARGAR DATASET
    # ------------------------------------------------------

    datos = pd.read_csv(
        RUTA_CSV
    )

    consultas = datos["consulta"].astype(str)

    categorias = datos["categoria"].astype(str)


    print("=" * 65)
    print("SEMANA 8 - RED NEURONAL + SQLITE + ONTOLOGIA")
    print("=" * 65)


    print("\nDatos cargados:")
    print(len(datos))


    print("\nCategorias disponibles:")

    for categoria in sorted(
        categorias.unique()
    ):
        print("-", categoria)


    # ------------------------------------------------------
    # 2. TF-IDF
    # ------------------------------------------------------

    vectorizador = TfidfVectorizer(
        lowercase=True
    )

    X = vectorizador.fit_transform(
        consultas
    )

    y = categorias


    print("\nCaracteristicas TF-IDF:")
    print(X.shape[1])


    # ------------------------------------------------------
    # 3. ENTRENAMIENTO / PRUEBA
    # ------------------------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )


    print("\nDatos de entrenamiento:")
    print(X_train.shape[0])

    print("Datos de prueba:")
    print(X_test.shape[0])


    # ------------------------------------------------------
    # 4. RED NEURONAL
    # ------------------------------------------------------

    modelo = MLPClassifier(
        hidden_layer_sizes=(32,),
        max_iter=600,
        random_state=42
    )


    modelo.fit(
        X_train,
        y_train
    )


    # ------------------------------------------------------
    # 5. EVALUACION
    # ------------------------------------------------------

    predicciones = modelo.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predicciones
    )


    print("\nAccuracy MLP:")
    print(round(accuracy, 4))


    # ------------------------------------------------------
    # 6. GUARDAR MODELO
    # ------------------------------------------------------

    with RUTA_MODELO.open("wb") as archivo:

        pickle.dump(
            modelo,
            archivo
        )


    with RUTA_VECTORIZADOR.open("wb") as archivo:

        pickle.dump(
            vectorizador,
            archivo
        )


    print("\nModelo guardado:")
    print(RUTA_MODELO.name)


    print("Vectorizador guardado:")
    print(RUTA_VECTORIZADOR.name)


    # ------------------------------------------------------
    # 7. SQLITE
    # ------------------------------------------------------

    with sqlite3.connect(
        RUTA_BD
    ) as conexion:

        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS incidentes (
                id INTEGER PRIMARY KEY,
                consulta TEXT NOT NULL,
                categoria_real TEXT NOT NULL,
                categoria_predicha TEXT NOT NULL,
                origen TEXT NOT NULL
            )
            """
        )

        conexion.execute(
            "DELETE FROM incidentes"
        )

        registros = []

        for indice in range(
            len(consultas)
        ):

            consulta_actual = consultas.iloc[
                indice
            ]

            categoria_real = categorias.iloc[
                indice
            ]

            vector_actual = vectorizador.transform(
                [consulta_actual]
            )

            categoria_predicha = modelo.predict(
                vector_actual
            )[0]

            registros.append(
                (
                    indice,
                    consulta_actual,
                    categoria_real,
                    categoria_predicha,
                    "consultas.csv"
                )
            )


        conexion.executemany(
            """
            INSERT INTO incidentes (
                id,
                consulta,
                categoria_real,
                categoria_predicha,
                origen
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            registros
        )

        conexion.commit()


    print("\nBase SQLite creada:")
    print(RUTA_BD.name)

    print("Registros almacenados:")
    print(len(registros))


    # ------------------------------------------------------
    # 8. ONTOLOGIA DE SOPORTE TI
    # ------------------------------------------------------

    G = nx.DiGraph()


    relaciones = [

        (
            "Asistente_Soporte_TI",
            "Incidente",
            {"rel": "analiza"}
        ),

        (
            "Modelo_MLP",
            "Incidente",
            {"rel": "clasifica"}
        ),

        (
            "Modelo_MLP",
            "Prediccion",
            {"rel": "produce"}
        ),

        (
            "Prediccion",
            "Categoria_Soporte",
            {"rel": "asigna"}
        ),

        (
            "Incidente",
            "Red",
            {"rel": "puede_pertenecer_a"}
        ),

        (
            "Incidente",
            "Correo",
            {"rel": "puede_pertenecer_a"}
        ),

        (
            "Incidente",
            "Infraestructura",
            {"rel": "puede_pertenecer_a"}
        ),

        (
            "Incidente",
            "Seguridad",
            {"rel": "puede_pertenecer_a"}
        ),

        (
            "Incidente",
            "Acceso",
            {"rel": "puede_pertenecer_a"}
        ),

        (
            "Incidente",
            "Hardware",
            {"rel": "puede_pertenecer_a"}
        ),

        (
            "Incidente",
            "Software",
            {"rel": "puede_pertenecer_a"}
        ),

        (
            "Red",
            "Equipo_Redes",
            {"rel": "se_escala_a"}
        ),

        (
            "Correo",
            "Mesa_Ayuda",
            {"rel": "se_escala_a"}
        ),

        (
            "Infraestructura",
            "Administrador_Servidores",
            {"rel": "se_escala_a"}
        ),

        (
            "Seguridad",
            "Equipo_Seguridad",
            {"rel": "se_escala_a"}
        ),

        (
            "Acceso",
            "Mesa_Ayuda",
            {"rel": "se_escala_a"}
        )
    ]


    G.add_edges_from(
        relaciones
    )


    # ------------------------------------------------------
    # 9. EJEMPLO DE PREDICCION
    # ------------------------------------------------------

    consulta_ejemplo = (
        "vpn no conecta"
    )

    vector_ejemplo = vectorizador.transform(
        [consulta_ejemplo]
    )

    clase_predicha = modelo.predict(
        vector_ejemplo
    )[0]


    G.add_edge(
        "Consulta_VPN",
        "Prediccion_VPN",
        rel="genera"
    )


    G.add_edge(
        "Prediccion_VPN",
        str(clase_predicha),
        rel="asigna_clase"
    )


    # ------------------------------------------------------
    # 10. EXPORTAR ONTOLOGIA
    # ------------------------------------------------------

    nx.write_graphml(
        G,
        RUTA_ONTOLOGIA
    )


    print("\nConsulta de ejemplo:")
    print(consulta_ejemplo)


    print("Clase predicha:")
    print(clase_predicha)


    print("\nOntologia creada:")
    print(RUTA_ONTOLOGIA.name)


    print("Relaciones ontologicas:")
    print(G.number_of_edges())


    # ------------------------------------------------------
    # 11. MOSTRAR RELACIONES
    # ------------------------------------------------------

    print(
        "\nEjemplos de relaciones ontologicas:"
    )


    for origen, destino, datos_relacion in list(
        G.edges(data=True)
    )[:8]:

        print(
            origen,
            "->",
            datos_relacion.get(
                "rel",
                "relacion"
            ),
            "->",
            destino
        )


    # ------------------------------------------------------
    # 12. RESUMEN
    # ------------------------------------------------------

    print("\n" + "=" * 65)

    print("ARCHIVOS GENERADOS")

    print("=" * 65)


    print(
        "-",
        RUTA_MODELO.name
    )

    print(
        "-",
        RUTA_VECTORIZADOR.name
    )

    print(
        "-",
        RUTA_BD.name
    )

    print(
        "-",
        RUTA_ONTOLOGIA.name
    )


    print("\n" + "=" * 65)

    print("SEMANA 8 FINALIZADA")

    print("=" * 65)


    return {
        "accuracy": round(
            float(accuracy),
            4
        ),
        "registros": len(registros),
        "relaciones": G.number_of_edges()
    }


# ==========================================================
# ANALIZAR UNA CONSULTA DESDE MAIN.PY O FLASK
# ==========================================================

def analizar_semana08(consulta):

    # ------------------------------------------------------
    # VERIFICAR ARTEFACTOS
    # ------------------------------------------------------

    archivos_requeridos = [
        RUTA_MODELO,
        RUTA_VECTORIZADOR,
        RUTA_BD,
        RUTA_ONTOLOGIA
    ]


    faltantes = [
        archivo.name
        for archivo in archivos_requeridos
        if not archivo.exists()
    ]


    if faltantes:

        raise FileNotFoundError(
            "Faltan artefactos de Semana 8: "
            + ", ".join(faltantes)
            + ". Ejecute primero: "
            + "python src/semana08_red_ontologia.py"
        )


    # ------------------------------------------------------
    # CARGAR MODELO
    # ------------------------------------------------------

    with RUTA_MODELO.open(
        "rb"
    ) as archivo:

        modelo = pickle.load(
            archivo
        )


    # ------------------------------------------------------
    # CARGAR VECTORIZADOR
    # ------------------------------------------------------

    with RUTA_VECTORIZADOR.open(
        "rb"
    ) as archivo:

        vectorizador = pickle.load(
            archivo
        )


    # ------------------------------------------------------
    # TRANSFORMAR CONSULTA
    # ------------------------------------------------------

    vector_consulta = vectorizador.transform(
        [consulta]
    )


    # ------------------------------------------------------
    # PREDICCION MLP
    # ------------------------------------------------------

    categoria_predicha = modelo.predict(
        vector_consulta
    )[0]


    # ------------------------------------------------------
    # CONFIANZA
    # ------------------------------------------------------

    probabilidades = modelo.predict_proba(
        vector_consulta
    )[0]


    confianza = max(
        probabilidades
    )


    # ------------------------------------------------------
    # SQLITE
    # ------------------------------------------------------

    with sqlite3.connect(
        RUTA_BD
    ) as conexion:

        cursor = conexion.execute(
            """
            SELECT COUNT(*)
            FROM incidentes
            """
        )

        registros = cursor.fetchone()[0]


    # ------------------------------------------------------
    # ONTOLOGIA
    # ------------------------------------------------------

    ontologia = nx.read_graphml(
        RUTA_ONTOLOGIA
    )


    relaciones = ontologia.number_of_edges()


    # ------------------------------------------------------
    # ESCALAMIENTO ONTOLOGICO
    # ------------------------------------------------------

    escalamiento = (
        "No definido"
    )


    if categoria_predicha in ontologia:

        for destino in ontologia.successors(
            categoria_predicha
        ):

            datos_relacion = (
                ontologia.get_edge_data(
                    categoria_predicha,
                    destino
                )
            )


            if (
                datos_relacion
                and datos_relacion.get(
                    "rel"
                ) == "se_escala_a"
            ):

                escalamiento = destino

                break


    # ------------------------------------------------------
    # RELACIONES DE LA CATEGORIA
    # ------------------------------------------------------

    relaciones_categoria = []


    if categoria_predicha in ontologia:

        for destino in ontologia.successors(
            categoria_predicha
        ):

            datos = ontologia.get_edge_data(
                categoria_predicha,
                destino
            )

            tipo_relacion = datos.get(
                "rel",
                "relacion"
            )

            relaciones_categoria.append(
                {
                    "origen": categoria_predicha,
                    "relacion": tipo_relacion,
                    "destino": destino
                }
            )


    # ------------------------------------------------------
    # RESULTADO PARA MAIN / FLASK
    # ------------------------------------------------------

    return {

        "consulta": consulta,

        "categoria_predicha":
            str(categoria_predicha),

        "confianza":
            round(
                float(confianza),
                4
            ),

        "confianza_porcentaje":
            round(
                float(confianza) * 100,
                2
            ),

        "accuracy":
            ACCURACY_MODELO,

        "accuracy_porcentaje":
            round(
                ACCURACY_MODELO * 100,
                2
            ),

        "modelo":
            RUTA_MODELO.name,

        "vectorizador":
            RUTA_VECTORIZADOR.name,

        "base_datos":
            RUTA_BD.name,

        "registros":
            registros,

        "ontologia":
            RUTA_ONTOLOGIA.name,

        "relaciones":
            relaciones,

        "escalamiento":
            escalamiento,

        "relaciones_categoria":
            relaciones_categoria
    }


# ==========================================================
# EJECUCION DIRECTA
# ==========================================================

if __name__ == "__main__":

    entrenar_semana08()