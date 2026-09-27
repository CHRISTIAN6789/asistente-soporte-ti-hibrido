# Semana 08 - Representaciones del Reconocimiento- Christian Felipe Alea Agudelo - Andres Esteban Cruz - S10A

## Proyecto: Asistente Inteligente de Soporte TI Híbrido

---

## 1. Introducción

Durante la Semana 08 se amplió el proyecto **Asistente Inteligente de Soporte TI Híbrido** mediante la integración de tres componentes relacionados con las representaciones del reconocimiento:

1. Red neuronal artificial.
2. Base de datos SQLite para almacenamiento de evidencia.
3. Ontología para representar conceptos y relaciones del dominio.

La finalidad de esta práctica es comprender que un sistema de reconocimiento no debería limitarse únicamente a producir una predicción.

El proceso completo debe permitir reconocer un patrón, conservar evidencia del procesamiento realizado e interpretar el resultado dentro del dominio del problema.

Por esta razón, la idea general de la implementación puede resumirse como:

```text
MODELO RECONOCE
       ↓
BASE DE DATOS REGISTRA
       ↓
ONTOLOGIA INTERPRETA
```

En el proyecto desarrollado, el ejemplo genérico de reconocimiento de dígitos fue adaptado al dominio de **Soporte TI**, utilizando consultas relacionadas con incidentes tecnológicos.

---

# 2. Objetivo

El objetivo de la Semana 08 fue integrar un mecanismo de reconocimiento basado en una red neuronal con componentes que permitieran almacenar evidencia e interpretar semánticamente sus resultados.

Específicamente se buscó:

- Entrenar una red neuronal MLP.
- Utilizar consultas reales del dominio de soporte tecnológico.
- Transformar texto a características numéricas mediante TF-IDF.
- Dividir los datos entre entrenamiento y prueba.
- Evaluar el modelo mediante accuracy.
- Persistir el modelo entrenado.
- Persistir el vectorizador TF-IDF.
- Registrar evidencia mediante SQLite.
- Crear una ontología de Soporte TI.
- Exportar dicha ontología a GraphML.
- Relacionar las predicciones con conceptos propios del proyecto.
- Integrar Semana 08 con el sistema acumulativo.
- Mostrar los resultados en la interfaz web.

---

# 3. Adaptación al Proyecto

El ejemplo presentado durante la clase utiliza imágenes de dígitos escritos a mano.

En este proyecto no se utilizó literalmente dicho ejemplo.

La práctica fue adaptada al objetivo del **Asistente Inteligente de Soporte TI Híbrido**.

En lugar de reconocer dígitos, la red neuronal reconoce categorías asociadas a incidentes tecnológicos.

El flujo adaptado es:

```text
Consulta de Soporte TI
        ↓
TF-IDF
        ↓
Vector numérico
        ↓
Red Neuronal MLP
        ↓
Categoría predicha
        ↓
SQLite
        ↓
Evidencia
        ↓
Ontología
        ↓
Interpretación del dominio
```

Por ejemplo:

```text
VPN no conecta
      ↓
TF-IDF
      ↓
MLP
      ↓
Red
      ↓
SQLite
      ↓
Evidencia
      ↓
Ontología
      ↓
Equipo_Redes
```

De esta manera, la Semana 08 mantiene relación directa con las funcionalidades desarrolladas previamente.

---

# 4. Dataset Utilizado

Para entrenar el modelo se utilizó:

```text
data/consultas.csv
```

El conjunto de datos fue ampliado hasta contar con:

```text
56 consultas
```

Las consultas fueron distribuidas entre siete categorías:

```text
Acceso
Correo
Hardware
Infraestructura
Red
Seguridad
Software
```

Se utilizaron ocho ejemplos para cada categoría.

La distribución fue:

```text
Acceso             8
Correo             8
Hardware           8
Infraestructura    8
Red                 8
Seguridad           8
Software            8
---------------------
Total              56
```

Esta organización permite trabajar con un conjunto equilibrado entre las categorías utilizadas por el clasificador.

