# Semana 10 - Reconocimiento Mediante Características - Christian Felipe Alea Agudelo - Andres Esteban Cruz - S10A

## Proyecto: Asistente Inteligente de Soporte TI


# Objetivo

Implementar un módulo de reconocimiento mediante características para complementar el análisis visual desarrollado en la Semana 9.

El objetivo consiste en transformar una imagen en una representación numérica que permita describir sus propiedades mediante:

- Histogramas de intensidad.
- Estadísticas de regiones conectadas.
- Descriptores de textura LBP (Local Binary Patterns).
- Vector final de características.

---

# Introducción

Durante la Semana 9 se realizó el procesamiento básico de imágenes utilizando:

- Conversión a escala de grises.
- Detección de contornos mediante Canny.
- Segmentación automática utilizando Otsu.
- Análisis de regiones conectadas.

La Semana 10 amplía este proceso mediante la generación de características que describen cuantitativamente la evidencia visual utilizada dentro del Asistente Inteligente de Soporte TI.

Estas características constituyen la base para futuros algoritmos de reconocimiento, clasificación y aprendizaje automático.

---

# Flujo General

El flujo implementado fue el siguiente:

```text
Imagen
   ↓
Escala de grises
   ↓
Histograma de intensidades
   ↓
Segmentación Otsu
   ↓
Regiones conectadas
   ↓
Texturas LBP
   ↓
Vector de características
```

---

# Histograma de Intensidad

Se construyó un histograma normalizado utilizando 32 divisiones (bins), permitiendo representar la distribución de intensidades presentes en la imagen.

Archivo generado:

```text
artifacts/semana10_histograma.png
```

El histograma permite:

- Analizar contraste.
- Identificar zonas oscuras y claras.
- Representar la distribución de niveles de intensidad.
- Generar características para clasificación posterior.

Resultado:

```text
✅ Histograma generado correctamente
```

---

# Segmentación y Regiones Conectadas

A partir de la máscara obtenida mediante Otsu se calcularon estadísticas regionales.

Resultados:

```text
Regiones detectadas : 27

Área media          : 1047.44 px

Desviación estándar : 5334.08 px
```

### Interpretación

Las regiones conectadas representan agrupaciones de píxeles pertenecientes a la misma estructura visual.

La elevada desviación estándar indica que existen regiones con tamaños muy diferentes entre sí, donde una región principal concentra gran parte de los píxeles segmentados y el resto corresponde a componentes pequeños.

---

# Descriptores de Textura LBP

Se aplicó Local Binary Pattern (LBP) para caracterizar las texturas presentes en la evidencia visual.

Configuración utilizada:

```text
Radio = 2

Puntos = 16
```

Los patrones binarios locales permiten:

- Describir texturas superficiales.
- Capturar características locales.
- Complementar la información geométrica obtenida mediante regiones conectadas.

Resultado:

```text
Radio utilizado : 2

Puntos utilizados : 16
```

---

# Vector de Características

Las características obtenidas fueron integradas en una única representación numérica.

Estructura del vector:

```text
Regiones

+
Histograma

+
LBP

=
Vector final
```

Dimensión obtenida:

```text
53 características
```

Archivo generado:

```text
artifacts/semana10_features.npy
```

Resultado:

```text
✅ Vector generado correctamente
```

---

# Integración con el Proyecto

La Semana 10 fue integrada directamente al Asistente Inteligente de Soporte TI.

Flujo actualizado:

```text
Usuario
   │
   ├── Consulta textual
   │       ↓
   │   Semana 7
   │   Semana 8
   │
   └── Evidencia visual
            ↓
        Semana 9
            ↓
        Semana 10
```

El usuario adjunta una imagen desde la aplicación web y el sistema genera automáticamente:

```text
Histograma
↓
Regiones
↓
LBP
↓
Vector de características
```

sin necesidad de procesos manuales adicionales.

---

# Resultados Obtenidos

```text
Histograma:
Generado correctamente

Archivo:
semana10_histograma.png


Regiones:
27

Área media:
1047.44 px

Desviación estándar:
5334.08 px


LBP:
Radio = 2

Puntos = 16


Vector final:
53 características

Archivo:
semana10_features.npy
```

---

# Evidencias Generadas

```text
artifacts/

├── semana09_vision.png

├── semana10_histograma.png

└── semana10_features.npy
```

---

# Validación

## Realizado

- [x] Histograma generado.
- [x] Estadísticas regionales calculadas.
- [x] Descriptores LBP generados.
- [x] Vector de características construido.
- [x] Integración con Flask realizada.
- [x] Integración con la interfaz web completada.

## Funciona

El sistema genera automáticamente todas las características visuales a partir de la evidencia adjunta por el usuario.

## Coincide

Los resultados corresponden a los conceptos desarrollados durante la Semana 10:

- Histogramas.
- Regiones conectadas.
- Local Binary Patterns (LBP).
- Vectores de características.

---

# Limitaciones

- El vector generado describe la imagen, pero no clasifica automáticamente el incidente.
- Las características dependen de la calidad de la evidencia visual.
- Cambios importantes de iluminación pueden afectar el histograma.
- LBP describe textura, pero no identifica objetos específicos.
- Las regiones conectadas dependen directamente de la segmentación obtenida mediante Otsu.

---

# Conclusión

La Semana 10 permitió transformar la evidencia visual del Asistente Inteligente de Soporte TI en una representación numérica estructurada. A partir del histograma de intensidad, las estadísticas de regiones conectadas y los descriptores de textura LBP fue posible construir un vector de 53 características que resume los elementos más relevantes de la imagen. Esta representación constituye la base para futuras etapas de clasificación automática, reconocimiento visual y aprendizaje automático dentro del proyecto.

---

# Archivos Relacionados

```text
src/

├── semana10_caracteristicas.py

├── semana09_vision.py

└── web/
    ├── app.py
    ├── templates/index.html
    └── static/style.css


reports/

└── semana10.md


artifacts/

├── semana09_vision.png

├── semana10_histograma.png

└── semana10_features.npy
```