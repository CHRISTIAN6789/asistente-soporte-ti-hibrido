# Semana 07 - Representaciones del Reconocimiento- Christian Felipe Alea Agudelo - Andres Esteban Cruz - S10A

## Proyecto: Asistente Inteligente de Soporte TI Híbrido

---

## 1. Introducción

Durante la Semana 07 se trabajaron diferentes formas de representar información dentro de un sistema de Inteligencia Artificial. Se estudiaron principalmente los métodos numéricos, los métodos simbólicos y el reconocimiento mediante autómatas.

La representación de información es importante debido a que un sistema inteligente no trabaja directamente con la realidad, sino con características, símbolos, estados o valores que permiten describir una situación determinada.

Para esta actividad, los conceptos fueron integrados al proyecto acumulativo **Asistente Inteligente de Soporte TI Híbrido**, evitando implementar literalmente el ejemplo desarrollado durante la clase.

El fenómeno seleccionado para la práctica fue el reconocimiento y procesamiento de un incidente de soporte TI.

---

## 2. Objetivo

El objetivo de la implementación fue representar un mismo incidente tecnológico mediante tres enfoques diferentes:

1. Representación numérica.
2. Representación simbólica.
3. Reconocimiento mediante autómata.

Cada representación permite analizar el mismo incidente desde una perspectiva diferente.

La implementación fue conectada directamente con la clasificación de tickets desarrollada previamente, utilizando características como la criticidad, el impacto y el tipo de incidente.

---

## 3. Adaptación al Proyecto

El Asistente Inteligente de Soporte TI Híbrido ya disponía de diferentes componentes para analizar incidentes tecnológicos.

Antes de implementar la Semana 07, el sistema podía identificar:

- Tipo de incidente.
- Criticidad.
- Impacto.
- Prioridad.
- Escalamiento.
- Categorías de Inteligencia Artificial.
- Reglas expertas.
- Información recuperada mediante TF-IDF.
- Clasificación inteligente.
- Ruta de resolución mediante A*.
- Priorización conceptual median*e Minimax.

Durante esta semana, a*gunos de estos resultados fueron u*ilizados como entrada para produci* tres nuevas formas de representac*ón.

De esta manera, la Semana 07 *o fue desarrollada como un ejercic*o independiente, sino como una amp*iación del sistema híbrido acumula*ivo.

---

## 4. Representación Nu*érica

La primera representación i*plementada corresponde al enfoque *umérico.

Los métodos numéricos pe*miten representar una situación me*iante conjuntos ordenados de valor*s. Posteriormente, estos valores p*eden utilizarse para realizar oper*ciones matemáticas y comparar dife*entes observaciones.

Dentro del p*oyecto, las características de un *ncidente de soporte TI son transfo*madas en valores numéricos.

Se de*inió una escala sencilla:

- Nivel*bajo: 1.
- Nivel medio: 2.
- Nivel*alto: 3.

De esta manera, caracter*sticas como la criticidad y el imp*cto pueden ser convertidas en valo*es cuantificables.

El sistema gen*ra un vector del incidente y poste*iormente lo compara con un patrón *e referencia asociado a un inciden*e crítico.

Un ejemplo de vector g*nerado por el sistema es:

**Vecto***el incidente:** [3, 1, 2]

El pa*rón crítico de referencia utilizad* es:

**Patrón crítico:** [3, 3, 3]

Para comparar ambas representaci*nes se calcula una distancia numér*ca.

En una de las pruebas realiza*as se obtuvo una distancia de:

*****36**

Una distancia menor indica*que el incidente presenta mayor si*ilitud con el patrón crítico de re*erencia.

Esta representación perm*te realizar comparaciones cuantita*ivas entre incidentes y facilita l* identificación de patrones.

---
*## 5. Representación Simbólica

La*segunda representación implementad* corresponde al enfoque simbólico.*
Los métodos simbólicos representa* la información mediante conceptos* hechos y relaciones explícitas.

*entro del proyecto, la información*obtenida mediante la clasificación*del ticket es convertida en hechos*simbólicos.

Por ejemplo, un incid*nte puede generar los siguientes h*chos:

- `criticidad_alta`
- `impa*to_alto`
- `infraestructura`

Post*riormente se aplican reglas sobre *stos hechos.

Cuando se identifica* simultáneamente una criticidad al*a y un impacto alto, el sistema pu*de concluir:

**incidente_critico**

Este enfoque permite representar*el conocimiento mediante una lógic* comprensible.

Una de sus princip*les ventajas es la explicabilidad,*ya que es posible identificar los *echos que provocaron determinada c*nclusión.

---

## 6. Reconocimiento Mediante Autómata

La tercera representación implementada corresponde al reconocimiento mediante un autómata.

El autómata representa el ciclo de atención de un ticket mediante estados y transiciones.

El estado inicial definido en el proyecto es:

**NUEVO**

Este estado representa el momento en que el incidente es recibido por el sistema.

Posteriormente, el ticket puede avanzar al estado:

**DIAGNOSTICO**