---

# 5. Representación del Texto mediante TF-IDF

Una red neuronal necesita recibir valores numéricos como entrada.

Como las consultas del proyecto están escritas en lenguaje natural, fue necesario transformar el texto a una representación numérica.

Para realizar esta transformación se utilizó:

```python
TfidfVectorizer
```

El proceso puede representarse como:

```text
"vpn no conecta"
        ↓
TF-IDF
        ↓
Vector numérico
        ↓
MLP
```

Después de procesar las 56 consultas, el vectorizador produjo:

```text
119 características TF-IDF
```

Cada característica representa información obtenida del vocabulario presente en el conjunto de consultas.

El vectorizador también fue almacenado para poder transformar futuras consultas de la misma manera utilizada durante el entrenamiento.

El archivo generado fue:

```text
artifacts/vectorizador_tfidf.pkl
```

---

# 6. División entre Entrenamiento y Prueba

Para evaluar la capacidad del modelo de trabajar con información diferente a la utilizada directamente durante el aprendizaje, el dataset fue dividido en dos grupos.

Se utilizó:

```python
train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)
```

La distribución obtenida fue:

```text
Datos totales:          56
Entrenamiento:          42
Prueba:                 14
```

Por lo tanto:

```text
75 % → Entrenamiento
25 % → Prueba
```

Además se utilizó:

```python
stratify=y
```

para conservar una distribución equilibrada de las diferentes categorías entre entrenamiento y prueba.

El uso de conjuntos distintos permite evaluar mejor si el modelo está aprendiendo patrones que pueden aplicarse a datos que no fueron utilizados directamente durante el entrenamiento.

---

# 7. Red Neuronal MLP

Para realizar el reconocimiento se utilizó una red neuronal mediante:

```python
MLPClassifier
```

MLP significa:

**Multilayer Perceptron**

o:

**Perceptrón Multicapa**.

Dentro del proyecto, la arquitectura implementada utiliza:

```python
MLPClassifier(
    hidden_layer_sizes=(32,),
    max_iter=600,
    random_state=42
)
```

El funcionamiento conceptual puede representarse como:

```text
119 características TF-IDF
            ↓
       Red Neuronal
            ↓
      Capa oculta
            ↓
 Categoría de Soporte TI
```

La red intenta aprender relaciones entre las características presentes en las consultas y las categorías correctas.

---

# 8. Entrenamiento

El entrenamiento se realiza mediante:

```python
modelo.fit(
    X_train,
    y_train
)
```

Durante este proceso, el modelo utiliza:

```text
X_train
```

como información de entrada y:

```text
y_train
```

como las categorías correctas.

Conceptualmente:

```text
Consultas conocidas
        ↓
TF-IDF
        ↓
Características
        ↓
MLP
        ↓
Comparación con categoría real
        ↓
Ajuste interno del modelo
```

El objetivo es que posteriormente el modelo pueda reconocer correctamente consultas nuevas.

---

# 9. Evaluación del Modelo

Después del entrenamiento se utilizaron los 14 registros reservados para prueba.

Las predicciones fueron comparadas contra las categorías reales mediante:

```python
accuracy_score()
```

El resultado obtenido durante la ejecución final fue:

```text
Accuracy MLP: 0.6429
```

Esto equivale aproximadamente a:

```text
64.29 %
```

Por lo tanto, el modelo clasificó correctamente aproximadamente el 64.29 % del conjunto utilizado para prueba.

Este resultado no significa que el modelo sea perfecto.

El desempeño puede estar condicionado por factores como:

- Tamaño relativamente pequeño del dataset.
- Cantidad de ejemplos disponibles por categoría.
- Similitud entre las palabras utilizadas en diferentes categorías.
- Variaciones del lenguaje natural.
- Cantidad de características TF-IDF.
- Arquitectura de la red neuronal.

Esta limitación constituye una oportunidad para mejorar el sistema mediante un conjunto de entrenamiento más grande y diverso.

---

# 10. Persistencia del Modelo

