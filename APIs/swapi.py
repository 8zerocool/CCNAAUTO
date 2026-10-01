import requests
import json

base_url = "https://swapi.dev/api/"
endpoint = "people/"

response = requests.get(base_url + endpoint)

# print(response.text)
# print(response.status_code)
# print(response.headers)

data = response.json()
print(data['results'][0]['name'])

