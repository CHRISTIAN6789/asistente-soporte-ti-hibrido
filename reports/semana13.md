# Semana 13 - Ingeniería del Conocimiento- Christian Felipe Alea Agudelo - Andres Esteban Cruz - S10A

## Proyecto: Asistente Inteligente de Soporte TI

### Integrante

- Christian Felipe Alea Agudelo

---

# Objetivo

Implementar un sistema de inferencia basado en reglas de producción para apoyar la toma de decisiones dentro del Asistente Inteligente de Soporte TI.

La solución utiliza:

- Base de hechos
- Base de reglas
- Motor de inferencia
- Encadenamiento hacia adelante
- Trazabilidad de reglas
- Conclusiones explicables

---

# Introducción

Durante las semanas anteriores se desarrollaron diferentes componentes del sistema:

```text
Semana 7
Representaciones del reconocimiento

Semana 8
Red neuronal MLP
SQLite
Ontología

Semana 9
Procesamiento de imágenes
Canny
Otsu
Regiones conectadas

Semana 10
Histogramas
LBP
Vectores de características

Semana 11
Benchmark de modelos
```

La Semana 13 incorpora técnicas de Ingeniería del Conocimiento mediante un motor de inferencia capaz de generar conclusiones automáticas a partir de hechos observados y reglas definidas explícitamente.

---

# Arquitectura Implementada

La arquitectura desarrollada se compone de:

```text
Base de Hechos
        ↓
Base de Reglas
        ↓
Motor de Inferencia
        ↓
Trazabilidad
        ↓
Conclusión
```

---

# Motor de Inferencia

Se implementó un mecanismo de inferencia mediante encadenamiento hacia adelante.

Proceso:

```text
Hechos iniciales
       ↓
Evaluación de reglas
       ↓
Nuevos hechos inferidos
       ↓
Conclusión final
```

La inferencia continúa hasta que no existan nuevas reglas que puedan activarse.

---

# Base de Hechos

Los hechos son obtenidos automáticamente a partir del análisis realizado por el sistema.

Para la prueba ejecutada se obtuvieron:

```text
alto_impacto

evidencia_disponible

incidente_critico

escalamiento_requerido

atencion_prioritaria

ticket_urgente
```

Estos elementos representan conocimiento disponible para el motor de inferencia.

---

# Base de Reglas

Se construyeron reglas de producción relacionadas con escenarios de soporte TI.

## Regla R1

```text
SI

alto_impacto

ENTONCES

escalamiento_requerido
```

---

## Regla R2

```text
SI

escalamiento_requerido

Y

evidencia_disponible

ENTONCES

atencion_prioritaria
```

---

## Regla R3

```text
SI

atencion_prioritaria

ENTONCES

ticket_urgente
```

---

# Encadenamiento de Reglas

Durante la ejecución se activaron:

```text
R1
↓
escalamiento_requerido

R2
↓
atencion_prioritaria

R3
↓
ticket_urgente
```

Trazabilidad:

```text
R1

R2

R3
```

---

# Resultados Obtenidos

## Hechos Inferidos

```text
alto_impacto

evidencia_disponible

incidente_critico

escalamiento_requerido

atencion_prioritaria

ticket_urgente
```

---

## Reglas Activadas

```text
R1

R2

R3
```

Número de reglas activadas:

```text
3
```

---

## Conclusión Final

Resultado del proceso de inferencia:

```text
Ticket urgente
```

---

# Interpretación

El motor de inferencia determinó que el incidente presenta condiciones suficientes para ser considerado un ticket urgente.

La secuencia de razonamiento utilizada fue:

```text
Alto impacto
      ↓
Escalamiento requerido
      ↓
Atención prioritaria
      ↓
Ticket urgente
```

Este comportamiento demuestra que el conocimiento almacenado en la base de reglas puede utilizarse para generar conclusiones automáticas y explicables.

---

# Integración con el Proyecto

La Semana 13 fue integrada completamente al Asistente Inteligente de Soporte TI.

Flujo actualizado:

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
```

La conclusión generada por el motor de inferencia complementa las decisiones obtenidas mediante clasificación, visión artificial y benchmark.

---

# Validación

## Realizado

- [x] Base de hechos construida.
- [x] Base de reglas implementada.
- [x] Motor de inferencia desarrollado.
- [x] Encadenamiento hacia adelante ejecutado.
- [x] Trazabilidad registrada.
- [x] Conclusión automática generada.
- [x] Integración con Flask realizada.
- [x] Integración con la interfaz web completada.

---

## Funciona

El sistema ejecuta correctamente el motor de inferencia y genera conclusiones basadas en los hechos disponibles.

---

## Coincide

Los resultados obtenidos corresponden con los conceptos estudiados en Ingeniería del Conocimiento:

- Base de hechos.
- Base de reglas.
- Inferencia.
- Encadenamiento hacia adelante.
- Explicabilidad.
- Sistemas basados en conocimiento.

---

# Evidencias Generadas

```text
src/

└── semana13_motor_inferencia.py


src/web/

├── app.py

├── templates/index.html

└── static/style.css


reports/

└── semana13.md
```

---

# Conclusión

La Semana 13 permitió incorporar técnicas de Ingeniería del Conocimiento al Asistente Inteligente de Soporte TI mediante un motor de inferencia basado en reglas de producción. A partir de hechos obtenidos durante el análisis del incidente, el sistema fue capaz de activar reglas, generar trazas explicables y concluir automáticamente que el incidente correspondía a un Ticket urgente. Esta funcionalidad fortalece la capacidad de razonamiento del sistema y complementa las técnicas de clasificación, visión artificial y evaluación de modelos implementadas en las semanas anteriores.