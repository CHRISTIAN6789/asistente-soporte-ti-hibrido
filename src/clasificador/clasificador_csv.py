import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def clasificar_csv(consulta):

    datos = pd.read_csv("data/consultas.csv")

    consultas = datos["consulta"].tolist()

    vectorizador = TfidfVectorizer()

    matriz = vectorizador.fit_transform(
        consultas + [consulta]
    )

    similitudes = cosine_similarity(
        matriz[-1:],
        matriz[:-1]
    )

    indice = similitudes.argmax()

    categoria = datos.iloc[indice]["categoria"]

    similitud = similitudes[0][indice]

    return categoria, round(similitud, 4)


