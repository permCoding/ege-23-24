import requests
from bs4 import BeautifulSoup
import re


url = 'https://pogoda7.ru/prognoz/gorod701-Russia-Permskiy_kray-Perm'
html = requests.get(url).text

sp = BeautifulSoup(html, 'lxml')
tag = sp.find('div', class_="sunrise_set")

txt = tag.text
print(txt)

tmps = [elm.strip() for elm in txt.strip().splitlines()]
print(tmps)

tmps = [
    tag.next_element.strip(),
    tag.next_element.next_element.next_element.strip()
]
print(tmps)

ptn = '<div class="sunrise_set.+?>(.+?)</div>'
lst = re.findall(ptn, html, re.DOTALL)
print(len(lst))
print(lst[0])

"""
<div class="sunrise_set tooltip" title="Восход и закат солнца">
                    Восход: 09:49<br>
                    Закат: 16:26                </div>
"""