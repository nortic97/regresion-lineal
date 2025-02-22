import matplotlib.pyplot as plt

def generate_plots(df):
    # Serie temporal
    plt.figure(figsize=(12, 6))
    plt.plot(df['Fecha'], df['Ventas'], marker='o', color='teal')
    plt.title('Ventas Mensuales (COP)')
    plt.ylabel('Ventas (COP)')
    plt.savefig('reports/figures/series_temporal.png')
    plt.close()

    # Boxplot
    plt.figure(figsize=(8, 4))
    plt.boxplot(df['Ventas'], vert=False)
    plt.title('Distribución de Ventas (COP)')
    plt.xlabel('Ventas (COP)')
    plt.savefig('reports/figures/boxplot.png')
    plt.close()