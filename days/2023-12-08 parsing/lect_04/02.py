from requests import get
from bs4 import BeautifulSoup
import re


def get_html(url):
    return get(url).text


def get_refs(html):
    bs = BeautifulSoup(html, 'html.parser')
    tags = bs.find_all('a', class_='list-sub__link')
    for tag in tags:
        title = tag.text
        link = url + tag.attrs['href']
        print(title, link)


def get_refs_re(html):
    ptn = 'class="list-sub__link" href="(.+?)">(.+?)</a>'
    tags = re.findall(ptn, html)
    for tag in tags:
        print(tag[1], url + tag[0])


url = 'https://learn.javascript.ru'
html = get_html(url)
get_refs_re(html)


"""
<a class="list-sub__link" href="/intro">Введение в JavaScript</a>
"""