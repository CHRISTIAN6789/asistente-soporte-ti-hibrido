# Semana 9 - Reconocimiento de imágenes-Christian Felipe Alea Agudelo - Andres Esteban Cruz - S10A

## Asistente Inteligente de Soporte TI

### Objetivo

Integrar reconocimiento y procesamiento básico de imágenes al **Asistente Inteligente de Soporte TI**, utilizando una evidencia visual asociada a un incidente. La práctica implementa extracción de características, detección de contornos mediante Canny, segmentación automática mediante Otsu y análisis de regiones conectadas.

La finalidad de esta etapa no es identificar automáticamente el dispositivo ni diagnosticar por sí sola la causa de una falla. El objetivo es convertir una imagen adjunta en **evidencia visual estructurada y medible**, que complemente el análisis textual del incidente.

---

## 1. Imagen utilizada

Para la práctica se utilizó una imagen relacionada con infraestructura de red, representada por un **router o equipo de conectividad**, coherente con el dominio del proyecto de Soporte TI.

La interfaz permite al usuario cargar archivos **PNG, JPG o JPEG**. La imagen se almacena en:

```text
src/web/static/uploads/
```

Para evitar sobrescrituras, Flask genera un nombre único para cada archivo cargado.

En la prueba realizada, la imagen fue normalizada a una resolución de:

```text
360 x 360 píxeles
```

Número total de píxeles:

```text
129600
```

Características de intensidad obtenidas:

```text
Intensidad mínima: 0.0
Intensidad máxima: 1.0
Intensidad media: 0.1894
```

Estos valores demuestran que la imagen fue convertida a una representación numérica adecuada para continuar con las operaciones de visión artificial.

---

## 2. Pipeline de procesamiento visual

El flujo implementado durante la Semana 9 es:

```text
Evidencia visual
      ↓
Escala de grises
      ↓
Extracción de características
      ↓
Canny
      ↓
Detección de contornos
      ↓
Otsu
      ↓
Máscara binaria
      ↓
Regiones conectadas
      ↓
Evidencia estructurada para Soporte TI
```

Este procesamiento permite pasar de una fotografía o captura a información cuantificable sobre intensidad, bordes, segmentación y regiones.

---

## 3. Detección de contornos con Canny

Para detectar los cambios importantes de intensidad presentes en la imagen se utilizó el algoritmo **Canny**.

Configuración utilizada:

```text
Método: Canny
Sigma: 2.0
```

Resultado obtenido:

```text
Píxeles de borde: 2522
Cobertura de bordes: 1.95 %
```

La cobertura indica que aproximadamente el **1.95 % de los píxeles de la imagen fueron identificados como bordes**.

En el caso de la imagen utilizada, los contornos permiten resaltar principalmente la silueta del equipo, las antenas, las separaciones de la carcasa y algunos elementos visibles del dispositivo.

### Interpretación de sigma

El parámetro `sigma` controla el nivel de suavizado aplicado antes de localizar los bordes.

```text
Sigma bajo  → mayor detalle, pero mayor sensibilidad al ruido.
Sigma alto  → mayor suavizado, pero posible pérdida de detalles pequeños.
```

Para la evidencia utilizada se trabajó con:

```text
sigma = 2.0
```

Este valor produjo una representación suficientemente limpia de los límites principales del equipo sin conservar una cantidad excesiva de ruido visual.

---

## 4. Segmentación automática mediante Otsu

Después de analizar los bordes, se utilizó el método de **Otsu** para determinar automáticamente un umbral de intensidad.

Resultado:

```text
Umbral Otsu: 0.416
```

A partir del umbral se construyó una máscara binaria que separa los píxeles considerados objeto de los píxeles considerados fondo.

Resultados de la máscara:

```text
Píxeles objeto: 28281
Píxeles fondo: 101319
Cobertura objeto: 21.82 %
Cobertura fondo: 78.18 %
```

Comprobación:

```text
28281 + 101319 = 129600 píxeles
```

