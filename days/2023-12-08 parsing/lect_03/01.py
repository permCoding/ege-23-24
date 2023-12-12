import requests
from bs4 import BeautifulSoup
import re


def get_data_bs4(html):
    sp = BeautifulSoup(html, 'lxml')
    tags = sp.find_all('div', class_="sunrise_set")
    lst = []
    for tag in tags:
        row = (
            tag.next_element.strip(),
            tag.next_element.next_element.next_element.strip()
        )
        lst.append(row)
    return lst


def get_data_re(html):
    ptn = '<div class="sunrise_set.+?>\s*(\S.*?)\s*<br/>\s*(\S.*?)\s*</div>'
    return re.findall(ptn, html, re.DOTALL)[1:]


url = 'https://pogoda7.ru/prognoz/gorod701-Russia-Permskiy_kray-Perm'
html = requests.get(url).text
# lst = get_data_bs4(html)
lst = get_data_re(html)

for row in lst: print(row)
"""
<div class="sunrise_set tooltip" title="Восход и закат солнца">
                    Восход: 09:49<br>
                    Закат: 16:26                </div>
"""