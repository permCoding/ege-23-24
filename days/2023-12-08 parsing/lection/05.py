from module import get
from bs4 import BeautifulSoup  # pip install bs4


html = get('https://pcoding.ru/parsing/03/page.html')

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all('td', class_="td__ball"):
    print(tag.text)
