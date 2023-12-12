import requests
from bs4 import BeautifulSoup
import wget  # pip install wget


def get_html(url):
    resp = requests.get(url)
    resp.encoding = 'utf8'
    return resp.text


def get_refs(htlm):
    bs = BeautifulSoup(html, 'html.parser')
    tags = bs \
        .find_all('table')[-1] \
        .find_all('a')
    return [(tag.text, tag['href']) for tag in tags]


def load_file_1(folder, filename, url):
    txt = get_html(url)
    with open(f"{folder}{filename}", 'w', encoding='utf8') as f:
        f.write(txt)


def load_file_2(folder, filename, url):
    wget.download(url, f"{folder}{filename}")


host = 'https://pcoding.ru/'
link = 'darkNet.php'
html = get_html(host+link)
refs = get_refs(html)

print(len(refs))
filename, url = refs[1]
print(filename, url)
load_file_2('./files/', filename, url)
