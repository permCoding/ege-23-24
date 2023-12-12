import requests
import re


def get_data_re(html):
    ptn = '<div class="sunrise_set.+?>\s*(\S.*?)\s*<br/>\s*(\S.*?)\s*</div>'
    return re.findall(ptn, html, re.DOTALL)[1:]


def get_time_1(lst):
    a, b = lst[0]
    print(a.split()[1], b.split()[1])


def get_time_2(lst):
    a, b = lst[0]
    ptn = '\d\d:\d\d'
    x, y = re.search(ptn, a), re.search(ptn, b)
    a1,a2 = x.span(); b1,b2 = y.span()
    print(a[a1:a2], b[b1:b2])


url = 'https://pogoda7.ru/prognoz/gorod701-Russia-Permskiy_kray-Perm'
html = requests.get(url).text
lst = get_data_re(html)

get_time_1(lst)
get_time_2(lst)


"""
<div class="sunrise_set tooltip" title="Восход и закат солнца">
                    Восход: 09:49<br>
                    Закат: 16:26                </div>
"""