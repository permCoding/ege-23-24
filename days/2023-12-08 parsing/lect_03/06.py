import requests
from bs4 import BeautifulSoup


def get_temp(html):
    sp = BeautifulSoup(html, 'lxml')
    return sp.find('div', class_="temperature").text


host = 'https://pogoda7.ru/prognoz/'
links = {
    'gorod701-Russia-Permskiy_kray-Perm': 'Пермь',
    'gorod702-Russia-Permskiy_kray-Berezniki': 'Березники',
    'gorod706-Russia-Permskiy_kray-Dobryanka': 'Добрянка',
    'gorod78840-Russia-Permskiy_kray-Cherdynskiy_rayon-Nyrob': 'Ныроб',
    'gorod148-Russia-Krasnodarskiy_kray-Sochi': 'Сочи',
    'gorod142-Russia-Krasnodarskiy_kray-Krasnodar': 'Краснодар'
}
for link in links.keys():
    html = requests.get(host+link).text
    print(get_temp(html), links[link])

"""
<div class="temperature tooltip" title="Текущая температура в Перми: -20.5°C .. -20.3°C">
-20°C
</div>
"""