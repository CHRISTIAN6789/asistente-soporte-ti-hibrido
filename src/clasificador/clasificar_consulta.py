import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

datos = pd.read_csv("data/consultas.csv")
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
consulta = ["La impresora no funciona"]

# Predicción
prediccion = modelo.predict(consulta)

print("Consulta:", consulta[0])
print("Categoría:", prediccion[0])