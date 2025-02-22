import pandas as pd
import numpy as np

import pandas as pd
import numpy as np


def generate_data():
    # Generar datos simulados
    dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='ME')

    # Generar valores de ventas con un componente estacional y ruido aleatorio
    ventas = 6500000 + 1500000 * np.sin(np.linspace(0, 2 * np.pi, len(dates))) + np.random.randint(-500000, 500000, len(dates))

    # Asegurar que las ventas estén dentro del rango deseado (5,000,000 a 8,000,000 COP)
    ventas = np.clip(ventas, 5000000, 8000000)

    # Generar datos de promociones (0: no hay promoción, 1: hay promoción)
    promociones = np.random.choice([0, 1], size=len(dates), p=[0.7, 0.3])

    return pd.DataFrame({
        'Fecha': dates,
        'Ventas': ventas,  # Ventas en COP
        'Promocion': promociones
    })


def clean_data(df):
    # Limpieza básica
    df = df.drop_duplicates().dropna()
    df['Mes'] = df['Fecha'].dt.month  # Crear feature numérico
    df['Mes_sin'] = np.sin(2 * np.pi * df['Mes'] / 12)
    df['Mes_cos'] = np.cos(2 * np.pi * df['Mes'] / 12)
    return df