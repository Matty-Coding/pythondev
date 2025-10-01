# POKEMON API

# classe Pokemon
# costruttore prende nome pokemon
# metodo info() recupera i dati tramite api
# estrai: nome, altezza, peso, abilità
# metodo __str__ restituisci stringa leggibile
# chiedi pokemon, crea oggetto, restituiscilo

import requests

class Pokemon:
    def __init__(self, nome):
        self.nome = nome
        self.data = None

    def info(self):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.nome}")
        if r.status_code == 200:
            self.data = r.json()
        else:
            print("Pokemon non trovato.")

    def __str__(self):
        if self.data:
            abilities = [ability["ability"]["name"] for ability in self.data["abilities"]]

            return f"\n{self.data["name"].upper()} --> Altezza: {self.data["height"]}, Peso: {self.data["weight"]}, Abilità: {", ".join(abilities).title()}\n"

utente = input("\nInserisci il nome di un pokemon: ").strip().lower()
poke = Pokemon(utente)
poke.info()
print(poke)