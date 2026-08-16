import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Cargar datos
datos = pd.read_csv("data/consultas.csv")

# Crear modelo
modelo = Pipeline([
    ("vectorizador", TfidfVectorizer()),
    ("clasificador", MultinomialNB())
])

# Entrenar modelo
modelo.fit(datos["consulta"], datos["categoria"])

# Consulta de prueba
consulta = ["No puedo entrar al sistema"]

# Predicción
prediccion = modelo.predict(consulta)

print("Consulta:", consulta[0])
print("Categoría:", prediccion[0])