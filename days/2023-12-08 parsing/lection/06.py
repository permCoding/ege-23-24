from module import get


with open('./data/page.html', 'w', encoding='utf8') as f:
    f.write(get('https://pcoding.ru/parsing/03/page.html'))
