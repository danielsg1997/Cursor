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