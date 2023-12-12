import requests
from bs4 import BeautifulSoup


def get_html(url):
    resp = requests.get(host+link)
    resp.encoding = 'utf8'
    return resp.text


def get_refs(htlm):
    bs = BeautifulSoup(html, 'html.parser')
    tags = bs.find_all('a', {'target':'_blank'})
    return [(tag.text, tag['href']) for tag in tags]


host = 'https://pcoding.ru/'
link = 'darkNet.php'
html = get_html(host+link)
refs = get_refs(html)

print(len(refs), refs[-1])

'''
<a class="links" href="https://pcoding.ru/pdf/backpack.pdf" target="_blank">
    backpack.pdf
</a>
'''