Después de entrenar la red neuronal, el modelo fue almacenado utilizando `pickle`.

El archivo generado es:

```text
artifacts/modelo_soporte_mlp.pkl
```

También se almacenó el vectorizador TF-IDF:

```text
artifacts/vectorizador_tfidf.pkl
```

Esto permite separar dos procesos:

```text
ENTRENAMIENTO
     ↓
Generación del modelo
     ↓
Archivo .pkl
```

y posteriormente:

```text
Consulta nueva
     ↓
Cargar vectorizador
     ↓
Cargar modelo
     ↓
Realizar predicción
```

Gracias a esta separación, el sistema principal y la interfaz web pueden reutilizar el modelo sin entrenarlo nuevamente cada vez que un usuario realiza una consulta.

---

# 11. Base de Datos SQLite

La segunda parte de la Semana 08 corresponde al almacenamiento de evidencia persistente.

Para este propósito se creó:

```text
artifacts/incidentes_soporte.db
```

La base utiliza SQLite.

Dentro de la base se creó una tabla denominada:

```text
incidentes
```

La información registrada incluye:

```text
id
consulta
categoria_real
categoria_predicha
origen
```

Se almacenaron:

```text
56 registros
```

El esquema conceptual es:

```text
Consulta
     ↓
Categoría real
     ↓
Predicción del modelo
     ↓
SQLite
```

La base permite conservar información relacionada con los datos utilizados y con las predicciones producidas por el modelo.

---

# 12. Importancia de la Evidencia

Una predicción aislada no proporciona toda la información necesaria para analizar el funcionamiento de un sistema inteligente.

Por ejemplo, el modelo puede indicar:

```text
Correo
```

Pero también es importante poder identificar:

```text
¿Qué consulta se utilizó?
¿Cuál era la categoría correcta?
¿Qué categoría predijo el modelo?
¿De dónde proviene el registro?
```

SQLite proporciona un mecanismo sencillo para conservar esta evidencia.

Por esta razón puede resumirse esta parte como:

```text
MODELO
   ↓
PREDICCION
   ↓
SQLITE
   ↓
EVIDENCIA
```

---

# 13. Ontología de Soporte TI

La tercera parte implementada corresponde a una ontología adaptada al dominio del proyecto.

La ontología se construyó utilizando:

```python
networkx
```

y un grafo dirigido:

```python
nx.DiGraph()
```

Los nodos representan conceptos del dominio y las aristas representan relaciones con significado.

Algunos conceptos utilizados son:

```text
Asistente_Soporte_TI
Incidente
Modelo_MLP
Prediccion
Categoria_Soporte
Red
Correo
Infraestructura
Seguridad
Acceso
Hardware
Software
Equipo_Redes
Mesa_Ayuda
Administrador_Servidores
Equipo_Seguridad
```

La implementación supera el mínimo de cinco conceptos propios requerido para la adaptación del proyecto.

---

# 14. Relaciones Ontológicas

La ontología contiene relaciones que pueden interpretarse como frases.

Algunos ejemplos son:

```text
Asistente_Soporte_TI
    → analiza
    → Incidente
```

```text
Modelo_MLP
    → clasifica
    → Incidente
```

```text
Modelo_MLP
    → produce
    → Prediccion
```

```text
Incidente
    → puede_pertenecer_a
    → Red
```

```text
Incidente
    → puede_pertenecer_a
    → Correo
```

```text
Incidente
    → puede_pertenecer_a
    → Seguridad
```

```text
Red
    → se_escala_a
    → Equipo_Redes
```

```text
Correo
    → se_escala_a
    → Mesa_Ayuda
```

```text
Infraestructura
    → se_escala_a
    → Administrador_Servidores
```

```text
Seguridad
    → se_escala_a
    → Equipo_Seguridad
```

La ejecución final generó:

```text
18 relaciones ontológicas
```

De esta manera se supera el requisito de incorporar al menos cinco relaciones propias del dominio del proyecto.

---

# 15. Exportación de la Ontología

