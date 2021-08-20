import requests

response = requests.get("https://rickandmortyapi.com/api/character")

assert response.status_code == 200

