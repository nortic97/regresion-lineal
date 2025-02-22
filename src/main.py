import os
import pandas as pd
from src.data_processing import generate_data, clean_data
from src.exploratory_analysis import generate_plots
from src.modeling import train_model


def main():
    # Crear carpetas si no existen
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("reports/figures", exist_ok=True)

    # Paso 1: Generar y guardar datos simulados
    raw_data = generate_data()
    raw_data.to_csv("data/raw/raw_sales_data.csv", index=False)

    # Paso 2: Limpiar datos
    cleaned_data = clean_data(raw_data)
    cleaned_data.to_csv("data/processed/cleaned_sales_data.csv", index=False)

    # Paso 3: Análisis exploratorio
    generate_plots(cleaned_data)

    # Paso 4: Modelado predictivo
    model, mae = train_model(cleaned_data)
    print(f"\nError Absoluto Medio del Modelo: {mae:.2f} COP")


if __name__ == "__main__":
    main()