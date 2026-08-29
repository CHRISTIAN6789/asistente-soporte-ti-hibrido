# Semana 03 - Taxonomía de Inteligencia Artificial - Christian Felipe Alea Agudelo - Andres Esteban Cruz - S10A

Proyecto: Asistente Inteligente de Soporte TI Híbrido
A. Descripción del problema

El proyecto desarrollado consiste en un Asistente Inteligente de Soporte TI Híbrido cuyo propósito es apoyar la identificación, clasificación y gestión de incidentes tecnológicos reportados por los usuarios.

Durante esta semana se incorporaron conceptos relacionados con representación de problemas, búsqueda heurística y toma de decisiones. Para ello se modeló el proceso de atención de incidentes como un espacio de estados y se implementó una representación inspirada en el algoritmo A* para generar rutas de resolución. Además, se incorporó una simulación conceptual de Minimax para comprender procesos de priorización y selección de alternativas.

El sistema desarrollado analiza la consulta del usuario, identifica categorías de Inteligencia Artificial, clasifica el ticket de soporte, determina su criticidad, impacto, prioridad y escalamiento, y finalmente genera una ruta sugerida de resolución.

B. Representación del problema

El problema fue representado como un espacio de estados. El estado inicial corresponde al momento en que un usuario registra un incidente dentro del sistema.

Los estados definidos para la resolución fueron:

Incidente.
Diagnosticar.
Revisar Credenciales.
Restablecer Contraseña.
Solucionado.

Cada uno de estos estados representa una etapa dentro del proceso de soporte técnico.

Las acciones permiten avanzar entre estados. Entre ellas se encuentran el diagnóstico del problema, la validación de credenciales, la recuperación de acceso y la verificación final de la solución implementada.

Las transiciones representan el cambio entre estados después de ejecutar una acción determinada. El flujo representado en el sistema puede entenderse como un proceso continuo que inicia con el reporte del incidente y finaliza cuando el problema ha sido corregido satisfactoriamente.

La meta del sistema consiste en alcanzar el estado Solucionado, indicando que el incidente fue atendido correctamente.

El costo de camino representa el esfuerzo necesario para avanzar entre estados. A medida que se realizan acciones de diagnóstico y corrección, el costo acumulado aumenta hasta alcanzar la solución final.

La heurística utilizada corresponde a una estimación de los pasos restantes para llegar al estado objetivo. De esta manera, el sistema puede priorizar aquellas alternativas que parecen más cercanas a la resolución del incidente.

La decisión de exploración se basa en la función de evaluación utilizada por A*:

f(n) = g(n) + h(n)

donde:

g(n) representa el costo acumulado.
h(n) representa la estimación restante.
f(n) representa el valor utilizado para seleccionar la mejor alternativa disponible.
C. Implementación

La implementación se desarrolló sobre el mismo repositorio acumulativo utilizado en las semanas anteriores.

El módulo de taxonomía fue actualizado para reconocer categorías relacionadas tanto con Inteligencia Artificial como con incidentes específicos de Soporte TI. Gracias a este módulo, el sistema puede identificar consultas relacionadas con correo corporativo, VPN, conectividad, servidores, aplicaciones, impresoras, autenticación multifactor, antivirus y otros escenarios comunes en un entorno empresarial.

También se implementó un módulo especializado para la clasificación de tickets. Este componente determina automáticamente el tipo de incidente, el nivel de criticidad, el impacto esperado, la prioridad de atención y el área responsable del escalamiento.

Como parte de la práctica principal de la semana, se desarrolló un módulo de búsqueda basado en la representación de estados y transiciones. Este módulo permite generar una ruta sugerida para la resolución de incidentes.

Finalmente, todos los componentes fueron integrados dentro de la aplicación principal, permitiendo que el usuario obtenga un análisis completo de su incidente desde una única interfaz.

D. Resultados
Caso de prueba 1: Servidor principal caído

Se ingresó una consulta relacionada con la caída del servidor principal de la organización.

El sistema identificó correctamente la incidencia como un problema de infraestructura crítica, asignando criticidad alta, impacto alto y prioridad P1. Asimismo, determinó que el escalamiento apropiado corresponde al administrador de servidores.

El resultado obtenido es consistente con las políticas habituales de soporte TI, dado que la indisponibilidad de un servidor puede afectar múltiples servicios y usuarios.

Caso de prueba 2: Correo corporativo no funciona

Se evaluó una consulta asociada al funcionamiento del correo corporativo.

El sistema clasificó correctamente el incidente dentro del dominio de soporte TI y determinó una criticidad media con prioridad P2. El escalamiento sugerido fue la mesa de ayuda.

La decisión es razonable debido a que el correo es un servicio importante para la operación diaria, aunque normalmente no compromete toda la infraestructura tecnológica.

Caso de prueba 3: Impresora fuera de servicio

Se analizó una falla relacionada con una impresora corporativa.

