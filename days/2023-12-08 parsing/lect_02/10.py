import requests
from bs4 import BeautifulSoup
import re


url = 'https://pogoda7.ru/prognoz/gorod701-Russia-Permskiy_kray-Perm'
html = requests.get(url).text

sp = BeautifulSoup(html, 'lxml')
tag = sp.find('div', class_="temperature")
print(tag.text)

ptn = '<div class="temperature.+?>(.+?)</div>'
tmp = re.findall(ptn, html)[0]
print(tmp)

"""
<div class="temperature tooltip" 
    title="Текущая температура в Перми: -27.7°C .. -27.2°C">
-27°C
</div>
"""