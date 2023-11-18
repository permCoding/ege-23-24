import requests

url = "https://pcoding.ru/csv/09_2098.txt"
resp = requests.get(url)
lines = resp.text.split('\n')

k = 0
for line in lines:
    x0, y0, x1, y1 = map(int, line.split(";"))
    if (x0==0 or y0==0) and (x1==0 or y1==0):
        k += 1
print(k)

"""
https://pcoding.ru/csv/09_2100.txt
http://parsing.1gb.ru/temp/Perm
https://pcoding.ru/fon/proCoding.png
https://pcoding.ru/pdf/sort.pdf
"""