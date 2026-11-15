# Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Leer el resumen de los resultados
resultados = pd.read_csv("resultados/resumen_escenarios.csv")

# Convertir los valores a porcentajes
resultados["Promedio"] = resultados["Promedio"] * 100
resultados["IC95_Inferior"] = resultados["IC95_Inferior"] * 100
resultados["IC95_Superior"] = resultados["IC95_Superior"] * 100

# Calcular el tamaño de las barras de error
error_inferior = resultados["Promedio"] - resultados["IC95_Inferior"]
error_superior = resultados["IC95_Superior"] - resultados["Promedio"]

# Mostrar los datos que utilizaremos en la gráfica
print(resultados[["Escenario", "Promedio", "IC95_Inferior", "IC95_Superior"]])

# Crear la gráfica de exactitud promedio
plt.figure(figsize=(9, 5))

plt.bar(
    resultados["Escenario"],
    resultados["Promedio"],
    yerr=[error_inferior, error_superior],
    capsize=6
)

# Agregar títulos y etiquetas
plt.title("Exactitud promedio por escenario")
plt.xlabel("Escenarios")
plt.ylabel("Exactitud (%)")

# Ajustar los límites del eje vertical
plt.ylim(85, 100)

# Mostrar los valores sobre las barras
for i, valor in enumerate(resultados["Promedio"]):
    plt.text(i, valor + 0.5, f"{valor:.2f}%", ha="center")

# Ajustar la presentación
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

# Guardar la gráfica
plt.savefig("graficas/exactitud_escenarios.png", dpi=300)

# Mostrar la gráfica
plt.show()

# Leer los resultados de cada ejecución
ejecuciones = pd.read_csv("resultados/resultados_por_ejecucion.csv")

# Convertir la exactitud a porcentaje
ejecuciones["Exactitud"] = ejecuciones["Exactitud"] * 100

# Organizar las exactitudes por escenario
datos_boxplot = [
    ejecuciones[ejecuciones["Escenario"] == "Escenario 1"]["Exactitud"],
    ejecuciones[ejecuciones["Escenario"] == "Escenario 2"]["Exactitud"],
    ejecuciones[ejecuciones["Escenario"] == "Escenario 3"]["Exactitud"]
]

# Comprobar los resultados
# Mostrar las primeras ejecuciones
print(ejecuciones.head())

# Contar las ejecuciones de cada escenario
print(ejecuciones.groupby("Escenario").size())

# Crear el diagrama de cajas
plt.figure(figsize=(9, 5))

plt.boxplot(
    datos_boxplot,
    tick_labels=["Escenario 1", "Escenario 2", "Escenario 3"]
)

# Ajustar los límites del eje vertical
plt.ylim(85, 100)

# Agregar títulos y etiquetas
plt.title("Distribución de exactitud por escenario")
plt.xlabel("Escenarios")
plt.ylabel("Exactitud (%)")

# Ajustar la presentación
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

# Guardar la gráfica
plt.savefig("graficas/distribucion_exactitud.png", dpi=300)

# Mostrar la gráfica
plt.show()

# Definir los archivos de las matrices
archivos = [
    "resultados/matriz_confusion_1.csv",
    "resultados/matriz_confusion_2.csv",
    "resultados/matriz_confusion_3.csv"
]

titulos = [
    "Escenario 1",
    "Escenario 2",
    "Escenario 3"
]

# Crear una figura con tres matrices
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, archivo, titulo in zip(axes, archivos, titulos):

    # Leer la matriz de confusión
    matriz = pd.read_csv(archivo, index_col=0)

    # Convertir las cantidades a porcentajes por fila
    matriz_porcentaje = matriz.div(matriz.sum(axis=1), axis=0) * 100

    # Crear el mapa de calor
    imagen = ax.imshow(matriz_porcentaje, cmap="Blues", vmin=0, vmax=100)

    # Agregar los nombres de los estados
    ax.set_xticks(range(3))
    ax.set_yticks(range(3))
    ax.set_xticklabels(matriz.columns, rotation=45, ha="right")
    ax.set_yticklabels(matriz.index)

    # Agregar los porcentajes dentro de cada celda
    for fila in range(3):
        for columna in range(3):
            valor = matriz_porcentaje.iloc[fila, columna]
            ax.text(columna, fila, f"{valor:.1f}%", ha="center", va="center")

    # Agregar títulos y etiquetas
    ax.set_title(titulo)
    ax.set_xlabel("Estado estimado")
    ax.set_ylabel("Estado real")

# Agregar una escala de colores
fig.colorbar(imagen, ax=axes, label="Porcentaje (%)", shrink=0.8)

# Ajustar la presentación
plt.suptitle("Matrices de confusión por escenario")
plt.tight_layout()

# Guardar la gráfica
plt.savefig("graficas/matrices_confusion.png", dpi=300)

# Mostrar la gráfica
plt.show()

# Definir los escenarios y los estados
escenarios_nombres = ["Escenario 1", "Escenario 2", "Escenario 3"]
estados_nombres = ["Normal", "Degradado", "Fallo"]

# Guardar los resultados de clasificación por estado
exactitud_estados = []

for i in range(1, 4):

    # Leer la matriz de confusión
    matriz = pd.read_csv(
        f"resultados/matriz_confusion_{i}.csv",
        index_col=0
    )

    # Calcular el porcentaje de aciertos por estado
    porcentajes = np.diag(matriz) / matriz.sum(axis=1) * 100

    exactitud_estados.append(porcentajes)

# Organizar los resultados
exactitud_estados = pd.DataFrame(
    exactitud_estados,
    index=escenarios_nombres,
    columns=estados_nombres
)

# Mostrar los resultados
print(exactitud_estados)

# Crear la gráfica de comparación por estado
ax = exactitud_estados.plot(
    kind="bar",
    figsize=(10, 5)
)

# Agregar títulos y etiquetas
plt.title("Exactitud de clasificación por estado y escenario")
plt.xlabel("Escenarios")
plt.ylabel("Exactitud (%)")

# Ajustar el eje vertical
plt.ylim(0, 100)

# Mostrar los valores sobre las barras
for contenedor in ax.containers:
    ax.bar_label(contenedor, fmt="%.1f%%", padding=2)

# Ajustar la presentación
plt.xticks(rotation=0)
plt.legend(title="Estados")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

# Guardar la gráfica
plt.savefig("graficas/exactitud_por_estado.png", dpi=300)

# Mostrar la gráfica
plt.show()