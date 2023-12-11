import requests
import re


url = 'https://pcoding.ru/parsing/03/page.html'
resp = requests.get(url)
resp.encoding = 'utf8'
html = resp.text

# ptn = '<td class="td__ball">(.{2,3})</td>'
# ptn = '<td class="td__ball">([0-9]{2,3})</td>'
# ptn = '<td class="td__ball">(\d{2,3})</td>'
# ptn = '<td class="td__ball">(\d+)</td>'
ptn = '>(\d+)<'
ptn = '>\s*(\d+)\s*<'
balls = [int(elm) for elm in re.findall(ptn, html)]
print(balls)
print(sum(balls) / len(balls))

# <td class="td__ball">150</td>