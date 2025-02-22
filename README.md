# Proyecto de Análisis Predictivo en el Sector Retail

Este repositorio contiene el código y los recursos utilizados para realizar un análisis predictivo en el sector retail. El objetivo del proyecto es predecir las ventas mensuales utilizando datos simulados y técnicas de machine learning, específicamente un modelo de **Random Forest Regressor**.

---

## Estructura del Repositorio

El repositorio está organizado de la siguiente manera:


```md
.
├── data/ # Carpeta que contiene los datos generados y procesados
│ ├── raw/ # Datos brutos generados (raw_sales_data.csv)
│ └── processed/ # Datos limpios y listos para el análisis (cleaned_sales_data.csv)
│
├── reports/ # Carpeta que contiene reportes y visualizaciones
│ └── figures/ # Gráficos generados durante el análisis exploratorio
│ ├── series_temporal.png # Gráfico de serie temporal de ventas
│ └── boxplot.png # Gráfico de caja de la distribución de ventas
│
├── src/ # Código fuente del proyecto
│ ├── data_processing.py # Script para generar y limpiar datos
│ ├── exploratory_analysis.py # Script para análisis exploratorio y visualización
│ ├── modeling.py # Script para entrenar y evaluar el modelo predictivo
│ └── main.py # Script principal que ejecuta todo el flujo de trabajo
│
├── requirements.txt # Archivo con las dependencias necesarias para ejecutar el proyecto
└── README.md # Este archivo, con la documentación del proyecto

```

---

## Descripción de los Archivos

### 1. **data_processing.py**
Este script contiene dos funciones principales:
- **`generate_data()`**: Genera datos simulados de ventas mensuales, incluyendo fechas, ventas y promociones.
- **`clean_data()`**: Realiza la limpieza de los datos, eliminando duplicados y valores nulos, y crea nuevas características como `Mes`, `Mes_sin` y `Mes_cos` para capturar la estacionalidad.

### 2. **exploratory_analysis.py**
Este script se encarga del análisis exploratorio de los datos. Incluye:
- **`generate_plots()`**: Genera dos gráficos:
  - **Serie Temporal**: Muestra las ventas mensuales a lo largo del tiempo.
  - **Boxplot**: Muestra la distribución de las ventas.

### 3. **modeling.py**
Este script contiene la lógica para entrenar y evaluar el modelo predictivo:
- **`train_model()`**: Entrena un modelo de **Random Forest Regressor** utilizando las variables `Mes` y `Promocion` para predecir las ventas. Además, calcula el **Error Absoluto Medio (MAE)** para evaluar el rendimiento del modelo.

### 4. **main.py**
Este es el script principal que ejecuta todo el flujo de trabajo:
1. Genera y guarda los datos brutos.
2. Limpia y procesa los datos.
3. Realiza el análisis exploratorio y genera visualizaciones.
4. Entrena y evalúa el modelo predictivo.

## Resultados

- **Error Absoluto Medio (MAE)**: El modelo tiene un MAE de `X.XX COP`, lo que indica la precisión de las predicciones. Los resultados están en **COP (Pesos Colombianos)** para reflejar un contexto local.
  
- **Visualizaciones**:
  - **Serie Temporal**: Muestra las ventas mensuales en COP con tendencias y estacionalidad.
  - **Boxplot**: Muestra la distribución de las ventas en COP, ayudando a identificar valores atípicos.

---

## Cómo Ejecutar el Proyecto

1. **Clonar el Repositorio**:
```bash
    git clone https://github.com/nortic97/regresion-lineal.git
    cd tu-repositorio
```
2. **requirements.txt**
Este archivo contiene todas las dependencias necesarias para ejecutar el proyecto. Puedes instalarlas fácilmente con el siguiente comando:
```bash
    pip install -r requirements.txt