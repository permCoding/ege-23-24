import requests
import json


def get_json(url):
    headers = { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf8'
    return resp.json()


host = 'https://kompege.ru'
url = 'https://kompege.ru/api/v1/task/11950'
data = get_json(url)
print(json.dumps(data, ensure_ascii=False, indent=4))

print(host+data['files'][0]['url'])
