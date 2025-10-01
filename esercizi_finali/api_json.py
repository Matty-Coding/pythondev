# API e JSON

# chiama l'API
# recupera i primi 5 host 
# salvali in post.json
# apri il file creato e stampalo

import requests, json

api = "https://jsonplaceholder.typicode.com/posts"

r = requests.get(api)
primi_5 = r.json()[:5]

with open("esercizi_finali/post.json", "w") as f:
    json.dump(primi_5, f, indent=4)

with open("esercizi_finali/post.json", "r") as f:
    print(f.read())