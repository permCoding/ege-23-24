import requests  # pip install requests

url = "https://pcoding.ru/csv/09_2100.txt"
resp = requests.get(url)  # open()
lines = resp.text.split('\n')

mx = 0
for line in lines:
    nums = sorted([int(e) for e in line.split(";")])
    a, b, c = nums
    if a**2 + b**2 == c**2:
        mx = max(mx, a+b)
print(mx)

"""
https://pcoding.ru/csv/09_2100.txt
http://parsing.1gb.ru/temp/Perm
https://pcoding.ru/fon/proCoding.png
https://pcoding.ru/pdf/sort.pdf
"""