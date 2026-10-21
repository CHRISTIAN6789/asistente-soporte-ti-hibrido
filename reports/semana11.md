# Semana 11 - Benchmark de Modelos de Inteligencia Artificial- Christian Felipe Alea Agudelo - Andres Esteban Cruz - S10A

## Proyecto: Asistente Inteligente de Soporte TI

### Integrante

- Christian Felipe Alea Agudelo

---

# Objetivo

Implementar un proceso de benchmarking para comparar diferentes modelos de aprendizaje automático y determinar cuál presenta el mejor desempeño para tareas de clasificación.

La evaluación se realizó utilizando:

- Logistic Regression
- Random Forest
- Multi Layer Perceptron (MLP)

Las métricas utilizadas fueron:

- Accuracy
- Tiempo de entrenamiento
- Tiempo de predicción

---

# Introducción

En las semanas anteriores se desarrollaron los diferentes módulos del Asistente Inteligente de Soporte TI:

```text
Semana 7
Representaciones del reconocimiento

Semana 8
MLP
SQLite
Ontología

Semana 9
Canny
Otsu
Regiones conectadas

Semana 10
Histogramas
LBP
Vectores de características
```

La Semana 11 incorpora una etapa de evaluación comparativa de modelos de Inteligencia Artificial mediante benchmark.

El propósito es medir de manera objetiva el rendimiento de diferentes algoritmos bajo las mismas condiciones de entrenamiento y prueba.

---

# Flujo de Benchmark

El flujo desarrollado es:

```text
Dataset
   ↓
Entrenamiento
   ↓
Predicción
   ↓
Accuracy
   ↓
Benchmark
   ↓
Selección del mejor modelo
```

---

# Modelos Evaluados

## Logistic Regression

Modelo lineal ampliamente utilizado para clasificación supervisada.

### Ventajas

- Bajo costo computacional.
- Entrenamiento rápido.
- Fácil interpretación.

---

## Random Forest

Modelo basado en múltiples árboles de decisión.

### Ventajas

- Alta precisión.
- Robustez frente al ruido.
- Buena capacidad de generalización.

---

## Multi Layer Perceptron (MLP)

Red neuronal multicapa utilizada para aprendizaje supervisado.

### Ventajas

- Modela relaciones no lineales.
- Flexible.
- Permite aprender patrones complejos.

---

# Implementación

Se desarrolló:

```text
src/
└── semana11_benchmark.py
```

El módulo ejecuta:

```python
LogisticRegression()

RandomForestClassifier()

MLPClassifier()
```

Posteriormente calcula:

```text
Accuracy
Tiempo de entrenamiento
Tiempo de predicción
```

y genera:

```text
artifacts/
└── benchmark.csv
```

---

# Resultados Obtenidos

## Logistic Regression

```text
Accuracy:
96.85 %

Tiempo de entrenamiento:
0.1774 s

Tiempo de predicción:
0.0005 s
```

---

## Random Forest

```text
Accuracy:
97.59 %

Tiempo de entrenamiento:
0.4835 s

Tiempo de predicción:
0.0208 s
```

---

## MLP

```text
Accuracy:
96.67 %

Tiempo de entrenamiento:
1.3260 s

Tiempo de predicción:
0.0011 s
```

---

# Comparación General

| Modelo | Accuracy | Entrenamiento | Predicción |
|----------|----------|----------|----------|
| Logistic Regression | 96.85 % | 0.1774 s | 0.0005 s |
| Random Forest | 97.59 % | 0.4835 s | 0.0208 s |
| MLP | 96.67 % | 1.3260 s | 0.0011 s |

---

# Mejor Modelo

Resultado obtenido:

```text
Random Forest
```

Accuracy alcanzado:

```text
97.59 %
```

### Interpretación

El benchmark permitió comparar los algoritmos bajo las mismas condiciones de entrenamiento y prueba.

Los resultados muestran que:

```text
Random Forest
```

obtuvo la mayor precisión sobre el conjunto de prueba utilizado.

Aunque Logistic Regression presentó menores tiempos de ejecución, Random Forest alcanzó un mejor equilibrio entre precisión y capacidad de generalización.

---

# Integración con el Proyecto

La Semana 11 fue integrada completamente al Asistente Inteligente de Soporte TI.

Arquitectura actual:

```text
Usuario
   │
   ├── Consulta
   │       ↓
   │   Semana 7
   │   Semana 8
   │
   └── Imagen
           ↓
       Semana 9
           ↓
       Semana 10
           ↓
       Semana 11
```

El benchmark se ejecuta automáticamente y presenta los resultados en la interfaz web.

---

# Evidencia Generada

Archivo generado:

```text
artifacts/
└── benchmark.csv
```

Contenido:

```text
Modelo
Accuracy
Tiempo de entrenamiento
Tiempo de predicción
```

---

# Resultados Relevantes

```text
Mejor modelo:
Random Forest

Accuracy:
97.59 %

Archivo:
benchmark.csv
```

---

# Validación

## Realizado

- [x] Implementación del benchmark.
- [x] Comparación de tres modelos.
- [x] Cálculo de Accuracy.
- [x] Medición de tiempos de entrenamiento.
- [x] Medición de tiempos de predicción.
- [x] Generación automática de benchmark.csv.
- [x] Integración con Flask.
- [x] Integración con la interfaz web.

---

## Funciona

El sistema ejecuta correctamente el benchmark y genera automáticamente las métricas de rendimiento.

---

## Coincide

Los resultados obtenidos corresponden con los objetivos planteados para la Semana 11:

- Comparación de modelos.
- Evaluación de desempeño.
- Benchmark.
- Selección de la mejor alternativa.

---

# Conclusión

La Semana 11 permitió evaluar objetivamente el rendimiento de distintos modelos de Inteligencia Artificial mediante un benchmark controlado. Los resultados demostraron que Random Forest obtuvo el mejor desempeño alcanzando una precisión de 97.59 %, superando a Logistic Regression y MLP en el conjunto de prueba utilizado. La integración de esta evaluación dentro del Asistente Inteligente de Soporte TI aporta evidencia cuantitativa para la selección de modelos y fortalece la toma de decisiones basada en métricas reales de rendimiento.

---

# Evidencias de Entrega

```text
src/
└── semana11_benchmark.py

artifacts/
└── benchmark.csv

src/web/
├── app.py
├── templates/index.html
└── static/style.css

reports/
└── semana11.md
```