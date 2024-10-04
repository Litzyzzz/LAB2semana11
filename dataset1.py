import matplotlib.pyplot as plt
import pandas as pd

#Con barras
df = pd.read_csv("sabrina.csv", delimiter=";")
x=df['track_name'].head(7)
y=df['spotify_streams'].head(7)
plt.title("Cantidad de Reproduciones de 7 canciones de Sabrina Carpenter")
plt.xlabel("Nombre de la cancion")
plt.ylabel("Reproducciones")
plt.bar(x,y,color=["red","pink","purple","beige","black","yellow","brown"])
plt.show()

#con lineas
df = pd.read_csv("sabrina.csv", delimiter=";")
x=df['track_name'].head(7)
y=df['spotify_global_peak'].head(7)
plt.title("Número de posiciones Globales de 7 canciones")
plt.xlabel("Nombre de la cancion")
plt.ylabel("Posicion Globalmente")
plt.plot(x,y)
plt.show()

#con pastel
df = pd.read_csv("sabrina.csv", delimiter=";")
#x=df['track_name'].head(7)
y=df['track_type'].head(7)
counts = y.value_counts()#aqui hace un conteo del tipo de cancion en la columna track type 
plt.title("Análisis del tipo de pista en 7 canciones de Sabrina Carpenter")
plt.pie(counts,labels=counts.index, autopct='%1.1f%%', colors=["pink","red","black"])
plt.show()



