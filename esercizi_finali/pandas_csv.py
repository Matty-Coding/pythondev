# PANDAS e file CSV

# crea un file csv con 5 colonne (Nome, Età, Città, Corso, Voto)
# leggi file con pandas
# calcola media voti
# trova lo studente con il voto maggiore
# esporta i risultati in risultati.csv

import pandas as pd

df = pd.read_csv("esercizi_finali/dati.csv", sep=",")

media_voti = df["Voto"].mean()

studente_voto_maggiore = df.loc[df["Voto"] == df["Voto"].max()]

studente_voto_maggiore.to_csv("esercizi_finali/risultati.csv", index=False)
