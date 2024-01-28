import requests
import re


def get_html(url):
    resp = requests.get(url)
    resp.encoding = 'utf8'
    return resp.text


def get_groups_names(html):
    ptn = r'<td class="td__group">ИС-2</td>'
    ptn = r'<td class="td__group">.{2,12}</td>'
    ptn = r'<td class="td__group">.+</td>'
    ptn = r'<td class="td__group">(.+)</td>'
    res = re.findall(ptn, html)
    # lst = []
    # for elm in res:
    #     if elm not in lst:
    #         lst.append(elm)
    return sorted(set(res), key=lambda x: x.split('-')[1])


url = 'https://pcoding.ru/parsing/03/page.html'
html = get_html(url)
groups = get_groups_names(html)
print(groups)

# <td class="td__group">ИС-2</td>