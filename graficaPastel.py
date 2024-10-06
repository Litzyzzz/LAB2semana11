import matplotlib.pyplot as plt
import pandas as pd

#link del dataset https://www.kaggle.com/datasets/delfinaoliva/sabrina-carpenter-discography


#con pastel
df = pd.read_csv("sabrina.csv", delimiter=";")
#x=df['track_name'].head(7)
y=df['track_musical_genre']
counts = y.value_counts()#aqui hace un conteo del tipo de cancion en la columna track type 
plt.title("Géneros Discográfico de Sabrina Carpenter")
plt.pie(counts,labels=counts.index, autopct='%1.1f%%')
plt.show()

"""
Esta gráfica nos dice que aproximadamente un 22% de la 
discografía de Sabrina Carpenter es de género folk pop, siendo esta
la mayoria

"""


