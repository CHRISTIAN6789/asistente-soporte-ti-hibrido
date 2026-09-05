# Semana 05 - Sistemas Híbridos de Inteligencia Artificial - Christian Felipe Alea Agudelo - Andres Esteban Cruz - S10A

Proyecto: Asistente Inteligente de Soporte TI Híbrido

1. Descripción del Proyecto

El proyecto desarrollado corresponde a un Asistente Inteligente de Soporte TI Híbrido orientado al análisis y gestión de incidentes tecnológicos reportados por usuarios de una organización.

Durante la Semana 05 se incorporaron conceptos relacionados con sistemas expertos, ingeniería del conocimiento, recuperación de información, reconocimiento de patrones y tratamiento del lenguaje natural. Estas funcionalidades fueron integradas al proyecto acumulativo desarrollado durante el semestre, permitiendo generar respuestas explicables a partir de reglas, conocimiento almacenado y mecanismos de clasificación.

La solución permite analizar una consulta realizada por un usuario, identificar el tipo de incidente, recuperar información relacionada desde una base de conocimiento, clasificar el problema y generar recomendaciones para su atención.

2. Sistema Híbrido Implementado

El sistema desarrollado integra diferentes componentes de Inteligencia Artificial dentro de un único flujo de procesamiento.

El usuario registra un incidente mediante una consulta escrita en lenguaje natural. A partir de dicha consulta, el sistema realiza una clasificación taxonómica, identifica el tipo de ticket, ejecuta reglas expertas, recupera información relevante mediante técnicas de similitud textual y genera una clasificación final del incidente.

Además, se integraron los componentes desarrollados en semanas anteriores, incluyendo búsqueda basada en A* y una representación conceptual de priorización mediante Minimax.

De esta forma, el sistema combina múltiples enfoques de Inteligencia Artificial dentro de una solución unificada orientada al dominio de soporte tecnológico.

3. Ingeniería del Conocimiento

La ingeniería del conocimiento se implementó mediante una base de conocimiento especializada en soporte técnico.

La base contiene información relacionada con situaciones reales de soporte TI, incluyendo problemas de correo corporativo, VPN, impresoras, servidores, autenticación, antivirus, malware, aplicaciones corporativas, conectividad y hardware.

La información almacenada constituye el conocimiento experto utilizado posteriormente por los mecanismos de recuperación de información.

Cada entrada describe procedimientos o recomendaciones que pueden ser utilizados para asistir en el diagnóstico y la solución de incidentes.

4. Sistema Experto

El sistema experto fue implementado mediante reglas de producción orientadas al dominio de soporte tecnológico.

Estas reglas permiten establecer recomendaciones específicas cuando determinadas condiciones son detectadas dentro de la consulta.

Por ejemplo, cuando una consulta contiene términos asociados al correo corporativo, el sistema recomienda verificar credenciales y disponibilidad del servicio. Cuando se detectan problemas relacionados con VPN, el sistema recomienda validar configuraciones y conectividad. De forma similar se definieron reglas para servidores, impresoras, malware, autenticación multifactor, accesos, redes inalámbricas y aplicaciones corporativas.

El uso de reglas permite que las respuestas generadas sean explicables y coherentes con el contexto del problema reportado.

5. Recuperación de Información

La recuperación de información fue implementada mediante técnicas TF-IDF y similitud del coseno.

El objetivo consiste en identificar cuál elemento de la base de conocimiento se encuentra más relacionado con la consulta realizada por el usuario.

Una vez procesada la consulta, el sistema calcula la similitud entre el texto ingresado y los documentos almacenados en la base de conocimiento. Posteriormente selecciona la información que presenta el mayor nivel de coincidencia.

Este proceso permite justificar la recomendación entregada al usuario y constituye uno de los mecanismos de explicación del sistema.

6. Reconocimiento de Patrones y Clasificación

Para implementar el reconocimiento de patrones se utilizó un conjunto de ejemplos etiquetados almacenados en un archivo CSV.

Las categorías utilizadas corresponden al dominio del proyecto e incluyen acceso, correo, red, hardware, infraestructura, seguridad y software.

Cada consulta ingresada por el usuario es comparada contra los ejemplos almacenados, permitiendo identificar la categoría más cercana mediante similitud textual.

Este mecanismo constituye la etapa de clasificación inteligente del sistema.

