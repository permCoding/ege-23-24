from requests import get


def get_html(url):
    return get(url).text


def get_refs(html):
    pass


artists = {
    "Billie Eilish": 49425,
    "Король и Шут": 1701
}

name = 'Billie Eilish'
link = artists[name]
url = 'https://rur.hitmotop.com/artist/' + str(link)
html = get_html(url)
refs = get_refs(html)

