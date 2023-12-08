from module import get
from bs4 import BeautifulSoup  # pip install bs4


url = 'https://pcoding.ru/parsing/03/page.html'
html = get(url)

soup = BeautifulSoup(html, 'html.parser')  # lxml html5

tag = soup.find('title')
print(tag)
print(tag.text)
