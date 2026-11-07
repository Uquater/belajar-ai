import requests

url = "https://catfact.ninja/fact"

response = requests.get(url, timeout=10)
response.raise_for_status()

data = response.json()
print(data["fact"])