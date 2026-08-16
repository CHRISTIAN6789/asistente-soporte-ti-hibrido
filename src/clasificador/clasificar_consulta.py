import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

datos = pd.read_csv("data/consultas.csv")

modelo = Pipeline([
    ("vectorizador", TfidfVectorizer()),
    ("clasificador", MultinomialNB())
])

modelo.fit(datos["consulta"], datos["categoria"])

consulta = ["No puedo entrar al sistema"]

prediccion = modelo.predict(consulta)

print("Consulta:", consulta[0])
print("Categoría:", prediccion[0])