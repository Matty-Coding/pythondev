import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# # Informational responses (100 – 199)
# # Successful responses (200 – 299)
# # Redirection messages (300 – 399)
# # Client error responses (400 – 499)
# # Server error responses (500 – 599)

# print(response.status_code)
# print(response.headers)
# print(response.text)
# print(response.json())

# -----------

# payload = {"userId" : 1}
# response = requests.get("https://jsonplaceholder.typicode.com/posts", params=payload)

# print(response.status_code)
# print(response.url)

# print(response.json)

# ------------

# data = {"title": "Nuovo Post", "id": 11, "body": "Contenuto", "userId": 1}

# response = requests.post("https://jsonplaceholder.typicode.com/posts", params=payload, json=data)

# print(response.status_code)

# print(response.json())


# -----------------------

# headers = {"User-Agent": "CorsoPython/1.0"}

# response = requests.get("https://httpbin.org/headers", headers=headers)

# print(response.json())

# ------------

# session = requests.Session()
# session.headers.update({"User-Agent": "SessionTest/1.0"})

# r1 = session.get("https://httpbin.org/cookies/set/sessioncookie/123")

# r2 = session.get("https://httpbin.org/cookies")

# print(r2.json())