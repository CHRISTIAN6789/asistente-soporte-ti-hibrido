# Semana 16 - Arquitectura y Motor de Referencia-Christian Felipe Alea Agudelo - Andres Esteban Cruz - S10A

## Proyecto: Asistente Inteligente de Soporte TI

### Integrantes

- Christian Felipe Alea Agudelo
- Andres Esteban Cruz

---

# Objetivo

Implementar un Motor de Referencia capaz de recuperar conocimiento validado y responder consultas utilizando referencias previamente verificadas dentro del dominio de Soporte TI.

El propósito es garantizar que cada respuesta presentada por el sistema esté respaldada por una fuente conocida y validada.

---

# Introducción

Durante las semanas anteriores se incorporaron diferentes técnicas de Inteligencia Artificial al Asistente Inteligente de Soporte TI:

```text
Semana 7
Representaciones del Reconocimiento

Semana 8
Red Neuronal MLP
SQLite
Ontología

Semana 9
Visión Artificial

Semana 10
Histogramas y Características

Semana 11
Benchmark de Modelos

Semana 13
Motor de Inferencia

Semana 14
Redes Semánticas

Semana 15
Base de Conocimiento Empresarial
```

La Semana 16 incorpora un Motor de Referencia encargado de entregar respuestas fundamentadas a partir de información validada.

---

# Arquitectura Implementada

La arquitectura desarrollada fue:

```text
Consulta del Usuario
          ↓
Normalización
          ↓
Búsqueda de Coincidencias
          ↓
Motor de Referencia
          ↓
Respuesta
          ↓
Fuente
```

El sistema evalúa palabras clave presentes en la consulta y busca la referencia validada más adecuada.

---

# Base de Referencias

Se implementó una base de referencias especializada para Soporte TI.

## REF-ACCESO

```text
Título:
Problemas de Acceso
```

Palabras clave:

```text
contraseña
password
mfa
usuario
bloqueado
acceso
autenticación
```

---

## REF-CORREO

```text
Título:
Incidentes de Correo
```

Palabras clave:

```text
correo
outlook
mail
buzón
sincronización
enviar
```

---

## REF-HARDWARE

```text
Título:
Problemas de Hardware
```

Palabras clave:

```text
pantalla
teclado
equipo
computador
disco
lento
```

---

## REF-INFRA

```text
Título:
Incidentes de Infraestructura
```

Palabras clave:

```text
servidor
infraestructura
servicio
memoria
caído
```

---

## REF-RED

```text
Título:
Problemas de Red
```

Palabras clave:

```text
internet
wifi
vpn
red
conectividad
conexión
```

---

## REF-SEGURIDAD

```text
Título:
Incidentes de Seguridad
```

Palabras clave:

```text
malware
virus
antivirus
seguridad
amenaza
```

---

## REF-SOFTWARE

```text
Título:
Problemas de Software
```

Palabras clave:

```text
software
erp
programa
aplicación
sistema
error
```

---

# Funcionamiento del Motor

El motor realiza las siguientes etapas:

## 1. Normalización

La consulta es convertida a minúsculas y se eliminan tildes.

Ejemplo:

```text
Conexión VPN
```

↓

```text
conexion vpn
```

---

## 2. Tokenización

La consulta se divide en palabras clave.

Ejemplo:

```text
No puedo acceder a la VPN institucional
```

↓

```text
no
puedo
acceder
vpn
institucional
```

---

## 3. Búsqueda

Se comparan las palabras obtenidas contra las claves registradas en las referencias.

---

## 4. Selección

Se selecciona la referencia con mayor cantidad de coincidencias.

---

## 5. Respuesta

El sistema entrega:

```text
Estado

Referencia

Título

Respuesta

Fuente
```

---

# Prueba Real Ejecutada

Consulta utilizada:

```text
Servidor principal caído
```

Resultado obtenido:

```text
Estado:
ENCONTRADA
```

Referencia:

```text
REF-INFRA
```

Título:

```text
Incidentes de Infraestructura
```

Respuesta:

```text
Escalar inmediatamente al administrador de infraestructura.
```

Fuente:

```text
Runbook Infraestructura
```

---

# Ejemplo de Resultado Presentado

```text
Estado:
ENCONTRADA

Referencia:
REF-INFRA

Título:
Incidentes de Infraestructura

Respuesta:
Escalar inmediatamente al administrador de infraestructura.

Fuente:
Runbook Infraestructura
```

---

# Integración con el Proyecto

La Semana 16 se integró completamente al Asistente Inteligente de Soporte TI.

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
            ↓
        Semana 16
```

El Motor de Referencia utiliza la consulta ingresada por el usuario para recuperar conocimiento validado y proporcionar una respuesta fundamentada.

---

# Resultados Obtenidos

## Estado

```text
ENCONTRADA
```

## Referencia

```text
REF-INFRA
```

## Título

```text
Incidentes de Infraestructura
```

## Fuente

```text
Runbook Infraestructura
```

## Respuesta

```text
Escalar inmediatamente al administrador de infraestructura.
```

---

# Validación

## Realizado

- [x] Motor de referencia implementado.
- [x] Normalización de consultas.
- [x] Búsqueda mediante palabras clave.
- [x] Recuperación de referencias validadas.
- [x] Respuesta fundamentada generada.
- [x] Identificación de fuente.
- [x] Integración con Flask.
- [x] Integración con interfaz web.

---

## Funciona

El sistema recupera correctamente referencias validadas a partir de consultas realizadas por el usuario.

---

## Coincide

Los resultados obtenidos corresponden con los objetivos planteados para la Semana 16:

- Arquitectura del conocimiento.
- Motor de referencia.
- Recuperación de información validada.
- Trazabilidad mediante fuentes.
- Respuestas fundamentadas.

---

# Conclusión

La Semana 16 permitió incorporar un Motor de Referencia capaz de asociar consultas realizadas por el usuario con conocimiento previamente validado. El sistema identifica coincidencias mediante palabras clave, selecciona la referencia más adecuada y entrega una respuesta acompañada de su fuente correspondiente. Esta funcionalidad fortalece la trazabilidad y confiabilidad de las respuestas generadas por el Asistente Inteligente de Soporte TI, complementando la base de conocimiento empresarial desarrollada durante la Semana 15.

---

# Evidencias de Entrega

```text
src/
└── semana16_motor_referencia.py

src/web/
├── app.py
├── templates/index.html
└── static/style.css

reports/
└── semana16.md
```