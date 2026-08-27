# Semana 03 - Taxonomía de Inteligencia Artificial - Christian Felipe Alea Agudelo - Andres Esteban Cruz - S10A

## Resultado automático frente a clasificación manual

| Caso | Categoría automática | Categorías detectadas | Manual | Estado |
|---|---|---|---|---|
| 1 | Visión por computador | Visión por computador | Visión por computador | Coincide |
| 2 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural, Sistemas de recomendación | Procesamiento de lenguaje natural | Coincide |
| 3 | Aprendizaje automático predictivo | Aprendizaje automático predictivo, Sistemas de recomendación | Aprendizaje automático predictivo | Coincide |
| 4 | Búsqueda y optimización | Búsqueda y optimización | Búsqueda y optimización | Coincide |
| 5 | Sistemas de recomendación | Sistemas de recomendación | Sistemas de recomendación | Coincide |
| 6 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 7 | Visión por computador | Visión por computador | Visión por computador | Coincide |
| 8 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 9 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 10 | Sistemas expertos | Sistemas expertos | Sistemas expertos | Coincide |
| 11 | Visión por computador | Visión por computador | Visión por computador | Coincide |
| 12 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural, Sistemas de recomendación | Procesamiento de lenguaje natural | Coincide |
| 13 | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Coincide |
| 14 | Búsqueda y optimización | Búsqueda y optimización | Búsqueda y optimización | Coincide |
| 15 | Aprendizaje automático predictivo | Aprendizaje automático predictivo, Robótica y sistemas autónomos | Aprendizaje automático predictivo | Coincide |
| 16 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 17 | Visión por computador | Visión por computador, Robótica y sistemas autónomos | Visión por computador | Coincide |
| 18 | Sistemas expertos | Sistemas expertos | Sistemas expertos | Coincide |
| 19 | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Coincide |
| 20 | Búsqueda y optimización | Búsqueda y optimización, Sistemas de recomendación | Búsqueda y optimización | Coincide |

Coincidencia con la referencia: **100.00%**

## Cinco reglas propias

- matricula / matriculas
- sentimiento
- falla / fallas
- sintoma / sintomas
- trayectoria / trayectorias

## Discrepancias y análisis

Durante la ejecución del clasificador se observó que algunos problemas pueden pertenecer simultáneamente a varias áreas de la Inteligencia Artificial. Esto ocurre porque las palabras clave identificadas pueden estar asociadas a más de una categoría.

### Caso 17
Descripción:
"Identificar peatones y señales de tránsito en las imágenes capturadas por un vehículo autónomo."

Palabras detectadas:
- peatones
- señales
- vehículo autónomo
Clasificación automática:
- Visión por computador
- Robótica y sistemas autónomos
Clasificación manual:
- Visión por computador
Análisis:
La clasificación automática detectó correctamente elementos relacionados con visión artificial y robótica. Sin embargo, la clasificación manual prioriza la visión por computador porque la tarea principal consiste en reconocer objetos dentro de imágenes.

Propuesta de mejora:
Asignar diferentes pesos a las palabras clave para determinar con mayor precisión la categoría principal.

### Caso 10
Descripción:

"Construir un sistema que sugiera posibles diagnósticos médicos a partir de síntomas ingresados por un profesional."

Palabras detectadas:

- diagnósticos

- síntomas


Clasificación automática:

- Sistemas expertos
Clasificación manual:

- Sistemas expertos

Análisis:

No se encontraron diferencias significativas. El uso de reglas y conocimiento especializado justifica la clasificación obtenida.
### Observación general
49
 
50
Se evidencia que los problemas reales rara vez pertenecen a una única categoría de Inteligencia Artificial. Un sistema puede combinar técnicas de visión por computador, aprendizaje automático, procesamiento de lenguaje natural, sistemas expertos y robótica para resolver una misma necesidad.

Como mejora futura, se podría implementar un sistema de ponderación que asigne porcentajes de pertenencia a cada categoría detectada, permitiendo representar de forma más precisa la naturaleza híbrida de los problemas de IA.