La clasificación obtenida correspondió a un incidente de periféricos, con criticidad baja, impacto bajo y prioridad P4.

El resultado es coherente porque la incidencia afecta un único dispositivo y no representa un riesgo significativo para la operación general de la organización.

Aplicación de A*

El algoritmo A* fue utilizado como referencia para representar una secuencia de resolución dentro del proceso de soporte técnico.

La ejecución del sistema muestra una ruta estructurada que inicia en el estado de incidente y avanza progresivamente hacia la solución. Esta representación permite comprender de manera clara las etapas necesarias para resolver el problema reportado.

La principal ventaja de esta representación es que facilita el análisis del proceso de resolución y permite explicar cómo el sistema avanza desde una situación inicial hasta una meta final utilizando costos y heurísticas.

Aplicación de Minimax

El proyecto desarrollado no corresponde a un problema adversarial, por lo que Minimax no fue implementado como algoritmo principal del sistema. Sin embargo, se realizó un análisis conceptual para demostrar la comprensión de esta técnica.

Se planteó un escenario donde el sistema debe decidir qué incidente atender primero considerando el impacto organizacional asociado a cada alternativa.

Para este análisis se consideraron tres casos: un servidor principal caído, una falla de VPN corporativa y una impresora fuera de servicio.

La caída del servidor fue considerada como la opción más importante debido a que afecta procesos críticos de la organización. La falla de VPN fue considerada de importancia intermedia, mientras que la falla de impresora fue considerada de menor impacto.

Bajo esta representación, la decisión seleccionada sería priorizar la atención del servidor principal caído, ya que genera el mayor beneficio operativo al ser resuelto.

Este ejercicio permitió comprender cómo Minimax selecciona la alternativa de mayor utilidad cuando existen múltiples opciones disponibles.

Poda Alfa-Beta

La poda alfa-beta fue estudiada como una técnica de optimización de Minimax.

Su función consiste en evitar la exploración de alternativas que no modificarán la decisión final. Esto permite reducir la cantidad de evaluaciones necesarias y mejorar el rendimiento del algoritmo.

En el contexto del ejemplo analizado, una vez identificada una alternativa claramente superior, algunas opciones menos relevantes podrían descartarse sin afectar la decisión final.

La principal ventaja de esta técnica es la reducción del costo computacional manteniendo exactamente el mismo resultado que produciría Minimax sin optimización.

Justificación de la no aplicación directa de Minimax

El sistema desarrollado tiene como objetivo resolver incidentes de soporte TI y no competir contra otro agente racional.

Por esta razón, el problema fue modelado como un problema de búsqueda y resolución mediante estados, acciones, costos y heurísticas, siendo A* una técnica más adecuada para representar este dominio.

Aunque Minimax no forma parte del flujo principal del sistema, su estudio permitió comprender las diferencias existentes entre los problemas de búsqueda y los problemas adversariales.

E. Análisis
Ventajas

La solución desarrollada integra múltiples conceptos de Inteligencia Artificial dentro de una única aplicación.

Además de clasificar incidentes, el sistema permite identificar categorías de IA, determinar prioridades, establecer mecanismos de escalamiento y representar procesos de resolución.

La implementación facilita la comprensión de conceptos como espacios de estados, costos de camino y heurísticas, aplicándolos directamente al dominio de soporte tecnológico.

Limitaciones

La clasificación actual se encuentra basada principalmente en reglas definidas manualmente.

Las rutas de resolución utilizadas son modelos simplificados y no representan todos los escenarios posibles que pueden presentarse en un entorno empresarial real.

Asimismo, la heurística utilizada corresponde a una aproximación conceptual y no a una estimación construida a partir de datos históricos.

Supuestos

Para el funcionamiento del sistema se asumió que los usuarios describen adecuadamente el problema reportado y que los costos asignados a las transiciones son constantes.

También se asumió que cada incidente puede asociarse a una categoría predominante para efectos de clasificación.

Posibles mejoras

Como trabajos futuros se propone incorporar algoritmos de aprendizaje automático para mejorar la clasificación de incidentes, implementar una versión completa y dinámica de A*, integrar bases de conocimiento empresariales y añadir métricas relacionadas con tiempos de atención y acuerdos de nivel de servicio.

Conclusiones

La actividad permitió aplicar los conceptos fundamentales estudiados durante la Semana 04 relacionados con representación de problemas, búsqueda heurística y toma de decisiones.

Se logró integrar estos conceptos dentro del Asistente Inteligente de Soporte TI Híbrido mediante la incorporación de módulos de clasificación, priorización, escalamiento y resolución de incidentes.

Los resultados obtenidos demuestran que los conceptos de Inteligencia Artificial pueden utilizarse para apoyar procesos reales de soporte tecnológico, aportando organización, automatización y capacidad de análisis dentro del proyecto acumulativo del semestre.