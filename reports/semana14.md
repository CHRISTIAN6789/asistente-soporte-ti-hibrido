# Semana 14 - Redes Semánticas- Christian Felipe Alea Agudelo - Andres Esteban Cruz - S10A

## Proyecto: Asistente Inteligente de Soporte TI

### Integrante

- Christian Felipe Alea Agudelo

---

# Objetivo

Implementar una red semántica para representar conocimiento mediante conceptos, relaciones, jerarquías, herencia e inferencia dentro del dominio de Soporte TI.

La finalidad de esta práctica consiste en modelar relaciones entre elementos tecnológicos y demostrar cómo una red semántica permite inferir conocimiento que no se encuentra almacenado explícitamente.

---

# Introducción

Durante las semanas anteriores se desarrollaron diversos componentes del Asistente Inteligente de Soporte TI:

```text
Semana 7
Representaciones del Reconocimiento

Semana 8
Red Neuronal MLP
SQLite
Ontología

Semana 9
Procesamiento de Imágenes
Canny
Otsu
Regiones Conectadas

Semana 10
Histogramas
Texturas LBP
Vectores de Características

Semana 11
Benchmark y Evaluación de Modelos

Semana 13
Motor de Inferencia
Ingeniería del Conocimiento
```

La Semana 14 incorpora una Red Semántica que permite representar conocimiento mediante relaciones entre conceptos y realizar inferencias utilizando estructuras jerárquicas.

---

# Conceptos Modelados

Se definieron los siguientes conceptos para el dominio de Soporte TI:

```text
Servidor

VPN

Router

Red

Infraestructura

Activo_TI
```

Estos conceptos representan elementos relevantes dentro de un entorno tecnológico y servirán como nodos dentro de la red semántica.

---

# Relaciones Registradas

Se construyeron las siguientes relaciones semánticas:

```text
Servidor → es_un → Infraestructura

VPN → es_un → Red

Router → es_un → Red

Red → es_un → Infraestructura

Infraestructura → es_un → Activo_TI

Impresora → es_un → Activo_TI

Activo_TI → necesita → Monitoreo

Infraestructura → necesita → Mantenimiento

Red → necesita → Conectividad

Servidor → necesita → Respaldo
```

Número total de relaciones registradas:

```text
10
```

---

# Jerarquía de Conceptos

La red construida puede representarse conceptualmente de la siguiente forma:

```text
Activo_TI
      ↑
Infraestructura
      ↑
      Red
     ↙   ↘
 Router  VPN

Servidor
    ↑
Infraestructura
```

Esta jerarquía permite heredar propiedades y realizar inferencias semánticas.

---

# Inferencias Realizadas

Las consultas ejecutadas fueron:

## Consulta 1

```text
¿Servidor es un Activo_TI?
```

Resultado:

```text
True
```

### Explicación

```text
Servidor
→ Infraestructura

Infraestructura
→ Activo_TI
```

Por lo tanto:

```text
Servidor
→ Activo_TI
```

---

## Consulta 2

```text
¿VPN es Infraestructura?
```

Resultado:

```text
True
```

### Explicación

```text
VPN
→ Red

Red
→ Infraestructura
```

Por lo tanto:

```text
VPN
→ Infraestructura
```

---

## Consulta 3

```text
¿Router es Activo_TI?
```

Resultado:

```text
True
```

### Explicación

```text
Router
→ Red

Red
→ Infraestructura

Infraestructura
→ Activo_TI
```

Por lo tanto:

```text
Router
→ Activo_TI
```

---

# Herencia de Propiedades

Una de las características fundamentales de las redes semánticas es la herencia.

## Necesidades del Servidor

Resultado:

```text
mantenimiento

monitoreo

respaldo
```

### Interpretación

Servidor hereda:

```text
Monitoreo
```

porque:

```text
Activo_TI → necesita → Monitoreo
```

Hereda:

```text
Mantenimiento
```

porque:

```text
Infraestructura → necesita → Mantenimiento
```

Y además posee:

```text
Respaldo
```

como propiedad propia.

---

## Necesidades de VPN

Resultado:

```text
conectividad

mantenimiento

monitoreo
```

### Interpretación

VPN hereda:

```text
Conectividad
```

desde:

```text
Red
```

Hereda:

```text
Mantenimiento
```

desde:

```text
Infraestructura
```

Y hereda:

```text
Monitoreo
```

desde:

```text
Activo_TI
```

---

# Implementación

Se desarrolló el archivo:

```text
src/
└── semana14_red_semantica.py
```

El sistema contiene:

```text
Clase RedSemantica

Relaciones

Consulta jerárquica

Herencia de propiedades

Inferencia semántica
```

---

# Integración con el Proyecto

La Semana 14 fue integrada dentro del Asistente Inteligente de Soporte TI.

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
           ↓
       Semana 13
           ↓
       Semana 14
```

La red semántica complementa la ontología desarrollada en semanas anteriores y añade inferencia basada en relaciones jerárquicas.

---

# Resultados Obtenidos

## Conceptos

```text
6
```

## Relaciones

```text
10
```

## Inferencias

```text
Servidor es Activo_TI → True

VPN es Infraestructura → True

Router es Activo_TI → True
```

## Herencia

```text
Servidor:
- monitoreo
- mantenimiento
- respaldo

VPN:
- conectividad
- mantenimiento
- monitoreo
```

---

# Validación

## Realizado

- [x] Red semántica implementada.
- [x] Relaciones registradas.
- [x] Jerarquías definidas.
- [x] Herencia de propiedades implementada.
- [x] Inferencias ejecutadas.
- [x] Integración con Flask realizada.
- [x] Integración visual dentro del sistema completada.

---

## Funciona

El sistema responde correctamente a consultas semánticas y realiza inferencias utilizando relaciones jerárquicas.

---

## Coincide

Los resultados corresponden con los conceptos estudiados en la guía de Redes Semánticas:

- Conceptos.
- Relaciones.
- Triples semánticos.
- Herencia.
- Inferencia.
- Consultas.

---

# Conclusión

La Semana 14 permitió incorporar una Red Semántica al Asistente Inteligente de Soporte TI para representar conocimiento de forma estructurada. A través de conceptos, relaciones jerárquicas y herencia de propiedades fue posible inferir conocimiento que no se encontraba explícitamente almacenado, demostrando que un Servidor puede ser reconocido como Activo_TI y que elementos como VPN heredan propiedades definidas en niveles superiores de la jerarquía. Esta implementación fortalece la capacidad de representación del conocimiento del sistema y complementa las técnicas de inferencia desarrolladas previamente.

---

# Evidencias de Entrega

```text
src/
└── semana14_red_semantica.py

src/web/
├── app.py
├── templates/index.html
└── static/style.css

reports/
└── semana14.md
```