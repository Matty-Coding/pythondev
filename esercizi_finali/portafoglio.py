# PORTAFOGLIO

# classe Portafoglio
# costruttore dizionario con criptvalute e quantità
# metodo valore_totale() usa le API di CoinGecko 
# per calcolare totale in USD

import requests

class Portafoglio:
    def __init__(self, criptodict):
        self.criptodict = criptodict

    def valore_totale(self):
        ids = ",".join(self.criptodict.keys())
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
        res = requests.get(url).json()
        totale = 0
        for c, q in self.criptodict.items():
            totale += res[c]["usd"] * q
        return totale
    

port = Portafoglio({"bitcoin": 0.5, "ethereum": 2})
print("Valore USD:", port.valore_totale())


# https://publicapis.io/coin-gecko-api


