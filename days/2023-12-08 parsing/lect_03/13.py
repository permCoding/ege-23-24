import requests
from bs4 import BeautifulSoup


def get_html(url):
    resp = requests.get(host+link)
    resp.encoding = 'utf8'
    return resp.text


def get_refs_1(htlm):
    bs = BeautifulSoup(html, 'html.parser')
    tags = bs \
        .find_all('table')[-1] \
        .find_all('a')
    return [(tag.text, tag['href']) for tag in tags]


def check(tag):
    u1 = tag.name == 'a'
    u2 = tag.has_attr('class')
    u3 = tag.has_attr('target')
    return u1 and not(u2) and u3


def get_refs_2(htlm):
    bs = BeautifulSoup(html, 'html.parser')
    tags = bs.find_all(check)
    return [(tag.text, tag['href']) for tag in tags]


host = 'https://pcoding.ru/'
link = 'darkNet.php'
html = get_html(host+link)
refs = get_refs_2(html)

print(len(refs))
for ref in refs: print(ref)

'''
<a class="links" href="https://pcoding.ru/pdf/backpack.pdf" target="_blank">
    backpack.pdf
</a>
'''