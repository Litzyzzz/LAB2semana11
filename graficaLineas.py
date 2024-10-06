import matplotlib.pyplot as plt
import pandas as pd

#Con lineas
df= pd.read_csv("covid19.csv")
x = df["Date"].head(12)
y = df["Confirmed"].head(12)
plt.title("Casos confirmados del COVID19")
plt.xlabel("Fecha")
plt.ylabel("Casos Confirmados")
plt.plot(x,y, color="RED",marker='o')#el tipo marker es para que se visualice mejor la linea
plt.show()

"""
Esta grafica nos muestra el aumento de los casos confirmados del
Covid 19 en el mes de Enero del año 2020, llegando hasta inicio de Febrero
siendo este el punto más alto desde que se confirmó el primero
"""
