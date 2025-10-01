# GITHUB API

# chiedi un nome utente
# stampa login, nome, repo pubblici, data creazione
# gestisci errore se l'utente non esiste

import requests, json

nome = input("Inserisci nome utente github: ").strip()

r = requests.get(f"https://api.github.com/users/{nome}")
if r.status_code == 200:
    jsondata = r.json()
    print(f"""
          Login: {jsondata["login"]}\n
          Nome: {jsondata["name"]}\n
          Repository pubblici: {jsondata["public_repos"]}\n
          Data Creazione: {jsondata["created_at"]}
    """)

else:
    print("Utente non trovato.")
