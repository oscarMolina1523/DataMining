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