import numpy as np
import pandas as pd

from simulacion import generar_simulacion, escenarios, estados
from viterbi import viterbi

# Configurar los parámetros del experimento
cantidad_ejecuciones = 30
cantidad_instantes = 1000
semilla_base = 42

# Guardar los resultados de cada ejecución
resultados = []

# Recorrer los tres escenarios
for indice, (nombre, parametros) in enumerate(escenarios.items()):

    # Preparar la matriz de confusión
    matriz_confusion = np.zeros((3, 3), dtype=int)

    exactitudes = []

    print("\nProcesando:", nombre)

    # Realizar las 30 ejecuciones
    for ejecucion in range(cantidad_ejecuciones):

        # Asignar una semilla diferente a cada ejecución
        semilla = semilla_base + indice * cantidad_ejecuciones + ejecucion

        # Generar los estados y las observaciones
        estados_reales, observaciones = generar_simulacion(
            parametros["pi"],
            parametros["A"],
            cantidad_instantes,
            semilla
        )

        # Estimar los estados mediante Viterbi
        estados_estimados = viterbi(
            observaciones,
            parametros["pi"],
            parametros["A"]
        )

        # Calcular la exactitud
        coincidencias = np.sum(estados_reales == estados_estimados)
        exactitud = coincidencias / cantidad_instantes

        exactitudes.append(exactitud)

        # Guardar los resultados de la ejecución
        resultados.append({
            "Escenario": nombre,
            "Ejecucion": ejecucion + 1,
            "Semilla": semilla,
            "Exactitud": exactitud
        })

        # Actualizar la matriz de confusión
        for real, estimado in zip(estados_reales, estados_estimados):
            matriz_confusion[real, estimado] += 1

    # Calcular las estadísticas del escenario
    promedio = np.mean(exactitudes)
    desviacion = np.std(exactitudes, ddof=1)
    minimo = np.min(exactitudes)
    maximo = np.max(exactitudes)

    # Calcular el intervalo de confianza del 95 %
    margen_error = 2.045 * desviacion / np.sqrt(cantidad_ejecuciones)

    limite_inferior = promedio - margen_error
    limite_superior = promedio + margen_error

    print("Exactitud promedio:", round(promedio * 100, 2), "%")
    print("Desviación estándar:", round(desviacion * 100, 2), "%")
    print("Exactitud mínima:", round(minimo * 100, 2), "%")
    print("Exactitud máxima:", round(maximo * 100, 2), "%")
    print(
        "Intervalo de confianza 95 %:",
        round(limite_inferior * 100, 2),
        "% -",
        round(limite_superior * 100, 2),
        "%"
    )

    # Guardar la matriz de confusión
    nombres_estados = [
    "Normal",
    "Degradado",
    "Fallo"
    ]

    matriz_df = pd.DataFrame(
        matriz_confusion,
        index=nombres_estados,
        columns=nombres_estados
    )

    matriz_df.index.name = "Estado_real"
    matriz_df.columns.name = "Estado_estimado"
    matriz_df.index.name = "Estado"

    matriz_df.to_csv(
        f"resultados/matriz_confusion_{indice + 1}.csv"
    )

# Organizar los resultados de las ejecuciones
df_resultados = pd.DataFrame(resultados)

# Calcular el resumen estadístico de cada escenario
resumen = df_resultados.groupby("Escenario")["Exactitud"].agg(
    Promedio="mean",
    Desviacion="std",
    Minimo="min",
    Maximo="max"
).reset_index()

# Agregar los intervalos de confianza
resumen["IC95_Inferior"] = (
    resumen["Promedio"] -
    2.045 * resumen["Desviacion"] / np.sqrt(cantidad_ejecuciones)
)

resumen["IC95_Superior"] = (
    resumen["Promedio"] +
    2.045 * resumen["Desviacion"] / np.sqrt(cantidad_ejecuciones)
)

# Guardar los resultados en archivos CSV
df_resultados.to_csv(
    "resultados/resultados_por_ejecucion.csv",
    index=False
)

resumen.to_csv(
    "resultados/resumen_escenarios.csv",
    index=False
)

# Mostrar el resumen final
print("\n===================================")
print("RESUMEN GENERAL DEL EXPERIMENTO")
print("===================================")

print(resumen.to_string(index=False))

print("\nExperimento finalizado correctamente.")
print("Total de ejecuciones:", len(df_resultados))
print("Total de instantes:", len(df_resultados) * cantidad_instantes)
