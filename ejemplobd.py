
import pandas as pd

def leer_base_datos(ruta_archivo):
    """Lee un archivo CSV y devuelve un DataFrame."""
    return pd.read_csv(ruta_archivo)

# Ejemplo de uso

import matplotlib.pyplot as plt

def calcular_kpis(df):
    """Calcula KPIs a partir de un DataFrame."""
    total_ventas = df['ventas'].sum()
    promedio_ventas = df['ventas'].mean()
    total_clientes = df['clientes'].nunique()
    
    return {
        'Total Ventas': total_ventas,
        'Promedio Ventas': promedio_ventas,
        'Total Clientes': total_clientes
    }

def graficar_kpis(kpis):
    """Grafica los KPIs proporcionados."""
    nombres = list(kpis.keys())
    valores = list(kpis.values())
    
    plt.bar(nombres, valores, color='blue')
    plt.xlabel('KPIs')
    plt.ylabel('Valores')
    plt.title('KPIs de Ventas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Ejemplo de uso


df = leer_base_datos('mibd.csv')
print(df.head())  # Muestra las primeras filas del DataFrame
kpis = calcular_kpis(df)
print(kpis)  # Muestra los KPIs calculados