Este estado representa el proceso de análisis inicial del incidente.

Cuando el incidente necesita intervención especializada, puede pasar al estado:

**ESCALADO**

Finalmente, después de aplicar las acciones necesarias, el ticket alcanza:

**RESUELTO**

El estado RESUELTO corresponde al estado de aceptación del autómata.

Un recorrido válido para un incidente crítico es:

**NUEVO → DIAGNOSTICO → ESCALADO → RESUELTO**

Cuando el ticket alcanza correctamente el estado RESUELTO, el sistema determina que la secuencia fue aceptada.

---

## 7. Interpretación del Autómata

El propósito del autómata es verificar si el proceso seguido por un ticket corresponde a una secuencia válida de estados.

El autómata no intenta encontrar la mejor solución para el incidente.

Su función consiste en reconocer si las transiciones realizadas cumplen con las reglas definidas.

Esto permite diferenciarlo del algoritmo A* utilizado previamente.

A* intenta encontrar una ruta de solución según los estados disponibles, mientras que el autómata verifica si una secuencia concreta corresponde a un recorrido válido.

La representación mediante autómatas puede utilizarse en soporte TI para modelar procesos como:

- Recepción de incidentes.
- Diagnóstico.
- Escalamiento.
- Resolución.
- Cierre.
- Reapertura.
- Validación.

---

## 8. Integración de las Tres Representaciones

Las tres representaciones utilizadas describen el mismo fenómeno desde perspectivas diferentes.

### Representación numérica

Permite responder:

**¿Qué tan parecido es el incidente actual a un patrón conocido?**

### Representación simbólica

Permite responder:

**¿Qué hechos describen el incidente y qué conclusión puede obtenerse mediante reglas?**

### Representación mediante autómata

Permite responder:

**¿La secuencia de atención del ticket corresponde a un flujo válido?**

La utilización de las tres representaciones fortalece el carácter híbrido del proyecto.

---

## 9. Comparación de las Representaciones

### 9.1 Representación Numérica

**Ventajas**

- Permite realizar cálculos matemáticos.
- Facilita la comparación entre incidentes.
- Permite medir distancias entre diferentes patrones.
- Puede utilizarse posteriormente con técnicas estadísticas o de aprendizaje automático.

**Limitaciones**

- Los números por sí solos no explican completamente el significado del incidente.
- Es necesario conocer qué representa cada posición del vector.
- Depende de una correcta transformación de características cualitativas a valores numéricos.

**Pérdida de información**

Al convertir elementos como criticidad o impacto en valores discretos pueden perderse detalles específicos del contexto original.

---

### 9.2 Representación Simbólica

**Ventajas**

- Facilita la interpretación humana.
- Permite utilizar reglas explícitas.
- Proporciona conclusiones explicables.
- Mantiene el significado conceptual de diferentes características.

**Limitaciones**

- Depende de reglas previamente definidas.
- Requiere actualizar manualmente el conocimiento cuando aparecen nuevas situaciones.
- Puede resultar difícil de mantener cuando aumenta significativamente la cantidad de reglas.

**Pérdida de información**

Una situación compleja puede simplificarse excesivamente al transformarse únicamente en un conjunto reducido de símbolos.

---

### 9.3 Representación mediante Autómata

**Ventajas**

- Permite visualizar claramente estados y transiciones.
- Facilita la validación de secuencias.
- Permite representar procesos estructurados.
- Resulta apropiada para ciclos de atención de tickets.

**Limitaciones**

- Todos los estados y transiciones válidas deben ser definidos previamente.
- Un flujo empresarial complejo puede requerir una gran cantidad de estados.
- No determina por sí mismo la mejor decisión.

**Pérdida de información**

El autómata conserva principalmente información relacionada con el estado y la secuencia del proceso, pero no representa todos los detalles técnicos asociados al incidente.

---

## 10. Pruebas Realizadas

### 10.1 Prueba de Infraestructura

Se realizó una consulta relacionada con un servidor que presenta problemas de recursos.

El sistema clasificó el incidente dentro del dominio de infraestructura.

La representación numérica generó un vector de características y lo comparó contra el patrón crítico.

La representación simbólica reconoció diferentes hechos relacionados con criticidad, impacto e infraestructura.

El autómata generó un recorrido compuesto por los estados Nuevo, Diagnóstico, Escalado y Resuelto.

El estado final correspondió a RESUELTO, por lo que la secuencia fue aceptada.

---

### 10.2 Prueba de Red

Se realizó una consulta relacionada con una conexión VPN que no podía establecerse.

El sistema identificó el incidente dentro del dominio de redes.

La representación numérica permitió transformar las características del ticket en valores cuantificables.

La representación simbólica generó hechos relacionados con la clasificación obtenida.

Finalmente, el autómata permitió representar el flujo de atención correspondiente hasta alcanzar el estado de resolución.

---

### 10.3 Prueba de Correo Corporativo

Se realizó una consulta relacionada con un problema de correo corporativo.

