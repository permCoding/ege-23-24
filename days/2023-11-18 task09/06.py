import requests
import json


url = "http://parsing.1gb.ru/tiobe/rate.desc.6"
resp = requests.get(url)
objs = resp.json()

print(json.dumps(objs, indent=2))


"""
https://pcoding.ru/csv/09_2100.txt
http://parsing.1gb.ru/temp/Perm
https://pcoding.ru/fon/proCoding.png
https://pcoding.ru/pdf/sort.pdf
"""