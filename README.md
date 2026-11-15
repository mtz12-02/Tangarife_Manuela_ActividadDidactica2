# Simulación de una red informática mediante Modelos Ocultos de Markov 

## Manuela Tangarife Zapata

## Descripción

Este proyecto consiste en la simulación de una red informática mediante Modelos Ocultos de Markov (HMM), utilizando Python. Se desarrolló de manera individual como parte de una actividad académica.

La simulación representa diferentes estados de funcionamiento de una red y utiliza indicadores observables, como la latencia, la pérdida de paquetes y la disponibilidad, para analizar su comportamiento.

Se implementó el algoritmo de Viterbi para estimar la secuencia de estados ocultos a partir de las observaciones generadas durante la simulación.

## Objetivos
- Aplicar los Modelos Ocultos de Markov a la representación de una red informática.
- Simular diferentes condiciones de funcionamiento de una red.
- Analizar la relación entre los estados ocultos y los indicadores observables.
- Implementar el algoritmo de Viterbi para estimar los estados de la red.
- Comparar los resultados obtenidos en diferentes escenarios mediante métricas de evaluación.

## Metodología

Se definieron tres estados ocultos para representar las condiciones de funcionamiento de la red:
- Normal: funcionamiento adecuado de la red.
- Degradado: presenta dificultades en su rendimiento.
- Fallo: representa una condición crítica de funcionamiento.
Como observaciones se utilizaron tres indicadores: latencia, pérdida de paquetes y disponibilidad.

El modelo se evaluó mediante tres escenarios de simulación, con 30 ejecuciones por escenario y 1.000 instantes de tiempo por ejecución, para un total de 90 ejecuciones.

## Desarrollo del proyecto

### Modelo de simulación

Se construyó un Modelo Oculto de Markov compuesto por los estados, las observaciones, las probabilidades iniciales, la matriz de transición y la matriz de emisión.

### Algoritmo de Viterbi
Se implementó el algoritmo de Viterbi para estimar la secuencia de estados ocultos más probable a partir de las observaciones generadas por la simulación.

### Comparación de escenarios
Se realizaron experimentos modificando los parámetros de inicialización y transición del modelo, con el propósito de observar cómo estos cambios influyen en la estimación de los estados de la red.

### Herramientas utilizadas
- Python
- Bibliotecas de Python utilizadas en la implementación del modelo y el análisis de resultados.

### Resultados
Los experimentos permitieron analizar el comportamiento del modelo en diferentes condiciones de funcionamiento de la red y comparar su capacidad para identificar los estados ocultos.
Se obtuvieron resultados de exactitud y otras métricas de evaluación para los tres escenarios, lo que permitió estudiar la influencia de los parámetros del modelo en la estimación de los estados.

Los resultados detallados se encuentran en las carpetas resultados/ y graficas/.

### Fuentes de consulta

- IEEE Xplore
- ScienceDirect
- SpringerLink
- MDPI
- Google Scholar
- Crossref

Estas fuentes se utilizaron para consultar artículos científicos, investigaciones previas y fundamentos teóricos relacionados con los Modelos Ocultos de Markov, la detección de anomalías y el análisis del rendimiento de redes informáticas.

## Estructura del proyecto

- `main.py:` ejecuta las simulaciones y consolida los resultados.
- `simulacion.py:` define los estados, las matrices de probabilidad y genera las observaciones.
- `viterbi.py:` implementa el algoritmo de Viterbi.
- `graficas.py:` genera las gráficas a partir de los resultados.
- `resultados/:` contiene los archivos CSV generados por las simulaciones.
- `graficas/:` almacena las gráficas generadas.
- `requirements.txt:` contiene las bibliotecas necesarias para ejecutar el proyecto.
- `.gitignore:` excluye archivos y carpetas que no deben incluirse en el repositorio.

## Instalación y ejecución

Para ejecutar el proyecto, se debe tener Python instalado y seguir estos pasos desde la carpeta principal del repositorio.

#### 1 Crear un entorno virtual

python -m venv venv

#### 2 Activar el entorno virtual

En Windows:

venv\Scripts\activate

#### 3 Instalar las dependencias

python -m pip install -r requirements.txt

#### 4 Ejecutar las simulaciones

python main.py

Este archivo realiza las simulaciones y genera los archivos de resultados en la carpeta resultados/.

#### 5 Generar las gráficas

python graficas.py

Este archivo utiliza los resultados generados anteriormente para crear las gráficas y guardarlas en la carpeta graficas/.

#### Importante: primero se debe ejecutar main.py y después graficas.py. Las carpetas resultados/ y graficas/ deben existir en el directorio principal del proyecto.