7. Tratamiento del Lenguaje Natural

El sistema incorpora técnicas básicas de procesamiento del lenguaje natural para interpretar las consultas realizadas por los usuarios.

Las consultas son transformadas y comparadas mediante técnicas de análisis textual que permiten extraer términos relevantes y encontrar similitudes con el conocimiento almacenado.

Gracias a este proceso, el sistema puede responder consultas expresadas en lenguaje natural tales como problemas de correo corporativo, dificultades de conexión VPN o incidentes relacionados con infraestructura tecnológica.

8. Casos de Prueba
Caso de Prueba 1: Correo Corporativo

Se realizó una consulta relacionada con el funcionamiento del correo corporativo.

El sistema identificó correctamente que se trataba de un incidente relacionado con servicios de correo electrónico. La regla activada recomendó verificar credenciales y disponibilidad del servicio. La información recuperada provenía de la base de conocimiento especializada en correo corporativo y la clasificación final correspondió a la categoría Correo.

La similitud obtenida fue de 0.6074, indicando una relación significativa entre la consulta y la información recuperada.

Caso de Prueba 2: Conexión VPN

Se realizó una consulta relacionada con problemas de conexión VPN.

El sistema activó la regla asociada a conectividad VPN, recuperó información relacionada con la configuración del cliente y la red, y clasificó correctamente el incidente dentro de la categoría Red.

La similitud obtenida fue de 0.5590 y la clasificación presentó una coincidencia completa con los ejemplos almacenados.

Caso de Prueba 3: Servidor con Alto Consumo de Recursos

Se ingresó una consulta relacionada con un servidor que presentaba alto consumo de recursos.

La regla activada recomendó validar los servicios críticos del servidor. La información recuperada describía procedimientos relacionados con análisis de procesos, capacidad del sistema y servicios activos.

La clasificación obtenida correspondió a Infraestructura y la similitud alcanzó un valor de 0.5194.

El resultado fue consistente con la naturaleza del incidente reportado.

9. Integración con Semanas Anteriores

El proyecto mantiene la integración de todos los componentes desarrollados anteriormente.

La taxonomía de Inteligencia Artificial implementada en la Semana 3 continúa siendo utilizada para clasificar las consultas dentro de categorías especializadas.

Los conceptos de representación de problemas, búsqueda A* y priorización conceptual mediante Minimax desarrollados en la Semana 4 permanecen integrados como parte del análisis realizado por el sistema.

La Semana 5 amplió el proyecto mediante la incorporación de conocimiento experto, clasificación inteligente y recuperación de información.

10. Ventajas de la Solución

La solución desarrollada ofrece múltiples ventajas.

Permite automatizar la clasificación de incidentes, recuperar conocimiento relevante para cada consulta, generar recomendaciones explicables y facilitar procesos de soporte tecnológico.

La integración de varias técnicas de Inteligencia Artificial dentro de una única aplicación proporciona una experiencia más completa para el usuario y facilita la toma de decisiones dentro del proceso de atención de incidentes.

Adicionalmente, el proyecto incorpora una interfaz web que mejora significativamente la interacción con el sistema.

11. Limitaciones

Entre las limitaciones identificadas se encuentra la dependencia de reglas definidas manualmente, así como el uso de una base de conocimiento estática.

Asimismo, las rutas utilizadas por el componente A* corresponden a una implementación simplificada orientada a fines académicos.

Aunque la clasificación funciona correctamente para los escenarios definidos, el sistema podría beneficiarse de técnicas más avanzadas de aprendizaje automático en futuras etapas.

12. Conclusiones

Durante la Semana 05 se logró integrar conceptos fundamentales de Inteligencia Artificial dentro del proyecto de Asistente Inteligente de Soporte TI Híbrido.

La incorporación de sistema experto, ingeniería del conocimiento, recuperación de información, reconocimiento de patrones y procesamiento del lenguaje natural permitió enriquecer significativamente las capacidades del proyecto.

Los resultados obtenidos demuestran que es posible combinar diferentes técnicas de Inteligencia Artificial para construir soluciones explicables y orientadas a problemas reales de soporte tecnológico.

La evolución del proyecto a través de las distintas semanas permitió construir una solución integral capaz de clasificar incidentes, recuperar conocimiento especializado, priorizar situaciones y proponer mecanismos de resolución dentro de un entorno de soporte TI.