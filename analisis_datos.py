"""
Ejercicio de Análisis de Datos Estadísticos

Este módulo realiza un análisis estadístico básico de datos numéricos almacenados
en un archivo CSV. Calcula medidas estadísticas descriptivas (media, mediana,
desviación estándar) para dos columnas de datos y genera una visualización
mediante un gráfico de dispersión (scatter plot).

Funcionalidades:
    - Lectura de datos desde un archivo CSV
    - Cálculo de estadísticas descriptivas (media, mediana, desviación estándar)
    - Visualización de datos mediante gráfico de dispersión

Requisitos:
    - pandas: Para manipulación de datos
    - matplotlib: Para visualización de gráficos
    - Archivo datos_numericos.csv con columnas 'columna_1' y 'columna_2'
"""

import pandas as pd
import matplotlib.pyplot as plt
#quiero leer el archivo datos_numericos.csv
datos = pd.read_csv("datos_numericos.csv")
#mostrar la media de la columna 1
print(datos["columna_1"].mean())
#mostrar la media de la columna 2
print(datos["columna_2"].mean())
#mostrar la mediana de la columna 1
print(datos["columna_1"].median())
#mostrar la mediana de la columna 2
print(datos["columna_2"].median())
#mostrar la desviacion estandar de la columna 1
print(datos["columna_1"].std())
#mostrar la desviacion estandar de la columna 2
print(datos["columna_2"].std())
#crear un scatter plot de columna_1 vs columna_2
plt.scatter(datos["columna_1"], datos["columna_2"])
plt.xlabel("columna_1")
plt.ylabel("columna_2")
plt.title("Scatter Plot: columna_1 vs columna_2")
plt.grid(True, alpha=0.3)
plt.show()