import requests
import json


# url = "https://pcoding.ru/fon/proCoding.png"
url = "https://pcoding.ru/pdf/sort.pdf"
resp = requests.get(url)
cont = resp.content

with open("./proCoding.png", "+wb") as f:
    f.write(cont)


"""
https://pcoding.ru/csv/09_2100.txt
http://parsing.1gb.ru/temp/Perm
https://pcoding.ru/fon/proCoding.png
https://pcoding.ru/pdf/sort.pdf
"""