Por lo tanto, la segmentación conserva la totalidad de los píxeles de la imagen y los distribuye en los dos grupos definidos por el umbral.

### Interpretación

El resultado muestra que aproximadamente el **21.82 % de la imagen pertenece al grupo identificado como objeto**, mientras que el **78.18 % corresponde al fondo**.

En la evidencia utilizada, Otsu consigue separar ampliamente la superficie clara del equipo respecto al fondo oscuro.

---

## 5. Regiones conectadas

Una vez obtenida la máscara binaria, se aplicó etiquetado de componentes conectados para identificar grupos de píxeles relacionados espacialmente.

Resultados:

```text
Regiones detectadas: 27
Regiones relevantes: 1
Área mínima del filtro: 100 px
Región mayor: 28246 px
Región menor: 1 px
Área promedio: 1047.44 px
```

El hecho de detectar **27 regiones** no significa que existan 27 objetos reales independientes. Las regiones pequeñas pueden corresponder a fragmentos, detalles visuales, separaciones producidas por la segmentación o ruido.

Por esta razón se utilizó un criterio de relevancia de:

```text
Área mínima = 100 píxeles
```

Después de aplicar este criterio, solamente **1 región** fue considerada significativa. Esta región corresponde a la mayor parte del objeto principal segmentado.

---

## 6. Evidencia visual generada

El módulo genera automáticamente la evidencia:

```text
artifacts/semana09_vision.png
```

La imagen comparativa contiene tres vistas:

1. **Evidencia Original**: imagen utilizada como entrada.
2. **Canny | sigma=2.0**: mapa de contornos detectados.
3. **Segmentación Otsu**: máscara binaria obtenida mediante el umbral automático.

Esta evidencia permite verificar visualmente que los resultados numéricos corresponden al procesamiento realizado.

---

## 7. Integración con el Asistente Inteligente de Soporte TI

La Semana 9 fue integrada a la aplicación Flask existente.

El flujo dentro del sistema queda de la siguiente manera:

```text
Usuario
  │
  ├── Describe incidente
  │        ↓
  │   Análisis textual
  │        ├── Taxonomía
  │        ├── Sistema experto
  │        ├── TF-IDF
  │        ├── Clasificación
  │        ├── A*
  │        ├── Semana 7
  │        └── Semana 8
  │
  └── Adjunta imagen
           ↓
       Semana 9
           ├── Características
           ├── Canny
           ├── Otsu
           └── Regiones conectadas
```

La imagen subida desde la aplicación es almacenada dentro de:

```text
src/web/static/uploads/
```

Posteriormente, `semana09_vision.py` procesa el archivo y genera los valores utilizados por la interfaz para presentar el análisis visual.

De esta manera, el asistente trabaja con **dos fuentes complementarias de evidencia**:

```text
Texto del incidente + Imagen del incidente
```

---

## 8. Estructura de archivos utilizada

La estructura relevante del proyecto para esta semana es:

```text
proyecto/
├── artifacts/
│   └── semana09_vision.png
├── reports/
│   └── semana09.md
├── src/
│   ├── semana09_vision.py
│   └── web/
│       ├── app.py
│       ├── static/
│       │   ├── style.css
│       │   └── uploads/
│       └── templates/
│           └── index.html
└── requirements.txt
```

Esta organización permite separar código, evidencia generada, interfaz web e informe semanal.

---

## 9. Limitaciones observadas

El procesamiento implementado presenta algunas limitaciones importantes:

- Una región conectada no equivale necesariamente a un objeto real.
- Cambios de iluminación pueden modificar el umbral calculado por Otsu.
- Canny puede detectar ruido si el suavizado es insuficiente.
- Un valor de `sigma` demasiado alto puede eliminar detalles útiles.
- La segmentación depende del contraste existente entre el objeto y el fondo.
- La etapa actual no reconoce automáticamente el tipo de dispositivo mostrado.
- El procesamiento visual complementa el diagnóstico, pero no reemplaza la información textual del incidente ni la validación técnica.