El sistema identificó correctamente el tipo de incidente y generó las tres representaciones.

La representación numérica permitió comparar el ticket contra un patrón crítico.

La representación simbólica permitió expresar las características mediante hechos.

Finalmente, el autómata permitió comprobar que el flujo de atención podía alcanzar correctamente el estado RESUELTO.

---

## 11. Integración con el Sistema Híbrido

La Semana 07 fue integrada con los componentes desarrollados anteriormente.

Actualmente, el flujo general del proyecto puede describirse de la siguiente manera:

**Consulta del usuario → Taxonomía IA → Clasificación del ticket → Sistema experto → Recuperación de información → Clasificación inteligente → A* → Minimax → Representaciones del reconocimiento**

Dentro del componente correspondiente a la Semana 07 se generan:

**Representación numérica → Representación simbólica → Reconocimiento mediante autómata**

Esto permite mantener el carácter acumulativo del proyecto.

---

## 12. Integración con la Interfaz Web

Las funcionalidades desarrolladas durante la Semana 07 también fueron integradas dentro de la interfaz web del Asistente Inteligente de Soporte TI Híbrido.

La página contiene una sección denominada:

**Semana 7 - Representaciones del Reconocimiento**

Dentro de esta sección se presentan tres tarjetas.

La primera tarjeta corresponde a la representación numérica y presenta el vector del incidente, el patrón crítico utilizado como referencia y la distancia calculada.

La segunda tarjeta corresponde a la representación simbólica y muestra los hechos reconocidos y la conclusión generada mediante reglas.

La tercera tarjeta muestra visualmente el autómata del ticket mediante estados conectados por transiciones.

Por ejemplo, un incidente crítico puede mostrar el siguiente recorrido:

**NUEVO → DIAGNOSTICO → ESCALADO → RESUELTO**

La interfaz también indica si el recorrido fue aceptado.

Esta integración facilita la comprensión del funcionamiento interno del sistema y constituye una evidencia visual de la implementación realizada.

---

## 13. Archivos Creados o Modificados

Para el desarrollo de la Semana 07 se creó el archivo:

**src/semana07_representaciones.py**

Este archivo contiene la lógica correspondiente a las representaciones numérica, simbólica y mediante autómata.

También se modificó:

**src/main.py**

Este archivo integra las nuevas representaciones dentro de la aplicación ejecutada mediante consola.

Se actualizó:

**src/web/app.py**

Este archivo conecta los resultados de Semana 07 con Flask y los envía hacia la interfaz.

También se modificó:

**src/web/templates/index.html**

Este archivo contiene la visualización web de las tres representaciones.

Finalmente, se actualizó:

**src/web/static/style.css**

Este archivo contiene los estilos utilizados para diferenciar visualmente las representaciones numérica, simbólica y mediante autómata.

---

## 14. Limitaciones

La representación numérica desarrollada utiliza una cantidad reducida de características. Esto significa que actualmente no representa toda la complejidad de un incidente real.

La representación simbólica depende de los hechos y reglas definidos previamente. Nuevos escenarios pueden requerir ampliar la base de reglas.

El autómata implementado representa únicamente un ciclo simplificado del proceso de atención.

En una herramienta real de gestión de servicios TI podrían existir estados adicionales como:

- Asignado.
- Pendiente.
- Esperando usuario.
- En validación.
- Cerrado.
- Reabierto.
- Cancelado.

Estas limitaciones deben considerarse en futuras versiones del sistema.

---

## 15. Posibles Mejoras

Como evolución del proyecto se propone ampliar la representación numérica mediante nuevas características, entre ellas:

- Número de usuarios afectados.
- Tiempo estimado de indisponibilidad.
- Cantidad de errores registrados.
- Impacto sobre servicios empresariales.
- Nivel de servicio comprometido.

La representación simbólica puede ampliarse mediante nuevos hechos y reglas que permitan realizar diagnósticos más detallados.

El autómata también puede ampliarse para representar procesos más cercanos a los utilizados en herramientas reales de Service Desk.

Otra posible mejora consiste en almacenar el historial de estados de cada ticket para posteriormente analizar patrones en los procesos de resolución.

---

## 16. Conclusiones

La Semana 07 permitió aplicar diferentes mecanismos de representación del conocimiento al Asistente Inteligente de Soporte TI Híbrido.

La representación numérica permitió transformar características de los incidentes en valores cuantificables y compararlos mediante una medida de distancia.

La representación simbólica permitió convertir las características del ticket en hechos comprensibles y generar conclusiones mediante reglas explícitas.

El autómata permitió representar el ciclo de atención de tickets mediante estados y transiciones, verificando si una determinada secuencia alcanza correctamente el estado de aceptación.

La combinación de las tres representaciones demuestra que un mismo problema puede ser modelado desde diferentes perspectivas dependiendo del tipo de información que el sistema necesite procesar.

Finalmente, la integración de estas representaciones dentro de la interfaz web permitió presentar los resultados de forma visual y explicable, fortaleciendo el enfoque híbrido y acumulativo del proyecto.