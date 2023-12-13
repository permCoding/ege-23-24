from requests import get
from bs4 import BeautifulSoup


def get_html(url):
    return get(url).text


def get_refs(html):
    bs = BeautifulSoup(html, "html.parser")
    tags = bs.find_all('div', class_="track__info")
    lst = []
    for tag in tags:
        title = tag.find('div', class_="track__title").text.strip()
        time = tag.find('div', class_="track__fulltime").text.strip()
        ref = tag.find('a', class_="track__download-btn")['href']
        lst.append((title, time, ref))
    return lst


def load_file(url, folder, filename):
    with open(f"{folder}{filename}", 'wb') as f:
        f.write(get(url).content)


artists = {
    "Billie Eilish": 49425,
    "Король и Шут": 1701
}

name = 'Billie Eilish'
link = artists[name]
url = 'https://rur.hitmotop.com/artist/' + str(link)
html = get_html(url)
refs = get_refs(html)

for ref in refs[:3]:
    print(ref)
    load_file(ref[2], './files/', ref[2].split('/')[-1])

"""
<div class="track__info">
    <a href="/song/63154737" class="track__info-l">
        <div class="track__title">
                                        bad guy
                                </div>
        <div class="track__desc">Billie Eilish</div>
    </a>

    <div class="track__info-r">
        <div class="track__time">

                                    
            <div class="track__fulltime">03:12</div>
            <div class="track__duration"></div>
        </div>

        <a data-nopjax="" href="https://rur.hitmotop.com/get/music/20190330/Billie_Eilish_-_bad_guy_63154737.mp3" class="track__download-btn"></a>
        <span data-nopjax="" class="track__download-btn track__like-btn" data-track-id="63154737"></span>
    </div>
</div>
"""

