# Ejercicio de afianzamiento
# carga de archivo csv
# visualización con grafico de dispersión
# clasificacion de clientes por nivel de compras

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('clientes_preprocesados.csv')

#visualizacion: graficos de dispersion
plt.scatter(df["Ingreso Normalizado"], df["Historial de Compras"], color="green")
plt.xlabel("Ingreso Normalizado")
plt.ylabel("Historial de Compras")
plt.title("Relacion entre ingreso y compras")
plt.show()

#clasificacion por nivel de compras
def clasificar(compras):
    if compras > 10:
        return "Alto"
    elif compras >= 5:
        return "Medio"
    else:
        return "Bajo"

df["Nivel Compras"]= df["Historial de Compras"].apply(clasificar)

#Guardar nuevo archivo
df.to_csv("clientes_clasificados.csv", index=False)