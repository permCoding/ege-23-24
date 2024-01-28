import requests
import re


def get_html(url):
    resp = requests.get(url)
    resp.encoding = 'utf8'
    return resp.text


def get_balls(html):
    ptn = r'<td class="td__ball">194</td>'
    ptn = r'<td class="td__ball">.+</td>'
    ptn = r'<td class="td__ball">\d+</td>'
    ptn = r'<td class="td__ball">(\d+)</td>'
    # ptn = r'(?<=<td class="td__ball">)\d+(?=</td>)'
    # ptn = r'(<td class="td__ball">)(\d+)(</td>)'
    res = re.findall(ptn, html)
    # for elm in res: print(elm[0], elm[1], elm[2])
    # return sorted(int(elm) for elm in res)
    return sorted(map(int, res))


url = 'https://pcoding.ru/parsing/03/page.html'
html = get_html(url)
balls = get_balls(html)
print(balls)
print(max(balls), min(balls), sum(balls)/len(balls))

# <td class="td__ball">194</td>