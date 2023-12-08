from bs4 import BeautifulSoup as BS


f = open('./data/page.html', 'r', encoding='utf8')
html = f.read()
f.close()

sp = BS(html, 'html.parser')

trs = sp \
    .find('table', id='students') \
    .find_all('tr')[1:]
print(len(trs))

trs = sp \
    .find('table', id='students') \
    .find_all('tr', class_='tr__data')
print(len(trs))

trs = sp \
    .find('table', id='students') \
    .find('tr') \
    .find_next_siblings()
print(len(trs))
