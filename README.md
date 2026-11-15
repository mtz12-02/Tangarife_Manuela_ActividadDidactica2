Simulación de una red informática mediante Modelos Ocultos de Markov
Manuela Tangarife Zapata
Descripción
Este proyecto consiste en la simulación de una red informática mediante Modelos Ocultos de Markov (HMM), utilizando Python. Se desarrolló de manera individual como parte de una actividad académica.

La simulación representa diferentes estados de funcionamiento de una red y utiliza indicadores observables, como la latencia, la pérdida de paquetes y la disponibilidad, para analizar su comportamiento.

Se implementó el algoritmo de Viterbi para estimar la secuencia de estados ocultos a partir de las observaciones generadas durante la simulación.
Objetivos
- Aplicar los Modelos Ocultos de Markov a la representación de una red informática.
- Simular diferentes condiciones de funcionamiento de una red.
- Analizar la relación entre los estados ocultos y los indicadores observables.
- Implementar el algoritmo de Viterbi para estimar los estados de la red.
- Comparar los resultados obtenidos en diferentes escenarios mediante métricas de evaluación.
Metodología
Se definieron tres estados ocultos para representar las condiciones de funcionamiento de la red:
- Normal: funcionamiento adecuado de la red.
- Degradado: presenta dificultades en su rendimiento.
- Fallo: representa una condición crítica de funcionamiento.
Como observaciones se utilizaron tres indicadores: latencia, pérdida de paquetes y disponibilidad.

El modelo se evaluó mediante tres escenarios de simulación, con 30 ejecuciones por escenario y 1.000 instantes de tiempo por ejecución, para un total de 90 ejecuciones.
Desarrollo del proyecto
Modelo de simulación
Se construyó un Modelo Oculto de Markov compuesto por los estados, las observaciones, las probabilidades iniciales, la matriz de transición y la matriz de emisión.
Algoritmo de Viterbi
Se implementó el algoritmo de Viterbi para estimar la secuencia de estados ocultos más probable a partir de las observaciones generadas por la simulación.
Comparación de escenarios
Se realizaron experimentos modificando los parámetros de inicialización y transición del modelo, con el propósito de observar cómo estos cambios influyen en la estimación de los estados de la red.
Herramientas utilizadas
- Python
- Bibliotecas de Python utilizadas en la implementación del modelo y el análisis de resultados.
Resultados
Los experimentos permitieron analizar el comportamiento del modelo en diferentes condiciones de funcionamiento de la red y comparar su capacidad para identificar los estados ocultos.

Se obtuvieron resultados de exactitud y otras métricas de evaluación para los tres escenarios, lo que permitió estudiar la influencia de los parámetros del modelo en la estimación de los estados.
Cómo se puede ejecutar el proyecto
1. Descargar o clonar este repositorio.
2. Abrir el archivo de Python correspondiente a la simulación.
3. Verificar que se encuentren instaladas las bibliotecas necesarias.
4. Ejecutar el programa.
5. Consultar los resultados, tablas y gráficas generadas por la simulación.
