# GESTORE CSV 

# crea classe GestoreCSV
# costruttore che accetta file csv
# metodo leggi() (modulo pandas)
# metodo statistiche(colonna) -->
# stampa media, massimo, minimo
# metodo salva_json(nome_file) esporta in JSON

import pandas as pd

class GestoreCSV:
    def __init__(self, file):
        self.file = file
        self.df = None

    def leggi(self):
        self.df = pd.read_csv(self.file, sep=",")
        print("Df creato correttamente.")
        return self.df
    
    def statistiche(self, colonna):
        if self.df is not None:
            print(f"Media --> {self.df[colonna].mean():.2f}")
            print(f"Massimo --> {self.df[colonna].max()}")
            print(f"Minimo --> {self.df[colonna].min()}")

    def salva_json(self, nome_file):
        if self.df is not None:
            print("File salvato correttamente in formato JSON.")
            self.df.to_json(f"esercizi_finali/{nome_file}.json", index=False)


gestore = GestoreCSV("esercizi_finali/dati.csv")
gestore.leggi()
gestore.statistiche("Voto")
gestore.salva_json("output_gestore")
