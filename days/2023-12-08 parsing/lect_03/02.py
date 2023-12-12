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
    # search ищет совпадение со всеми символами с любого места строки


def get_time_3(lst):
    a, b = lst[0]
    ptn = '\D*([0-9]{2}:[0-9]{2})'
    x, y = re.match(ptn, a), re.match(ptn, b)
    print(x.group(1), y.group(1))
    # match ищет совпадение со всеми символами с начала строки


url = 'https://pogoda7.ru/prognoz/gorod701-Russia-Permskiy_kray-Perm'
html = requests.get(url).text
lst = get_data_re(html)

get_time_1(lst)
get_time_2(lst)
get_time_3(lst)

"""
<div class="sunrise_set tooltip" title="Восход и закат солнца">
                    Восход: 09:49<br>
                    Закат: 16:26                </div>
"""