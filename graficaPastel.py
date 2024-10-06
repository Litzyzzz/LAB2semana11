import matplotlib.pyplot as plt
import pandas as pd

#link del dataset https://www.kaggle.com/datasets/delfinaoliva/sabrina-carpenter-discography


#con pastel
df = pd.read_csv("sabrina.csv", delimiter=";")
#x=df['track_name'].head(7)
y=df['track_type'].head(7)
counts = y.value_counts()#aqui hace un conteo del tipo de cancion en la columna track type 
plt.title("Análisis del tipo de pista en 7 canciones de Sabrina Carpenter")
plt.pie(counts,labels=counts.index, autopct='%1.1f%%', colors=["pink","red","black"])
plt.show()



