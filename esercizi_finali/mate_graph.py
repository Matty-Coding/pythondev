# GENERARE E VISUALIZZARE DATI

# usa numpy per generare 100 numeri casuali
# calcola media, deviazione standard, massimo
# disegna istogramma con matplotlib
# salva il grafico in .png


import numpy as np
import matplotlib.pyplot as plt

array = [np.random.randint(low=1, high=100) for _ in range(100)]

print(f"Media: {np.mean(array)} - Deviazione Standard: {np.std(array):.2f} - Massimo: {np.max(array)}")

plt.hist(array)
plt.savefig("esercizi_finali/graph.png")