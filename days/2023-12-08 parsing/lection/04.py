from module import get
from bs4 import BeautifulSoup  # pip install bs4


url = 'https://pcoding.ru/parsing/03/page.html'
html = get(url)

soup = BeautifulSoup(html, 'html.parser')  # lxml html5

tags = soup.find_all('td', class_="td__ball")
print(tags)

tags = soup.find_all('td', {"class": "td__ball"})
print(tags)

dct = dict()
dct["class"] = "td__ball"
tags = soup.find_all('td', dct)
print(tags)


for tag in tags: print(tag.text)

# def lambda
# re
