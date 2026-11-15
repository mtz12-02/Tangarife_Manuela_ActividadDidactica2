import numpy as np
from simulacion import B_L, B_P, B_D

def calcular_emision(observacion, estado):

    # Obtener las tres observaciones
    obs_latencia, obs_perdida, obs_disponibilidad = observacion

    # Calcular la probabilidad conjunta de las observaciones
    probabilidad = (
        B_L[estado, obs_latencia] *
        B_P[estado, obs_perdida] *
        B_D[estado, obs_disponibilidad]
    )

    return probabilidad

def viterbi(observaciones, pi, A):

    cantidad = len(observaciones)
    numero_estados = len(pi)

    # Crear las tablas de probabilidades y caminos
    delta = np.zeros((cantidad, numero_estados))
    caminos = np.zeros((cantidad, numero_estados), dtype=int)

    # Inicializar las probabilidades del primer instante
    for estado in range(numero_estados):
        delta[0, estado] = (
            np.log(pi[estado]) +
            np.log(calcular_emision(observaciones[0], estado))
        )

    # Calcular las probabilidades de los siguientes instantes
    for instante in range(1, cantidad):

        for estado in range(numero_estados):

            probabilidades = (
                delta[instante - 1] + np.log(A[:, estado])
            )

            caminos[instante, estado] = np.argmax(probabilidades)

            delta[instante, estado] = (
                np.max(probabilidades) +
                np.log(calcular_emision(observaciones[instante], estado))
            )

    # Encontrar el estado final más probable
    secuencia = np.zeros(cantidad, dtype=int)
    secuencia[-1] = np.argmax(delta[-1])

    # Reconstruir la secuencia de estados
    for instante in range(cantidad - 2, -1, -1):
        secuencia[instante] = caminos[
            instante + 1, secuencia[instante + 1]
        ]

    return secuencia
