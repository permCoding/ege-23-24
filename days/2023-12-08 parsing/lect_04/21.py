import requests
from bs4 import BeautifulSoup

def get_html(host):
    url = host + '/test?theme=414&sort=ids'
    headers = { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf8'
    return resp.text


host = 'https://inf-ege.sdamgia.ru'
html = get_html(host)
bs = BeautifulSoup(html, 'html.parser')
tags = bs.find_all('span', class_="prob_nums")
for tag in tags:
    a = tag.find('a')
    link = host + a.attrs['href']
    title = a.text
    print(title, link)

'''
<span style="" class="prob_nums">
    Тип 25&nbsp;№&nbsp;
    <a href="/problem?id=61405">61405</a> 
    <img src="/img/briefcase--plus.png" class="briefcase" style="filter: grayscale(0.8);" onclick="login_popup();" title="Добавить в вариант">
</span>
'''
