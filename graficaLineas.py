import matplotlib.pyplot as plt
import pandas as pd

#Con lineas

df= pd.read_csv("covid19.csv")
x = df["Date"].value_counts()
y = df["Confirmed"].value_counts()
plt.title("Casos confirmados del COVID19")
plt.xlabel("Fecha")
plt.ylabel("Casos Confirmados")
plt.plot(x,y)
plt.show()
