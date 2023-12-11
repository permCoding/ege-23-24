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

balls = []
for row in rows:
    td = row.find_all('td')[-1]
    ball = int(td.text.strip())
    balls.append(ball)

print(sum(balls) / len(balls))
