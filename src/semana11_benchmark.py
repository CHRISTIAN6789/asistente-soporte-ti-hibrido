import time
import pandas as pd

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score


def analizar_semana11():

    X, y = load_digits(
        return_X_y=True
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42
    )

    modelos = {

        "Logistic Regression":
            LogisticRegression(
                max_iter=3000
            ),

        "Random Forest":
            RandomForestClassifier(
                n_estimators=100,
                random_state=42
            ),

        "MLP":
            MLPClassifier(
                hidden_layer_sizes=(100,),
                max_iter=500,
                random_state=42
            )
    }

    resultados = []

    mejor_modelo = None
    mejor_accuracy = 0

    for nombre, modelo in modelos.items():

        inicio = time.time()

        modelo.fit(
            X_train,
            y_train
        )

        tiempo_entrenamiento = (
            time.time() - inicio
        )

        inicio = time.time()

        pred = modelo.predict(
            X_test
        )

        tiempo_prediccion = (
            time.time() - inicio
        )

        accuracy = accuracy_score(
            y_test,
            pred
        )

        resultados.append({

            "modelo":
                nombre,

            "accuracy":
                round(
                    accuracy * 100,
                    2
                ),

            "tiempo_train":
                round(
                    tiempo_entrenamiento,
                    4
                ),

            "tiempo_pred":
                round(
                    tiempo_prediccion,
                    4
                )
        })

        if accuracy > mejor_accuracy:

            mejor_accuracy = accuracy
            mejor_modelo = nombre

    tabla = pd.DataFrame(
        resultados
    )

    tabla.to_csv(
        "artifacts/benchmark.csv",
        index=False
    )

    return {

        "modelos":
            resultados,

        "mejor_modelo":
            mejor_modelo,

        "mejor_accuracy":
            round(
                mejor_accuracy * 100,
                2
            ),

        "archivo":
            "benchmark.csv"
    }


if __name__ == "__main__":

    resultado = analizar_semana11()

    print(
        "\n===== RESULTADOS BENCHMARK =====\n"
    )

    print(resultado)