#if you don't have the required libraries, install them using:
#pip install pandas numpy matplotlib scikit-learn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

clientes={
    "ID":[1,2,3,4,5],
    "Edad":[22, 35, 45, 23, 31],
    "Genero":["M", "F", "male", "female", "Masculino"],
    "Ingreso Mensual":[3000, 4500, np.nan, 2800, 5000],
    "Historial de Compras":[5, 10, 3, 2, 8],
    "Suscripcion de Newsletter":["Si", "No", "Si", "No", "Si"]
}

df=pd.DataFrame(clientes)
#print(df) # Uncomment to see the DataFrame

#clean the data
df=df.drop_duplicates(subset="ID")#delete duplicates
df["Ingreso Mensual"]=df["Ingreso Mensual"].fillna(df["Ingreso Mensual"].mean())#fill missing values with the mean
df["Genero"]=df["Genero"].replace({"M":"Masculino","male":"Masculino", "F":"Femenino","female":"Femenino"})#unify categories

#information visualization
plt.hist(df["Edad"], bins=5, color='skyblue', edgecolor='black')
plt.title("Distribución de Edad")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

#data transformation
scaler=MinMaxScaler()
df["Ingreso Normalizado"]= scaler.fit_transform(df[["Ingreso Mensual"]])
df_encoded=pd.get_dummies(df["Genero", "Suscripcion de Newsletter"], drop_first=True)
df["Grupo Edad"]=pd.cut(df["Edad"], bins=[0, 25, 35, 45, 50], labels=["18-25", "26-35", "36-50"])

#feature selection
df_final = pd.concat([df.drop(columns=['ID', 'Genero', 'Suscripcion a Newsletter', 'Ingreso Mensual']), df_encoded], axis=1)
df_final.to_csv("clientes_preprocesados.csv", index=False)