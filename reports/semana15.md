# Semana 15 - Organización de la Base de Conocimiento Empresarial- Redes Semánticas- Christian Felipe Alea Agudelo - Andres Esteban Cruz - S10A

## Proyecto: Asistente Inteligente de Soporte TI

### Integrante

- Christian Felipe Alea Agudelo

---

# Objetivo

Implementar una Base de Conocimiento Empresarial utilizando SQLite para organizar, almacenar y consultar conocimiento validado relacionado con el dominio de Soporte TI.

La implementación busca centralizar información confiable mediante:

- Dominios de conocimiento.
- Expertos.
- Artículos validados.
- Consultas SQL.
- Gestión estructurada de información.

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
Regiones

Semana 10
Histogramas
LBP
Vectores de Características

Semana 11
Benchmark de Modelos

Semana 13
Motor de Inferencia

Semana 14
Redes Semánticas
```

La Semana 15 incorpora una Base de Conocimiento Empresarial para organizar información validada y reutilizable dentro del sistema.

---

# Arquitectura Implementada

La solución se desarrolló utilizando:

```text
SQLite
      ↓
Dominios
      ↓
Expertos
      ↓
Artículos
      ↓
Consultas SQL
      ↓
Conocimiento Empresarial
```

La base de datos fue integrada dentro del proyecto utilizando:

```text
artifacts/
└── incidentes_soporte.db
```

---

# Tablas Implementadas

Se diseñaron las siguientes tablas:

## Dominio

```text
id
nombre
```

Representa áreas de conocimiento.

Ejemplos:

```text
Soporte TI
Infraestructura
```

---

## Aplicación

```text
id
nombre
dominio_id
```

Permite asociar sistemas y servicios con dominios específicos.

---

## Experto

```text
id
nombre
```

Representa personas responsables de la validación de conocimiento.

---

## Herramienta

```text
id
nombre
```

Representa plataformas utilizadas dentro de la organización.

---

## Artículo

```text
id
titulo
contenido
estado
dominio_id
experto_id
```

Permite almacenar procedimientos y conocimiento reutilizable.

---

# Dominios Registrados

La implementación registra los siguientes dominios:

```text
Soporte TI

Infraestructura
```

Cantidad:

```text
2 dominios
```

---

# Expertos Registrados

La base almacena los siguientes expertos:

```text
Analista Soporte

Administrador Infraestructura
```

Cantidad:

```text
2 expertos
```

---

# Artículos Validados

Se registraron los siguientes artículos con estado:

```text
VALIDADO
```

### Artículo 1

```text
Restablecimiento VPN
```

Estado:

```text
VALIDADO
```

---

### Artículo 2

```text
Cambio de contraseña
```

Estado:

```text
VALIDADO
```

---

# Consultas SQL

La recuperación de conocimiento se realiza mediante consultas SQL sobre la base de datos.

Consulta implementada:

```sql
SELECT

    titulo,
    estado

FROM articulo

WHERE estado = 'VALIDADO';
```

Resultado:

```text
Restablecimiento VPN

Cambio de contraseña
```

---

# Base de Datos Utilizada

Archivo:

```text
artifacts/
└── incidentes_soporte.db
```

Motor:

```text
SQLite
```

Características:

```text
Ligero
Portátil
Integrado en Python
Sin servidor adicional
```

---

# Integración con el Proyecto

La Base de Conocimiento Empresarial se integró a la arquitectura del Asistente Inteligente de Soporte TI.

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
            ↓
        Semana 14
            ↓
        Semana 15
```

La información validada puede ser utilizada para apoyar futuras consultas y procesos de soporte.

---

# Resultados Obtenidos

## Dominios

```text
Soporte TI

Infraestructura
```

---

## Expertos

```text
Analista Soporte

Administrador Infraestructura
```

---

## Artículos Validados

```text
Restablecimiento VPN

Cambio de contraseña
```

---

## Total de Artículos

```text
2
```

---

# Interpretación

La Base de Conocimiento Empresarial centraliza información validada para apoyar diagnósticos, consultas técnicas y procedimientos recurrentes dentro del entorno de Soporte TI.

Los artículos almacenados representan conocimiento reutilizable y verificable, permitiendo reducir tiempos de respuesta y mejorar la gestión del conocimiento organizacional.

---

# Validación

## Realizado

- [x] Base SQLite creada.
- [x] Tablas implementadas.
- [x] Dominios registrados.
- [x] Expertos registrados.
- [x] Artículos registrados.
- [x] Consulta SQL implementada.
- [x] Recuperación de artículos validados.
- [x] Integración con Flask realizada.
- [x] Integración visual completada.

---

## Funciona

El sistema consulta correctamente la base de conocimiento y recupera la información validada almacenada.

---

## Coincide

Los resultados obtenidos corresponden con los objetivos de la Semana 15:

- Organización del conocimiento.
- Gestión empresarial del conocimiento.
- Recuperación mediante SQL.
- Centralización de artículos validados.
- Integración con sistemas inteligentes.

---

# Conclusión

La Semana 15 permitió incorporar una Base de Conocimiento Empresarial al Asistente Inteligente de Soporte TI mediante SQLite. La implementación organiza el conocimiento utilizando dominios, expertos y artículos validados, permitiendo consultas estructuradas y reutilización de información relevante para la resolución de incidentes. La integración fortalece la capacidad del sistema para almacenar y recuperar conocimiento de manera organizada, complementando los mecanismos de inferencia, redes semánticas y clasificación implementados en semanas anteriores.

---

# Evidencias de Entrega

```text
src/
└── semana15_base_conocimiento.py

artifacts/
└── incidentes_soporte.db

src/web/
├── app.py
├── templates/index.html
└── static/style.css

reports/
└── semana15.md
```