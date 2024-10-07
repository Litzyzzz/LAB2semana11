#TANIA DEL CARMEN QUINTANILLA LOZANO
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('vgsales.csv')

games = df['Name'].head(5)
sales = df['Global_Sales'].head(5)

# Crear gráfico de barras
plt.bar(games, sales, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.title('Ventas Globales de Videojuegos')
plt.xlabel('JUEGOS')
plt.ylabel('VENTAS (millones)')
plt.show()

#https://www.kaggle.com/gregorut/videogamesales

"""
El grafico muestra las ventas globales de los cinco videojuegos mas vendidos del dataset. 
Se nota que uno de los juegos tiene ventas mucho mas altas que los demas, lo que refleja 
su popularidad. Esto nos sugiere que hay varios factores, como la plataforma o la publicidad, 
que influyen en las ventas de cada titulo. En resumen, algunos juegos destacan mucho mas que otros en el mercado.
"""