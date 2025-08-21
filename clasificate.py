# Strengthening exercise
# CSV file upload
# Scatter chart visualization
# Customer classification by purchasing level

import pandas as pd
import matplotlib.pyplot as plt

# Upload the CSV file
df = pd.read_csv('clientes_preprocesados.csv')

#visualization: scatter plots
plt.scatter(df["Ingreso Normalizado"], df["Historial de Compras"], color="green")
plt.xlabel("Ingreso Normalizado")
plt.ylabel("Historial de Compras")
plt.title("Relacion entre ingreso y compras")
plt.show()

#classification by purchasing level
def clasificar(compras):
    if compras > 10:
        return "Alto"
    elif compras >= 5:
        return "Medio"
    else:
        return "Bajo"

df["Nivel Compras"]= df["Historial de Compras"].apply(clasificar)

#Save new file
df.to_csv("clientes_clasificados.csv", index=False)