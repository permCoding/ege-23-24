import requests
import re
import m04


def get_data_re(html):
    ptn = '<div class="sunrise_set.+?>\s*(\S.*?)\s*<br/>\s*(\S.*?)\s*</div>'
    return re.findall(ptn, html, re.DOTALL)[1:]


def get_time(elm):
    a, b = elm
    return a.split()[1], b.split()[1]


url = 'https://pogoda7.ru/prognoz/gorod701-Russia-Permskiy_kray-Perm'
html = requests.get(url).text

for elm in get_data_re(html)[1:]:
    a, b = get_time(elm)
    print(a, b, m04.get_day_len(a, b))

"""
<div class="sunrise_set tooltip" title="Восход и закат солнца">
                    Восход: 09:49<br>
                    Закат: 16:26                </div>
"""