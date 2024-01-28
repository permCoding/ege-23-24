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


url = 'https://pcoding.ru/parsing/01/page.html'
html = get_html(url)
# with open('./page.html', mode='w', encoding='utf8') as f:
#     f.write(html)
links = get_links(html)
f = open('./data.txt', 'w', encoding='utf8')
for elm in links:
    # print(elm)
    ptn = '<a href="(.+?)">(.+?)</a>'
    res = re.search(ptn, elm)
    # print(res[2], res[1])
    # print(res[2], '\t', res[1])
    # print(f"заголовок - {res[2]}; ссылка - {res[1]}")
    print(res[2].ljust(12, ' '), res[1])
    f.write(res[2].ljust(12, ' ') + res[1] + '\n')
f.close()

"""
<li>
    <a href="https://www.notik.ru/goods/smarts-asus-zenfone-3-deluxe-zs570kl-gold-48551.htm">Notik</a>
</li>

"""