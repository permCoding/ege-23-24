import requests
import re


def get_html(url):
    resp = requests.get(url)
    resp.encoding = 'utf8'
    return resp.text


def get_links(html):
    ptn = '<li>(.+?)</li>'
    res = re.findall(ptn, html, re.DOTALL)
    return [elm.strip() for elm in res]


def get_pairs_index(links):
    pairs = []
    for elm in links:
        ptn = '<a href="(.+?)">(.+?)</a>'
        res = re.search(ptn, elm)
        print(res[2].ljust(12, ' '), res[1])
        pairs.append((res[2], res[1]))
    return pairs 


def get_pairs_names(links):
    pairs = []
    for elm in links:
        ptn = '<a href="(?P<link>.+?)">(?P<title>.+?)</a>'
        res = re.search(ptn, elm)
        print(res['title'].ljust(12, ' '), res['link'])
        pairs.append((res['title'], res['link']))
    return pairs 


def save_to_file(filename, pairs):
    f = open(filename, 'w', encoding='utf8')
    for pair in pairs:
        f.write(pair[0].ljust(12, ' ') + pair[1] + '\n')
    f.close()


url = 'https://pcoding.ru/parsing/01/page.html'
html = get_html(url)
links = get_links(html)
pairs = get_pairs_index(links)
pairs = get_pairs_names(links)
save_to_file('./data.txt', pairs)

"""
<li>
    <a href="https://www.notik.ru/goods/smarts-asus-zenfone-3-deluxe-zs570kl-gold-48551.htm">Notik</a>
</li>

"""