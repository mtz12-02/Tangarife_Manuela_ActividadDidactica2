import numpy as np

# Estados ocultos de la red
estados = ["Normal", "Degradado", "Fallo"]

# Categorías de las observaciones
latencia = ["Baja", "Media", "Alta"]
perdida = ["Baja", "Media", "Alta"]
disponibilidad = ["Alta", "Media", "Baja"]

# Matriz de emisión de latencia
B_L = np.array([
    [0.80, 0.17, 0.03],
    [0.15, 0.70, 0.15],
    [0.05, 0.20, 0.75]
])

# Matriz de emisión de pérdida de paquetes
B_P = np.array([
    [0.85, 0.12, 0.03],
    [0.20, 0.65, 0.15],
    [0.05, 0.20, 0.75]
])

# Matriz de emisión de disponibilidad
B_D = np.array([
    [0.95, 0.04, 0.01],
    [0.25, 0.60, 0.15],
    [0.05, 0.20, 0.75]
])

# Parámetros de los escenarios experimentales
escenarios = {
    "Escenario 1": {
        "pi": np.array([0.80, 0.15, 0.05]),
        "A": np.array([
            [0.85, 0.13, 0.02],
            [0.20, 0.65, 0.15],
            [0.10, 0.25, 0.65]
        ])
    },

    "Escenario 2": {
        "pi": np.array([0.60, 0.25, 0.15]),
        "A": np.array([
            [0.70, 0.22, 0.08],
            [0.12, 0.58, 0.30],
            [0.05, 0.25, 0.70]
        ])
    },

    "Escenario 3": {
        "pi": np.array([0.90, 0.08, 0.02]),
        "A": np.array([
            [0.93, 0.06, 0.01],
            [0.35, 0.60, 0.05],
            [0.25, 0.35, 0.40]
        ])
    }
}

def generar_simulacion(pi, A, cantidad, semilla=None):

    # Crear el generador de números aleatorios
    rng = np.random.default_rng(semilla)

    estados_reales = []
    observaciones = []

    # Generar el estado inicial
    estado = rng.choice(len(estados), p=pi)

    for instante in range(cantidad):

        # Guardar el estado real
        estados_reales.append(estado)

        # Generar las tres observaciones
        obs_latencia = rng.choice(3, p=B_L[estado])
        obs_perdida = rng.choice(3, p=B_P[estado])
        obs_disponibilidad = rng.choice(3, p=B_D[estado])

        observaciones.append([
            obs_latencia,
            obs_perdida,
            obs_disponibilidad
        ])

        # Generar el siguiente estado
        if instante < cantidad - 1:
            estado = rng.choice(len(estados), p=A[estado])

    return np.array(estados_reales), np.array(observaciones)
