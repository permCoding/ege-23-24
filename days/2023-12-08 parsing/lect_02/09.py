import requests
from bs4 import BeautifulSoup as BS


url = 'https://pcoding.ru/parsing/03/page.html'
resp = requests.get(url)
resp.encoding = 'utf8'
html = resp.text

bs = BS(html, 'html.parser')
rows = bs \
    .find('table', class_="list") \
    .find_all('tr', class_="tr__data")

data = []
for row in rows:
    group = row.find('td', class_="td__group").text.strip()
    ball = int(row.find('td',class_="td__ball").text.strip())
    data += [(group, ball)]

for group in {elm[0] for elm in data}:
    lst = [x for x in data if x[0]==group]
    avg = sum(x[1] for x in lst) / len(lst)
    print(f"{group:<7}=> {avg:3.2f}")
