import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sabrina.csv")
frec=df["track_name", "spotify_global_peak"].value_counts()
plt.bar(frec.values,frec.index)

plt.show()

