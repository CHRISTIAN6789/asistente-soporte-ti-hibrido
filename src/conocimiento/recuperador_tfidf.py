from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recuperar_informacion(consulta):

    with open(
        "data/base_conocimiento.txt",
        "r",
        encoding="utf-8"
    ) as archivo:

        documentos = [
            linea.strip()
            for linea in archivo
            if linea.strip()
        ]

    vectorizador = TfidfVectorizer()

    matriz = vectorizador.fit_transform(
        documentos + [consulta]
    )

    similitudes = cosine_similarity(
        matriz[-1],
        matriz[:-1]
    )

    indice = similitudes.argmax()

    documento = documentos[indice]

    valor_similitud = similitudes[0][indice]

    return documento, round(valor_similitud, 4)