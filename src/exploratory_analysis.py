import matplotlib.pyplot as plt

def generate_plots(df):
    # Serie temporal
    plt.figure(figsize=(12, 6))
    plt.plot(df['Fecha'], df['Ventas'] / 1_000_000, marker='o', color='teal')  # Dividir por 1,000,000 para mostrar en millones
    plt.title('Ventas Mensuales (Millones de COP)')
    plt.ylabel('Ventas (Millones de COP)')
    plt.savefig('reports/figures/series_temporal.png')
    plt.close()

    # Boxplot
    plt.figure(figsize=(8, 4))
    plt.boxplot(df['Ventas'] / 1_000_000, vert=False)  # Dividir por 1,000,000 para mostrar en millones
    plt.title('Distribución de Ventas (Millones de COP)')
    plt.xlabel('Ventas (Millones de COP)')
    plt.savefig('reports/figures/boxplot.png')
    plt.close()