Después de construir el grafo, la ontología se exporta al formato GraphML.

El archivo generado es:

```text
artifacts/ontologia_soporte.graphml
```

Este archivo mantiene de forma persistente los conceptos y relaciones creados durante la práctica.

El proceso puede resumirse:

```text
Conceptos
    +
Relaciones
    ↓
NetworkX
    ↓
Grafo dirigido
    ↓
GraphML
```

---

# 16. Integración entre Predicción y Ontología

Una característica importante de la implementación consiste en conectar la categoría producida por la MLP con los conceptos de la ontología.

Por ejemplo, una consulta relacionada con correo puede producir:

```text
Consulta
    ↓
TF-IDF
    ↓
MLP
    ↓
Correo
```

Después, la ontología permite interpretar:

```text
Correo
    ↓ se_escala_a
Mesa_Ayuda
```

Con esto el sistema no solamente responde:

```text
Categoría = Correo
```

sino que puede conectar la categoría con información adicional del dominio.

---

# 17. Prueba Visual Realizada

Durante las pruebas de la interfaz web se procesó una consulta clasificada por la red neuronal como:

```text
Correo
```

La interfaz mostró:

```text
Categoría predicha:       Correo
Confianza MLP:            98.25 %
Accuracy del modelo:      64.29 %
Base SQLite:              incidentes_soporte.db
Registros almacenados:    56
Ontología:                ontologia_soporte.graphml
Relaciones ontológicas:   18
Escalamiento sugerido:    Mesa_Ayuda
```

La relación ontológica mostrada fue:

```text
Correo
   ↓ se_escala_a
Mesa_Ayuda
```

Esta prueba permitió comprobar que los tres componentes estaban integrados correctamente con la interfaz.

---

# 18. Prueba con VPN

Durante la ejecución independiente de Semana 08 también se utilizó:

```text
vpn no conecta
```

La red neuronal produjo:

```text
Red
```

El recorrido conceptual fue:

```text
vpn no conecta
      ↓
TF-IDF
      ↓
MLP
      ↓
Red
      ↓
Ontología
      ↓
Equipo_Redes
```

Esta prueba demuestra que la predicción puede relacionarse con información propia del dominio mediante la ontología.

---

# 19. Integración con el Proyecto Acumulativo

Semana 08 no fue desarrollada como una aplicación independiente.

La funcionalidad fue incorporada al proyecto acumulativo.

Actualmente el flujo general puede representarse como:

```text
Consulta del usuario
        ↓
Taxonomía IA
        ↓
Clasificación del Ticket
        ↓
Sistema Experto
        ↓
Recuperación de Información
        ↓
Clasificación Inteligente
        ↓
A*
        ↓
Minimax
        ↓
Semana 7
        ↓
Representación Numérica
Representación Simbólica
Autómata
        ↓
Semana 8
        ↓
Red Neuronal MLP
SQLite
Ontología
```

Esto permite mantener la evolución progresiva del sistema híbrido.

---

# 20. Integración con main.py

El archivo:

```text
src/main.py
```

fue actualizado para importar:

```python
from semana08_red_ontologia import analizar_semana08
```

Posteriormente puede analizar la consulta mediante:

```python
resultado_semana08 = analizar_semana08(
    consulta
)
```

Esta función carga los artefactos previamente generados y devuelve información relacionada con:

- Categoría predicha.
- Confianza de la predicción.
- Accuracy del modelo.
- Base SQLite.
- Número de registros.
- Ontología.
- Número de relaciones.
- Escalamiento ontológico.

Esta organización evita duplicar la lógica de Semana 08 dentro del programa principal.

---

# 21. Integración con Flask

La Semana 08 también fue integrada con:

```text
src/web/app.py
```

La aplicación importa:

```python
from semana08_red_ontologia import analizar_semana08
```

Cuando el usuario envía una consulta desde la página web, Flask ejecuta:

```python
semana08 = analizar_semana08(
    consulta
)
```

Los resultados son enviados al HTML mediante:

```python
"semana08": semana08
```

De esta manera, la interfaz puede mostrar dinámicamente los resultados del reconocimiento neuronal, SQLite y la ontología.

---

# 22. Integración con la Interfaz Web

En:

```text
src/web/templates/index.html
```

se añadió una sección denominada:

```text
Semana 8 - Reconocimiento Inteligente
```

La sección presenta tres tarjetas.

## Tarjeta 1: Red Neuronal MLP

Presenta:

- Categoría predicha.
- Confianza.
- Accuracy.
- Modelo utilizado.
- Vectorizador utilizado.
- Flujo de reconocimiento.

Visualmente:

```text
Consulta
   ↓
TF-IDF
   ↓
MLP
   ↓
Categoría
```

## Tarjeta 2: Evidencia SQLite

Presenta:

- Nombre de la base.
- Número de registros.
- Estado de la evidencia.

Además representa:

```text
Consulta
   ↓
Categoría
   ↓
Predicción
   ↓
SQLite
```

## Tarjeta 3: Ontología

Presenta:

- Archivo GraphML.
- Número de relaciones.
- Escalamiento sugerido.
- Relaciones relacionadas con la categoría.

Por ejemplo:

```text
Correo
  ↓ se_escala_a
Mesa_Ayuda
```

---

# 23. Flujo Completo de Semana 08

La implementación final puede representarse como:

```text
Consulta
   ↓
TF-IDF
   ↓
MLP
   ↓
Predicción
   ↓
SQLite
   ↓
Evidencia
   ↓
Ontología
   ↓
Significado
```

La idea puede resumirse mediante:

```text
MLP RECONOCE
SQLITE REGISTRA
ONTOLOGIA INTERPRETA
```

---

# 24. Archivos Generados

La ejecución de Semana 08 produce:

```text
artifacts/
├── modelo_soporte_mlp.pkl
├── vectorizador_tfidf.pkl
├── incidentes_soporte.db
└── ontologia_soporte.graphml
```

### modelo_soporte_mlp.pkl

Contiene la red neuronal entrenada.

### vectorizador_tfidf.pkl

Contiene el vectorizador utilizado para transformar las consultas en características numéricas.

### incidentes_soporte.db

Contiene la evidencia persistente de las consultas y predicciones.

### ontologia_soporte.graphml

Contiene los conceptos y relaciones de la ontología del dominio.

---

# 25. Archivos Creados o Modificados

Para Semana 08 se creó:

```text
src/semana08_red_ontologia.py
```

También se modificaron:

```text
data/consultas.csv
src/main.py
src/web/app.py
src/web/templates/index.html
src/web/static/style.css
```

Y se generaron los artefactos:

```text
artifacts/modelo_soporte_mlp.pkl
artifacts/vectorizador_tfidf.pkl
artifacts/incidentes_soporte.db
artifacts/ontologia_soporte.graphml
```

Finalmente se creó:

```text
reports/semana08.md
```

como documentación de la práctica.

---

# 26. Resultados Finales

Los resultados obtenidos fueron:

```text
Consultas del dataset:        56
Categorías:                    7
Características TF-IDF:      119
Datos de entrenamiento:       42
Datos de prueba:              14
Accuracy MLP:             0.6429
Accuracy porcentual:       64.29 %
Registros SQLite:             56
Relaciones ontológicas:       18
```

Estos resultados corresponden a la ejecución final utilizada para integrar la Semana 08.

---

# 27. Limitaciones

La principal limitación observada corresponde al tamaño del dataset.

Aunque el conjunto fue ampliado hasta 56 consultas, todavía representa una cantidad reducida de ejemplos para una red neuronal.

Actualmente existen solamente ocho ejemplos por categoría.

Otra limitación consiste en que TF-IDF analiza principalmente la importancia de términos dentro del conjunto y no comprende completamente el significado contextual de las oraciones.

Por ejemplo, diferentes formas de expresar el mismo problema pueden producir representaciones distintas.