Estas limitaciones son importantes porque permiten entender que el procesamiento de imagen actual funciona principalmente como **extracción y estructuración de evidencia**, no como un clasificador visual completo.

---

## 10. Aporte al proyecto final

La integración de Semana 9 amplía el Asistente Inteligente de Soporte TI al incorporar información visual al análisis de incidentes.

Antes de esta implementación, la mayor parte del razonamiento dependía de la descripción textual del usuario. Ahora el sistema puede recibir también una evidencia gráfica, procesarla y obtener datos objetivos sobre sus características visuales.

Las salidas de Canny, Otsu y regiones conectadas pueden utilizarse posteriormente para:

- validar evidencias adjuntas a tickets;
- extraer características visuales adicionales;
- localizar zonas relevantes dentro de una imagen;
- construir descriptores de forma o textura;
- alimentar modelos de clasificación de imágenes;
- comparar evidencias entre incidentes;
- fortalecer la trazabilidad visual del soporte técnico.

---

## 11. Validación de la práctica

### Realizado

- [x] Se implementó `semana09_vision.py`.
- [x] Se utilizó una imagen relacionada con el proyecto.
- [x] Se implementó detección de contornos con Canny.
- [x] Se implementó segmentación automática con Otsu.
- [x] Se analizaron regiones conectadas.
- [x] Se generó `artifacts/semana09_vision.png`.
- [x] Se integró Semana 9 con Flask.
- [x] Se incorporó carga de evidencia visual desde la interfaz web.
- [x] Se documentaron los resultados de la práctica.

### Funciona

El módulo procesa la imagen sin errores bloqueantes y produce tanto métricas numéricas como una evidencia visual comparativa.

### Coincide

Los resultados obtenidos corresponden a los conceptos estudiados durante la Semana 9: características de imagen, detección de contornos, umbral automático, máscara binaria y regiones conectadas.

---

## 12. Resultados principales

```text
Imagen: 360 x 360 píxeles
Píxeles totales: 129600
Intensidad media: 0.1894

Canny
Sigma: 2.0
Píxeles de borde: 2522
Cobertura: 1.95 %

Otsu
Umbral: 0.416
Píxeles objeto: 28281
Píxeles fondo: 101319
Objeto: 21.82 %
Fondo: 78.18 %

Regiones conectadas
Regiones totales: 27
Regiones relevantes: 1
Área mínima: 100 px
Región mayor: 28246 px
Región menor: 1 px
Área promedio: 1047.44 px
```

---

## Conclusión

La Semana 9 permitió incorporar reconocimiento y procesamiento básico de imágenes al Asistente Inteligente de Soporte TI. La evidencia utilizada fue transformada a una representación numérica, posteriormente Canny permitió identificar sus principales contornos y Otsu generó automáticamente una segmentación entre objeto y fondo. Finalmente, el análisis de regiones conectadas permitió cuantificar la estructura de la máscara y separar las regiones pequeñas de la región visual más significativa. Con `sigma=2.0` se detectaron **2522 píxeles de borde**, equivalentes al **1.95 %** de la imagen, mientras que Otsu calculó un umbral de **0.416** y clasificó el **21.82 %** de los píxeles como objeto. Se obtuvieron **27 regiones conectadas**, de las cuales **1 región** superó el criterio de 100 píxeles. La implementación demuestra que una imagen adjunta puede convertirse en evidencia reproducible, cuantificable y útil para complementar el análisis textual de incidentes dentro del proyecto, dejando además como evidencia verificable el archivo `artifacts/semana09_vision.png`.

---

## Evidencias de entrega

```text
src/semana09_vision.py
artifacts/semana09_vision.png
reports/semana09.md
src/web/app.py
src/web/templates/index.html
src/web/static/style.css
```

## Referencia de clase

El desarrollo se basa en la guía tutorial de **Semana 9: Reconocimiento de imágenes**, que plantea como evidencia final código ejecutable, imagen comparativa, análisis en Markdown y avance versionado en el repositorio. La guía trabaja el pipeline de características, Canny, Otsu, máscara y regiones conectadas. citeturn274search20
