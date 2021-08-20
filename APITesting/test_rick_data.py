import requests

response = requests.get("https://rickandmortyapi.com/api/character")

assert response.status_code == 200

data = response.json()
print(data)
print(data["info"]["671"])
assert(data["info"]["671"])

