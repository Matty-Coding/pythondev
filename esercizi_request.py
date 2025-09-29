import shutil, requests

# r = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# print("Status code -->", r.status_code)
# print("Headers -->", r.headers)
# print("Risposta in JSON -->", r.json())


# --------------

# payload = {"userId": 2}
# r = requests.get("https://jsonplaceholder.typicode.com/posts", params=payload)
# contenuto = r.json()

# def estrai_title(dizionario):
#     return {"title" : dizionario["title"]}

# titoli = []
# for i in contenuto:
#     titoli.append(estrai_title(i))

# print("Solo titoli:\n")
# for i in titoli:
#     print(i)


# -----------------

# dati_post = {"title": "Python", "body": "Sto studiando requests", "userId": 10}

# r_post = requests.post("https://jsonplaceholder.typicode.com/posts", json=dati_post)

# print("Status Code -->", r_post.status_code)
# print("Risposta server -->", type(r_post.json()))


# -------------


# r = requests.get(
#     "https://httpbin.org/headers", 
#     headers={
#         "User-Agent": "CorsoPython/2.0",
#         "Authorization": "Bearer 12345"
#         }
#     )

# print("Chech headers -->", r.json())


# --------------


# r = requests.get("https://www.python.org/static/img/python-logo.png")

# try:
#     with open("logo.png", "wb") as f:
#         f.write(r.content)
#     print("File salvato correttamente.")
# except Exception as e:
#     print("Errore -->", e)


# -------------------


# sessione = requests.Session()

# r = sessione.get("https://httpbin.org/cookies/set/testcookie/12345")
# r = sessione.get("https://httpbin.org/cookies/set/provacookie/5678")

# r1 = sessione.get("https://httpbin.org/cookies") 

# print("\nStatus Code -->", r1.status_code)
# print(r1.json())


# ------------------

# try:
#     r = requests.get("https://httpbin.org/delay/5", timeout=3)
#     print("Connessione avvenuta correttamente.")

# except requests.exceptions.Timeout:
#     print("Errore, tempo scaduto.")

