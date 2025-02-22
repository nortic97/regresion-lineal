import pandas as pd
import numpy as np


def generate_data():
    # Generar datos simulados
    dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='ME')
    ventas = 3000 + 500 * np.sin(np.linspace(0, 2*np.pi, len(dates))) + np.random.randint(-500, 500, len(dates))
    promociones = np.random.choice([0, 1], size=len(dates), p=[0.7, 0.3])

    return pd.DataFrame({
        'Fecha': dates,
        'Ventas': ventas,
        'Promocion': promociones
    })


def clean_data(df):
    # Limpieza básica
    df = df.drop_duplicates().dropna()
    df['Mes'] = df['Fecha'].dt.month  # Crear feature numérico
    df['Mes_sin'] = np.sin(2 * np.pi * df['Mes'] / 12)
    df['Mes_cos'] = np.cos(2 * np.pi * df['Mes'] / 12)
    return df