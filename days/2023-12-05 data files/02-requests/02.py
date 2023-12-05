import requests
import json

url = "https://pcoding.ru/json/clients.json"

response = requests.get(url)
response.encoding = "utf8"
line = response.text

data = json.loads(line)  # строку в объект

clients = data["clients"]  # выбрал поле clients

print(json.dumps(clients[0], ensure_ascii=False, indent=2))