La red neuronal también presenta un accuracy del 64.29 %, lo que evidencia que todavía existen casos que pueden ser clasificados incorrectamente.

La ontología fue diseñada específicamente para fines académicos y representa una versión simplificada de las relaciones que existirían dentro de una organización real.

Finalmente, SQLite mantiene actualmente información básica sobre las consultas y predicciones, pero podría incorporar mayor trazabilidad.

---

# 28. Posibles Mejoras

Como trabajo futuro se propone aumentar significativamente el número de consultas del dataset.

Por ejemplo:

```text
50 a 100 ejemplos por categoría
```

permitirían disponer de una base de entrenamiento más amplia.

También podrían explorarse diferentes configuraciones de la MLP:

```text
Número de neuronas
Número de capas ocultas
Funciones de activación
Número de iteraciones
Regularización
```

Otra mejora podría consistir en incorporar características adicionales del ticket:

```text
Criticidad
Impacto
Prioridad
Número de usuarios afectados
Servicio afectado
Tiempo de indisponibilidad
```

SQLite podría ampliarse con:

```text
Fecha de análisis
Hora
Confianza del modelo
Prioridad
Área responsable
Estado del ticket
Modelo utilizado
```

La ontología podría incorporar conceptos como:

```text
Servicio
Aplicación
Servidor
Usuario
Sede
Acuerdo_SLA
Impacto
Prioridad
Especialista
Equipo_Soporte
```

Esto permitiría construir una representación más completa del dominio.

---

# 29. Comparación de los Tres Componentes

## Red Neuronal

Pregunta principal:

```text
¿Qué categoría parece corresponder al incidente?
```

Responsabilidad:

```text
RECONOCER
```

Ventaja principal:

Permite aprender patrones a partir de ejemplos.

Limitación principal:

Depende de la cantidad y calidad de los datos utilizados para entrenamiento.

---

## SQLite

Pregunta principal:

```text
¿Qué evidencia existe sobre los datos y las predicciones?
```

Responsabilidad:

```text
REGISTRAR
```

Ventaja principal:

Permite conservar información persistente y consultable.

Limitación principal:

Almacenar información no implica comprender su significado.

---

## Ontología

Pregunta principal:

```text
¿Qué significa la categoría y cómo se relaciona con el dominio?
```

Responsabilidad:

```text
INTERPRETAR
```

Ventaja principal:

Permite representar conceptos y relaciones explícitas.

Limitación principal:

Las relaciones deben definirse previamente y mantenerse conforme evoluciona el dominio.

---

# 30. Conclusiones

La Semana 08 permitió ampliar el **Asistente Inteligente de Soporte TI Híbrido** incorporando reconocimiento mediante redes neuronales, persistencia mediante SQLite y representación semántica mediante una ontología.

La red neuronal MLP permitió aprender patrones a partir de consultas previamente clasificadas y producir nuevas categorías.

El uso de TF-IDF permitió transformar las consultas escritas en lenguaje natural a una representación numérica compatible con la red neuronal.

La evaluación obtuvo un accuracy de 64.29 %, resultado que demuestra que el modelo puede identificar diferentes patrones, pero también evidencia la necesidad de ampliar y mejorar el conjunto de entrenamiento.

La base SQLite permitió conservar 56 registros como evidencia persistente del experimento.

La ontología permitió incorporar significado a las categorías del sistema mediante 18 relaciones propias del dominio de Soporte TI.

La integración de estos tres componentes permitió pasar de una predicción aislada a un proceso más completo:

```text
RECONOCER
   ↓
REGISTRAR
   ↓
INTERPRETAR
```

Finalmente, la integración con `main.py`, Flask, HTML y CSS permitió incorporar Semana 08 directamente al sistema acumulativo y visualizar de forma clara el reconocimiento neuronal, la evidencia almacenada y las relaciones ontológicas.

De esta manera, el proyecto mantiene su enfoque híbrido y continúa integrando diferentes técnicas de Inteligencia Artificial dentro de una misma solución orientada al análisis de incidentes de soporte tecnológico.